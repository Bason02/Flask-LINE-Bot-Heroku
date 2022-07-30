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
result = {}
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
    UID=str(event.source.user_id)
    uprofile=line_bot_api.get_profile(UID)
    name=uprofile.display_name
    if event.message.text== "抽" :
        #name=event.message.text[:-1] #-----------------------
        tmps=""
        tmpstr=""
        for k in range(3):     
            a=nlist.pop(random.randint(0,len(nlist)-1))
            tmps+="\n"+a["國名"]+" "+a["code"]+"\n"+"面積："+a["面積"]+"\n"
            tmpstr+=" "+a["國名"]+"、"     
        result[UID]=name+"："+tmpstr[:-1]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result[UID]+"\n"+tmps))
    elif "查詢" == event.message.text :
        ttmp="查詢全部：\n"
        for a,b in result.items():
            ttmp+=b+"\n"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=ttmp))
       
        
    elif event.message.text == "-test":
        t={}
        ttmps=""
        ttmpstr=""
        for k in range(3):     
            ta=nlist.pop(random.randint(0,len(nlist)-1))
            ttmps+="\n"+ta["國名"]+" "+ta["code"]+"\n"+"面積："+ta["面積"]+"\n"
            ttmpstr+=" "+ta["國名"]+"、"     
        t["王一"]="王一"+"："+ttmpstr[:-1]
        print()
        print(t)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=t["王一"]+"\n"+ttmps))
