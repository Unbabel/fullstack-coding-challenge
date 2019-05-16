#import psycopg2
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from UnbabelChallenge import app
from UnbabelChallenge.Exceptions import UnExc

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ekityrat:gC9760_xArfHrl8PDFR1ht4MxvDWwwFu@dumbo.db.elephantsql.com:5432/ekityrat'

db = SQLAlchemy(app)

from UnbabelChallenge.Model.User import User
from UnbabelChallenge.Model.Translation import Translation
from UnbabelChallenge.Model.Languages import Language

def destroy_create():
    db.drop_all()
    db.create_all()
    
def seed():
    source_l = Language(short_name='en', full_name='English')
    target_l = Language(short_name='es', full_name='Spanish')

    db.session.add(source_l)
    db.session.add(target_l)
    db.session.commit()

def delete_translation_by_url(url):
    Translation.query.filter(Translation.callback_url == url).delete()
    db.session.commit()
    return;

def get_translation_by_url(url):
    return Translation.query.filter(Translation.callback_url == url).one()

def get_languages():
    return Language.query.all()

def get_language(id):
    return Language.query.filter(Language.id == id).one()

def get_user_by_username(username):
    try:
        result = User.query.filter_by(username=username).first()
        return result
    except Exception as e:
        return UnExc.DB_ERROR

def get_user_by_email(email):
    try:
        result = User.query.filter_by(email=email).first()
        return result
    except Exception as e:
        return UnExc.DB_ERROR

def add_user(username, email, password_hash):
    try:
        tmp_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(tmp_user)
        db.session.commit()
    except Exception as e:
        return UnExc.DB_ERROR

def save_changes():
    try:
        db.session.commit()
    except Exception as e:
        return UnExc.DB_ERROR

def get_translations(user_id):
    try: 
        result = Translation.query.filter_by(user_id=user_id).all()
        return result
    except Exception as e:
        print(e)
        return UnExc.DB_ERROR

def get_translation_urls(user_id):
    try: 
        result = Translation.query.filter_by(user_id=user_id).all().options(load_only("callback_url"))
        return result
    except Exception as e:
        print(e)
        return UnExc.DB_ERROR

def get_translation_by_id(id):
    try:
        result = Translation.query.get(id)
        return result
    except:
        return UnExc.DB_ERROR

def add_translation(text, original_language, target_language, user_id, status, callback_url):
    try:
        tmp_translation = Translation(
            text = text, 
            request_date=datetime.now(), 
            status=status, 
            callback_url=callback_url, 
            user_id=user_id, 
            source_language_id=db.session.query(Language).filter(Language.short_name == original_language).one().id,
            target_language_id=db.session.query(Language).filter(Language.short_name == target_language).one().id)

        db.session.add(tmp_translation)
        db.session.commit()
    except Exception as e:
        raise UnExc.DB_ERROR