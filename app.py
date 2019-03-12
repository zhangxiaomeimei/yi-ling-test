from flask import Flask, request, abort

import psycopg2

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,TextMessage,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,ButtonsTemplate,PostbackTemplateAction
)
import os
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ['lineToken'])
# Channel Secret
handler = WebhookHandler(os.environ['lineSecret'])


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    
    text2 = "According to your input, my answer is " + event.message.text
    
    if event.message.text.find("bye")>=0 or event.message.text.find("Bye")>=0 or event.message.text.find("拜拜")>=0:
        text2 = "謝謝您的詢問，希望有機會能再為您服務。"
    if event.message.text.find("你好")>=0 or event.message.text.find("您好")>=0 or event.message.text.find("妳好")>=0:
        text2 = "您好!!很高興跟您傳訊息!"
    if event.message.text.find("會考")>=0:
        text2 = "請找陳昇國!"
    if event.message.text.find("喝酒")>=0:
        text2 = "請找彭振昌，他會灌到你，讓你不要不要的!"
    if event.message.text.find("ChiChi")>=0:
        text2 = "Please find ID:cliff135。"
    if event.message.text.find("助教")>=0:
        text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"
    if event.message.text.find("線性代數")>=0:
        text2 = "目前教授線性代數的老師有陳嘉文、彭振昌、陳昇國、林仁彥，但是大多數老師都可以、也有可能會教授此門課。"
    if event.message.text.find("微積分")>=0:
        text2 = "目前全體老師均有教授微積分的經驗。"
    if event.message.text.find("高等微積分")>=0:
        text2 = "今年教授高等微積分的老師為陳嘉文教授。"
    if event.message.text.find("林仁彥")>=0:
        text2 = "林仁彥老師的專長為最佳化，辦公室在理工大樓八樓A16-815，辦公室電話05-271-7880。"
    if event.message.text.find("彭振昌")>=0:
        text2 = "彭振昌老師的專長為動態系統，辦公室在理工大樓八樓A16-822，辦公室電話05-271-7878。"
    # conn=psycopg2.connect("host=120.113.174.17 port=5432 dbname=mathLineBot user=mathLineBot password=mk8559")
    # cur = conn.cursor()
    # sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
    # cur.execute(sql)
    # rows = cur.fetchall()
    # #text2 = "According to your input, my answer is "
    # text2 = ""
    # for row in rows:
    #     text2 = text2 + str(row[2]) 
    # if text2 == "":
    #     text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"
    

    message = TextSendMessage(text=text2)

    message = StickerSendMessage(package_id=1,sticker_id=2)

    (original_content_url='https://applealmond.com/wp-content/uploads/2018/11/1541078537-090bd6987af814bfa1d1a0bfd919f47d.png',preview_image_url='https://applealmond.com/wp-content/uploads/2018/11/1541078537-090bd6987af814bfa1d1a0bfd919f47d.png')  
    
    replay_message(event,message)
 
def replay_message(event,text):
    #text = 'According to your input, my answer is ' + text
    line_bot_api.reply_message(
        event.reply_token,
         text)
        
def push_message(event,text):
    #text = 'According to your input, my answer is ' + text
    line_bot_api.reply_message(
        event.source.user_id,
        text)        

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
