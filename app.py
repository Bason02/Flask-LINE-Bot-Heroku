import os
from datetime import datetime
from flask import Flask, abort, request
import random

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

nlist=[{"國名":"美國","code":"USA","面積":"平方千米"},{"國名":"英國","code":"BPD","面積":"平方千米"},{"國名":"中國","code":"CHN","面積":"平方千米"},{"國名":"台國","code":"TWC","面積":"平方千米"},{"國名":"紐西蘭","code":"NCL","面積":"平方千米"},{"國名":"日本","code":"JPY","面積":"平方千米"},{"國名":"加國","code":"CAD","面積":"平方千米"}]

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
