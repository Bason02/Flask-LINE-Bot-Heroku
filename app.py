 
#-------------------------------------------------
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openpyxl 
from openpyxl import load_workbook
import random

token="yELy9B74H0cL0gkv7XWfMTTOXhVVbQCNGzUufb+D5cX3iW28cUgo6lgvA2V7H8Tc58U9QBAxwrSwENcLOgTPYShDj82BRaH9nZvEYVCPt1AgHV7EyoyV54AfYzhieYSO66cWbhSqrvTWt6n+wywI6QdB04t89/1O/w1cDnyilFU="
ChannelSecrets="6bc6b4178058ab8ccb63ae67fe67385a"

app1 = Flask(__name__)
@app.route("/")
def home():
    return "Hello Flask"
@app.route("/test")
def test():
    return "Hello TEST"

handler = WebhookHandler(ChannelSecrets)
line_bot_api = LineBotApi(token)
# 收 Line 訊息
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


wb = load_workbook('流浪地圖.xlsx')
nlist=[]
result = {}
for j in wb["Data"]:
    tmp={}
    tmp["國名"]=j[0].value
    tmp["code"]=j[1].value
    tmp["面積"]=str(j[3].value)+"平方千米"
    nlist.append(tmp)


# Echo 回應, 相當於學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo_message(event):
    UID=str(event.source.user_id)
    uprofile=line_bot_api.get_profile(UID)
    print(uprofile)
    name=uprofile.display_name ###
    if UID in result and event.message.text== "抽" :
        n2="你抽過了！上次抽的結果是"+result[UID]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n2))
    elif event.message.text== "抽" :
        #name=event.message.text[:-1] #-----------------------
        tmps=""
        tmpstr=""
        for k in range(3):     
            a=nlist.pop(random.randint(0,len(nlist)-1))
            tmps+="\n"+a["國名"]+" "+a["code"]+"\n"+"面積："+a["面積"]+"\n"
            tmpstr+=" "+a["國名"]+"、"     
        result[UID]=name+"："+tmpstr[:-1]
        print()
        print(result)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result[UID]+"\n"+tmps))
        
    elif "查詢" == event.message.text :
        ttmp="查詢全部：\n"
        for a,b in result.items():
            ttmp+=b+"\n"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=ttmp))
        
    elif  event.message.text == "-restart":
        result={}
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="重新啟動"))
        
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
        
        
if __name__ == "__main__":
    app.run()
