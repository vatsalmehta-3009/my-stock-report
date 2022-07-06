# in the evening 5.00pm everyday
# send a message to telegram bot
import telebot
import os
from fetch_stocks_data.get_stock_price import get_prices,dftoimg
import pandas as pd
import dataframe_image as dfi

token = "2135617433:AAG78wQaJSgA8QsvoLzltOQx3UiNqafTFbY"
my_chat_id = 952012762
STATIC_PATH = "static/images/"

bot = telebot.TeleBot(token)
print(bot)
bot.send_message(my_chat_id,"Hi")
print(os.getcwd())
print("Photo sent")
tickers = ['TCS.NS',
          # 'WIPRO.NS',
          # 'IRCTC.NS'
          ]
# photo = "mytable.png"
@bot.message_handler(commands=['Greet'])
def greet(message):
  print(message.chat.id)
  bot.reply_to(message,"Hey!Howit going?")

  df = get_prices(tickers)
  dftoimg(df,"mytable.png")

  # df_styled = df.style.background_gradient() 
  # dfi.export(df_styled,"mytable.png",table_conversion="matplotlib")
  bot.send_photo(message.chat.id,open(STATIC_PATH+"mytable.png",'rb'))
bot.polling()