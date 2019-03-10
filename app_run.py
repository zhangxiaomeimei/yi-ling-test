from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('OJ//AyvuxgQiWqV7BvxbPGzdQxJ5KoybPgZzmBOvac5mXGMoDDZNak/JVhgAPCMpoqoLdnVN+FITlDIfqs4vjjdyNuF9V+0Z9WDFfbf7f+P6XtUR3RzeziK82sY7er78TQQMPeO8tqFqDsFVv+XudgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8f8d8abb200858801253eedc3d784f80')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()