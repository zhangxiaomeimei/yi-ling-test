from flask import Flask, request, abort

import psycopg2

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#from linebot.models import (
#    MessageEvent,TextMessage,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,ButtonsTemplate,PostbackTemplateAction
#)

from linebot.models import *

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

    

    message = TextSendMessage(text=text2) 
    
    
    #傳送貼圖
    Sticker_Message = StickerSendMessage(package_id=1,sticker_id=2) 
    
    #傳送圖片
    Image_Message = ImageSendMessage(original_content_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png',preview_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png')

    Video_Message = VideoSendMessage(original_content_url='https://jylin.myqnapcloud.com/test.mp4', preview_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png')

    Audio_Message = AudioSendMessage(original_content_url='https://jylin.myqnapcloud.com/test.m4a', duration=100000)

    #Location_Message = LocationSendMessage(title='my location', address='Tainan', latitude=22.994821, longitude=120.196452)

    Imagemap_Message = ImagemapSendMessage(
        base_url='https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png#',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='https://ithelp.ithome.com.tw/m/articles/10198142',
                area=ImagemapArea(
                    x=0, y=0, width=520, height=1040
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=0, width=520, height=1040
                )
            )
        ]
    )


    # Buttons_Template = TemplateSendMessage(
    #     alt_text='Buttons Template',
    #     template=ButtonsTemplate(
    #         title='這是ButtonsTemplate',
    #         text='ButtonsTemplate可以傳送text,uri',
    #         thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #         actions=[
    #             MessageTemplateAction(
    #                 label='ButtonsTemplate',
    #                 text='ButtonsTemplate'
    #             ),
    #             URITemplateAction(
    #                 label='VIDEO1',
    #                 uri='https://www.youtube.com/watch?v=YKiMrg6rgYQ'
    #             ),
    #             PostbackTemplateAction(
    #                 label='postback',
    #                 text='postback text',
    #                 data='postback1'
    #             )
    #         ]
    #     )
    # )

      
    # Confirm_Template = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ConfirmTemplate(
    #         title='這是ConfirmTemplate',
    #         text='這就是ConfirmTemplate,用於兩種按鈕選擇',
    #         actions=[                              
    #             PostbackTemplateAction(
    #                 label='Y',
    #                 text='Y',
    #                 data='action=buy&itemid=1'

    #             ),
    #             MessageTemplateAction(
    #                 label='N',
    #                 text='N'
    #             )
    #         ]
    #     )
    # )

    # Carousel_Template = TemplateSendMessage(
    #     alt_text='Carousel template',
    #     template=CarouselTemplate(
    #         columns=[
    #             CarouselColumn(
    #                 thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 title='this is menu1',
    #                 text='description1',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='postback1',
    #                         text='postback text1',
    #                         data='action=buy&itemid=1'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='message1',
    #                         text='message text1'
    #                     ),
    #                     URITemplateAction(
    #                         label='uri1',
    #                         uri='https://www.youtube.com/watch?v=YKiMrg6rgYQ'
    #                     )
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 title='this is menu2',
    #                 text='description2',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='postback2',
    #                         text='postback text2',
    #                         data='action=buy&itemid=2'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='message2',
    #                         text='message text2'
    #                     ),
    #                     URITemplateAction(
    #                         label='連結2',
    #                         uri='https://www.youtube.com/watch?v=GuqY5OViunk'
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    # )

    # Image_Carousel = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ImageCarouselTemplate(
    #         columns=[
    #             ImageCarouselColumn(
    #                 image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 action=PostbackTemplateAction(
    #                     label='postback1',
    #                     text='postback text1',
    #                     data='action=buy&itemid=1'
    #                 )
    #             ),
    #             ImageCarouselColumn(
    #                 image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 action=PostbackTemplateAction(
    #                     label='postback2',
    #                     text='postback text2',
    #                     data='action=buy&itemid=2'
    #                 )
    #             )
    #         ]
    #     )
    # )

    replay_message(event,Imagemap_Message)

 
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