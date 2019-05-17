"""
All the views and routes configurations

Currently, 4 views exist:
1. **Login** - The root directory for a user that hasn't logged in
2. **Register** - Simple registration page
3. **Translate** - The main view, where the user can request new translations,
and see brief information about previous requests
4. **Translation** - Detailed view for a specific translation

Other than these, there are 4 additional routes that pose as helper
methods:
'/auth'
'/add-new-translation'
'/register-new-user'
'/logout'
"""

from datetime import datetime
from flask import request, redirect, render_template, url_for
from flask_toastr import Toastr
from UnbabelChallenge import app
from UnbabelChallenge.Services import translation_service, db_connection, authentication_service
from UnbabelChallenge.Exceptions import UnExc
from UnbabelChallenge.Model.Translation import Translation
from UnbabelChallenge.Model.Languages import Language
import random
import string
import os


toastr = Toastr()
toastr.init_app(app)

# Create a unique identifier for the translation that then gets used as its callback_url
def create_calback_url(stringLength=10):
    translation_urls = db_connection.get_translation_urls(authentication_service.current_user_id)

    letters = string.ascii_lowercase
    tmp_url =  ''.join(random.choice(letters) for i in range(stringLength))

    if tmp_url in translation_urls:
        create_calback_url(stringLength)
    else:
        return tmp_url


# Performs the process of adding a new translation. 
# Doesn't return its own view.
@app.route('/add-translation', methods = ['POST'])
def add_translation():
    if not authentication_service.logged_in:
        return redirect('/login')

    # Break down received data
    txt = request.form['text']
    original_language = request.form['sourceLanguage']
    target_language = request.form['targetLanguage']
    uid = authentication_service.current_user_id
    
    try:
        cburl = create_calback_url(10)

        result = translation_service.request_translation(original_language, target_language, txt, identifier=cburl)

        if result is not UnExc:
            db_connection.add_translation(text=txt, 
                                          original_language=original_language, 
                                          target_language=target_language, 
                                          user_id=uid, status=result['status'], 
                                          callback_url=cburl)

            return redirect('translate#success')
        else:
            return result
    except Exception as e:
        return UnExc.DB_ERROR

    return redirect('translate#success')

@app.route('/')
@app.route('/login')
def login():    
    return render_template(
        'login.html',
        loggedIn=authentication_service.logged_in,
        title='Login',
        year=datetime.now().year)

@app.route('/translate')
def translate():
    if not authentication_service.logged_in:
        return redirect('/login')

    languages = db_connection.get_languages()
    data = db_connection.get_translations(authentication_service.current_user_id)

    data.sort(key=lambda x: len(x.text), reverse=True)

    data_source_languages = []
    data_target_languages = []

    MAX_CHARS = 400

    for translation in data:
        translation.text = (translation.text[:MAX_CHARS] + ' (...)') if len(translation.text) > MAX_CHARS else translation.text
        tmpSource = db_connection.get_language(translation.source_language_id).short_name
        tmpTarget = db_connection.get_language(translation.target_language_id).short_name
        data_source_languages.append(tmpSource)
        data_target_languages.append(tmpTarget)

    return render_template(
        'translate.html',
        loggedIn=authentication_service.logged_in,
        languages=languages,
        sources=data_source_languages,
        targets=data_target_languages,
        translations = data,
        title='Translations',
        year=datetime.now().year,
    )

@app.route('/register')
@app.route('/registration')
def register():
    return render_template(
        'registration.html',
        loggedIn=authentication_service.logged_in,
        title='Registration',
        year=datetime.now().year)

@app.route('/auth', methods = ['POST'])
def auth():
    alias = request.form['email']
    pw = request.form['password']
    
    user = db_connection.get_user_by_username(alias)

    #check if user exists:
    if  user == None:
        user = db_connection.get_user_by_email(alias)

    if user == None:
        return redirect('/login#no-such-user')
    
    enc_pw = user.password_hash

    authorized = authentication_service.verify_password(enc_pw, pw)
    
    if authorized:
        authentication_service.current_user_id = user.id
        authentication_service.logged_in = True
        return redirect('/translate')

    else:
        return redirect('/login#wrong-password')


@app.route('/translation/delete/<callback_url>')
def delete_translation(callback_url):
    db_connection.delete_translation_by_url(callback_url)
    return redirect('/translate#deleted')

@app.route('/translation/<callback_url>')
def translation(callback_url):

    translation = (db_connection.get_translation_by_url(callback_url))
    slang = db_connection.get_language(translation.source_language_id);
    tlang = db_connection.get_language(translation.target_language_id);


    source_language_fname = slang.full_name + " (" + slang.short_name + ")" 
    target_language_fname = tlang.full_name + " (" + tlang.short_name + ")" 
    date = translation.request_date
    status = translation.status
    text = translation.text
    translated_text = translation.translated_text if translation.translated_text is not None else "Translation not yet available."

    return render_template(
        'translation.html',
        loggedIn=authentication_service.logged_in,
        source_language_text=source_language_fname,
        target_language_text=target_language_fname,
        date=date,
        status=status,
        text=text,
        translated_text=translated_text,
        year=datetime.now().year)

@app.route('/register-new-user', methods = ['POST'])
def register_new_user():
    user = request.form['username']
    email = request.form['email']
    pw = request.form['password']

    pw_h = authentication_service.hash_password(pw)

    db_connection.add_user(user, email, pw_h)
    authentication_service.current_user_id = db_connection.get_user_by_username(user).id

    if authentication_service.current_user_id != -1:
        authentication_service.logged_in = True
        return redirect('/translate')

    else:
        return redirect('/register#unknown-error')

@app.route('/logout')
def logout():
    authentication_service.current_user_id = -1
    authentication_service.logged_in = False
    return redirect('/login')