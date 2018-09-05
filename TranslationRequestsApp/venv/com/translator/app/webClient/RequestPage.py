from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from com.translator.app.core import TranslationsService

trans_app = Flask(__name__);
Bootstrap(trans_app)
service = TranslationsService.TranslationsService()

@trans_app.route('/',methods=['GET'])
def index():
    print('Call to index received ... ')
    trans_request_data = service.queryRequests()
    return render_template('TranslationRequestsPage.html',data=trans_request_data);


@trans_app.route('/SubmitRequest',methods=['POST','GET'])
def submitRequest():
    print('Submitting new Request for text:')
    text = request.args['submittedText']
    print(text)
    if text is not None and len(text) != 0:
        service.submitRequest(text)

    trans_request_data = service.queryRequests()
    return render_template('TranslationRequestsPage.html',data=trans_request_data);


@trans_app.route('/pending',methods=['GET'])
def pendingRequest():
    trans_request_data = service.queryRequests()
    return render_template('TranslationRequestsPage.html',data=trans_request_data);






