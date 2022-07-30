Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@Bason02 
hsuanchi
/
Flask-LINE-Bot-Heroku
Public template
Code
Issues
1
Pull requests
Actions
Projects
Wiki
Security
Insights
Flask-LINE-Bot-Heroku/app.py /
@hsuanchi
hsuanchi docs(img): add img for reademe.md
Latest commit 0f86664 on 30 Nov 2020
 History
 1 contributor
40 lines (28 sloc)  1.06 KB

import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
