from flask import Flask, request, Response
import os
import json

from awsses import ses_send_email

# App config.
app = Flask(__name__)
app.config.from_object(__name__)

json_data = open('env.json')
env_vars = json.load(json_data)['environment_variables']

# AWS SES Config
SENDER = env_vars['SENDER']
RECIPIENT = env_vars['RECIPIENT']
SES_REGION = env_vars['SES_REGION']
CHARSET = env_vars['CHARSET']

# @TODO: Add URL Lock
@app.route("/", methods=['POST'])
def contact():
    response_message = dict()

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']

        response_message['status'] = ses_send_email(SENDER, RECIPIENT, subject, message + ' ' + phone, SES_REGION, CHARSET)
        resp = Response(response_message, status=200, mimetype='application/json')

        return resp


if __name__ == "__main__":
    app.run()
