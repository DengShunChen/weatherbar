from flask import Flask, request, abort
import configparser

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")

# Channel Access Token
line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
# Channel Secret
handler = WebhookHandler(config['line_bot']['Channel_Secret'])


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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    if event.message.text == "雷達":
      message = ImageSendMessage(
        original_content_url='https://www.cwb.gov.tw/Data/radar/CV1_TW_1000.png',
        preview_image_url='https://www.cwb.gov.tw/Data/radar/CV1_TW_1000.png'
      )
      line_bot_api.reply_message(event.reply_token, message)
      return 0

carousel_template_message = TemplateSendMessage(
        alt_text='目錄 contains',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://wi-images.condecdn.net/image/doEYpG6Xd87/crop/810/f/weather.jpg',
                    title='天氣資訊',
                    text='請選擇',
                    actions=[
                        MessageAction(
                            label='雷達',
                            text='雷達'
                        ),
                        URIAction(
                            label='氣溫',
                            text='氣溫'
                        ),
                        URIAction(
                            label='氣象局官網',
                            uri='https:www.cwb.gov.tw'
                        )
                    ]
                )
            ]
      )
)

line_bot_api.reply_message(event.reply_token, carousel_template_message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
