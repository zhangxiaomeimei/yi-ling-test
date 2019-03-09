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

line_bot_api = LineBotApi('4WQI6I2rOieaWwWKEfiLw7LizPK9GXt3IR6P7gv7XCsa1WUhT3+Hu4CAxJOZieh0S9jCPN1RlLRTtHvkYR15pirANB51USl+rdYgWi6V0myJLcFfhjLqpNegMbeGqFvC6aU508Hh1F71N24moKSfSgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3df3bf55fa0f5860ac36d18396a5b77')


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