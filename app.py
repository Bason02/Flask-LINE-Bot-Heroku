from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
import os
from datetime import datetime

app = Flask(__name__)
token="yELy9B74H0cL0gkv7XWfMTTOXhVVbQCNGzUufb+D5cX3iW28cUgo6lgvA2V7H8Tc58U9QBAxwrSwENcLOgTPYShDj82BRaH9nZvEYVCPt1AgHV7EyoyV54AfYzhieYSO66cWbhSqrvTWt6n+wywI6QdB04t89/1O/w1cDnyilFU="
ChannelSecrets="6bc6b4178058ab8ccb63ae67fe67385a"

line_bot_api = LineBotApi(os.environ.get(token))
handler = WebhookHandler(os.environ.get(ChannelSecrets))

handler = WebhookHandler(ChannelSecrets)
line_bot_api = LineBotApi(token)
# 收 Line 訊息
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


nlist=[{'國名': 'Country Name', 'code': 'Country Code', '面積': '2018平方千米'}, {'國名': '世界', 'code': 'WLD', '面積': '134542704.08平方千米'}, {'國名': '俄羅斯聯邦', 'code': 'RUS', '面積': '17098250平方千米'}, {'國名': '加拿大', 'code': 'CAN', '面積': '9879750平方千米'}, {'國名': '美國', 'code': 'USA', '面積': '9831510平方千米'}, {'國名': '中國', 'code': 'CHN', '面積': '9600012.9平方千米'}, {'國名': '巴西', 'code': 'BRA', '面積': '8515770平方千米'}, {'國名': '澳大利亞', 'code': 'AUS', '面積': '7741220平方千米'}, {'國名': '印度', 'code': 'IND', '面積': '3287259平方千米'}, {'國名': '阿根廷', 'code': 'ARG', '面積': '2780400平方千 米'}, {'國名': '哈薩克', 'code': 'KAZ', '面積': '2724902平方千米'}, {'國名': '阿爾及利亞', 'code': 'DZA', '面積': '2381741平方千米'}, {'國名': '剛果（金）', 'code': 'COD', '面積': '2344860平方千米'}, {'國名': '沙烏地阿拉伯', 'code': 'SAU', '面積': '2149690平方千米'}, {'國名': '墨西哥', 'code': 'MEX', '面積': '1964375平方千米'}, {'國名': '印尼', 'code': 'IDN', '面積': '1916862.2平方千米'}, {'國名': '蘇丹', 'code': 'SDN', '面積': '1854105.405平方千米'}, {'國名': '利比亞', 'code': 'LBY', '面積': '1759540平方千米'}, {'國名': '伊朗伊斯蘭共和國', 'code': 'IRN', '面積': '1745150平方千米'}, {'國名': '蒙古', 'code': 'MNG', '面積': '1564116平方千米'}, {'國名': '秘魯', 'code': 'PER', '面積': '1285220平方千米'}, {'國名': '安哥拉', 'code': 'AGO', '面積': '1246700平方千米'}, {'國名': '南非', 'code': 'ZAF', '面積': '1219090平方千米'}, {'國名': '哥倫比亞', 'code': 'COL', '面積': '1141750平方千米'}, {'國名': '衣索比亞', 'code': 'ETH', '面積': '1136259.41平方千米'}, {'國名': '玻利維亞', 'code': 'BOL', '面積': '1098580平方千米'}, {'國名': '阿拉伯埃及共和國', 'code': 'EGY', '面積': '1001450平方千米'}, {'國名': '坦尚尼亞', 'code': 'TZA', '面積': '947300平方千米'}, {'國名': '奈及利亞', 'code': 'NGA', '面積': '923770平方千米'}, {'國名': '委內瑞拉玻利瓦爾省共和國', 'code': 'VEN', '面積': '912050平方千米'}, {'國名': '巴基斯坦', 'code': 'PAK', '面積': '796100平方千米'}, {'國名': '土耳其', 'code': 'TUR', '面積': '785350平方千米'}, {'國名': '智利', 'code': 'CHL', '面積': '756700平方千米'}, {'國名': '緬甸', 'code': 'MMR', '面積': '676590平方千米'}, {'國名': '阿富汗', 'code': 'AFG', '面積': '652860平方千米'}, {'國名': '南蘇丹', 'code': 'SSD', '面積': '633906.576平方千米'}, {'國名': '挪威', 'code': 'NOR', '面積': '625221.59平方千米'}, {'國名': '中非共和國', 'code': 'CAF', '面積': '622980平方千米'}, {'國名': '烏克蘭', 'code': 'UKR', '面積': '603550平方千米'}, {'國名': '馬達加斯加', 'code': 'MDG', '面積': '587295平方千米'}, {'國名': '肯亞', 'code': 'KEN', '面積': '580370平方千米'}, {'國名': '法國', 'code': 'FRA', '面積': '549087平方千米'}, {'國名': '葉門共和國', 'code': 'YEM', '面積': '527970平方千米'}, {'國名': '泰國', 'code': 'THA', '面積': '513120平方千米'}, {'國名': '西班牙', 'code': 'ESP', '面積': '505957.289平方千米'}, {'國名': '瑞典', 'code': 'SWE', '面積': '447430平方千米'}, {'國名': '摩洛哥', 'code': 'MAR', '面積': '446550平方千米'}, {'國名': '伊拉克', 'code': 'IRQ', '面積': '435052平方千米'}, {'國名': '加勒比小國', 'code': 'CSS', '面積': '434990平方千米'}, {'國名': '巴拉圭', 'code': 'PRY', '面積': '406752平方千米'}, {'國名': '辛巴威', 'code': 'ZWE', '面積': '390760平方千米'}, {'國名': '日本', 'code': 'JPN', '面積': '377974平方千米'}, {'國名': '德國', 'code': 'DEU', '面積': '357580平方千米'}, {'國名': '剛果（布）', 'code': 'COG', '面積': '342000平方千米'}, {'國名': '芬蘭', 'code': 'FIN', '面積': '338450平方千米'}, {'國名': '越南', 'code': 'VNM', '面積': '331230平方千米'}, {'國名': '馬來西亞', 'code': 'MYS', '面積': '330345平方千米'}, {'國名': '波蘭', 'code': 'POL', '面積': '312690平方千米'}, {'國名': '阿曼', 'code': 'OMN', '面積': '309500平方千米'}, {'國名': '義大利', 'code': 'ITA', '面積': '302070平方千米'}, {'國名': '菲律賓', 'code': 'PHL', '面積': '300000平方千米'}, {'國名': '布吉納法索', 'code': 'BFA', '面積': '274220平方千米'}, {'國名': '紐西蘭', 'code': 'NZL', '面積': '267710平方千米'}, {'國名': '加蓬', 'code': 'GAB', '面積': '267670平方千米'}, {'國名': '厄瓜多爾', 'code': 'ECU', '面積': '256370平方千米'}, {'國名': '幾內亞', 'code': 'GIN', '面積': '245860平方千米'}, {'國名': '英國', 'code': 'GBR', '面積': '243610平方千米'}, {'國名': '烏干達', 'code': 'UGA', '面積': '241550平方千米'}, {'國名': '羅馬尼亞', 'code': 'ROU', '面積': '238400平方千米'}, {'國名': '阿拉伯敘利亞共和國', 'code': 'SYR', '面積': '185180平方千米'}, {'國名': '柬埔寨', 'code': 'KHM', '面積': '181040平方千米'}, {'國名': '烏拉圭', 'code': 'URY', '面積': '176220平方千米'}, {'國名': '蘇利南', 'code': 'SUR', '面積': '163820平方千米'}, {'國名': '突尼斯', 'code': 'TUN', '面積': '163610平方千米'}, {'國名': '孟加拉', 'code': 'BGD', '面積': '147570平方千米'}, {'國名': '尼泊爾', 'code': 'NPL', '面積': '147180平方千米'}, {'國名': '希臘', 'code': 'GRC', '面積': '131960平方千米'}, {'國名': '尼加拉瓜', 'code': 'NIC', '面積': '130370平方千米'}, {'國名': '朝鮮民主主義人民共和國', 'code': 'PRK', '面積': '120540平方千米'}, {'國名': '馬拉威', 'code': 'MWI', '面積': '118480平方千米'}, {'國名': '厄立特里亞', 'code': 'ERI', '面積': '117600平方千米'}, {'國名': '洪都拉斯', 'code': 'HND', '面積': '112490平方千米'}, {'國名': '賴比瑞亞', 'code': 'LBR', '面積': '111370平方千米'}, {'國名': '保加利亞', 'code': 'BGR', '面積': '111000平方千米'}, {'國名': '古巴', 'code': 'CUB', '面積': '109880平方千米'}, {'國名': '瓜地馬拉', 'code': 'GTM', '面積': '108890平方千米'}, {'國名': '冰島', 'code': 'ISL', '面積': '103000平方千米'}, {'國名': '大韓民國', 'code': 'KOR', '面積': '100370平方千米'}, {'國名': '阿拉伯聯合大公國', 'code': 'ARE', '面積': '98647.9平方千米'}, {'國名': '匈牙利', 'code': 'HUN', '面積': '93030平方千米'}, {'國名': '葡萄牙', 'code': 'PRT', '面積': '92225.6平方千米'}, {'國名': '約旦', 'code': 'JOR', '面積': '89320平方千米'}, {'國名': '克羅埃西亞', 'code': 'HRV', '面積': '88070平方千米'}, {'國名': '奧地利', 'code': 'AUT', '面積': '83879平方千米'}, {'國名': '捷克共和國', 'code': 'CZE', '面積': '78870平方千米'}, {'國名': '巴拿馬', 'code': 'PAN', '面積': '75320平方千米'}, {'國名': '愛爾蘭', 'code': 'IRL', '面積': '70280平方千米'}, {'國名': '斯里蘭卡', 'code': 'LKA', '面積': '65610平方千米'}, {'國名': '立陶宛', 'code': 'LTU', '面積': '65290平方千米'}, {'國名': '太平洋島國', 'code': 'PSS', '面積': '65150平方千米'}, {'國名': '哥斯大黎加', 'code': 'CRI', '面積': '51100平方千米'}, {'國名': '斯洛伐克共和國', 'code': 'SVK', '面積': '49030平方千米'}, {'國名': '多明尼加共和國', 'code': 'DOM', '面積': '48670平方千米'}, {'國名': '愛沙尼亞', 'code': 'EST', '面積': '45340平方千米'}, {'國名': '丹麥', 'code': 'DNK', '面積': '42920平方千米'}, {'國名': '荷蘭', 'code': 'NLD', '面積':'41540平方千米'}, {'國名': '瑞士', 'code': 'CHE', '面積': '41290.39平方千米'}, {'國名': '不丹', 'code': 'BTN', '面積': '38390平方千米'}, {'國名': '幾內亞比索共和國', 'code': 'GNB', '面積': '36130平方千米'}, {'國名': '莫爾達瓦', 'code': 'MDA', '面積': '33850平方千米'}, {'國名': '比利時', 'code': 'BEL', '面積': '30530平方千米'}, {'國名': '海地', 'code': 'HTI', '面積': '27750平方千米'}, {'國名': '以色列', 'code': 'ISR', '面積': '22070平方千米'}, {'國名': '薩爾瓦多', 'code': 'SLV', '面積': '21040平方千米'}, {'國名': '斯洛維尼亞', 'code': 'SVN', '面積': '20480平方千米'}, {'國名': '新赫里多尼亞', 'code': 'NCL', '面積': '18580平方千米'}, {'國名': '科威特', 'code': 'KWT', '面積': '17820平方千米'}, {'國名': '史瓦濟蘭', 'code': 'SWZ', '面積': '17360平方千米'}, {'國名': '卡達', 'code': 'QAT', '面積': '11490平方千米'}, {'國名': '甘比亞', 'code': 'GMB', '面積': '11300平方千米'}, {'國名': '牙買加', 'code': 'JAM', '面積': '10990平方千米'}, {'國名': '黎巴嫩', 'code': 'LBN', '面積': '10450平方千米'}, {'國名': '薩摩亞', 'code': 'WSM', '面積': '2840平方千米'}, {'國名': '盧森堡', 'code': 'LUX', '面積': '2590平方千米'}, {'國名': '開曼群島', 'code': 'CYM', '面積': '264平方千米'}, {'國名': '英屬維爾京群島', 'code': 'VGB', '面積': '150平方千米'}, {'國名': '摩納哥', 'code': 'MCO', '面積': '74.92平方千米'}]
result = {}


# Echo 回應, 相當於學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo_message(event):
    UID=str(event.source.user_id)
    uprofile=line_bot_api.get_profile(UID)
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
        
