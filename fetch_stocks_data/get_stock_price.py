from numpy import e
import yfinance as yf
import pandas as pd
import dataframe_image as dfi

# my portfolio average buys
# wipro = 628.09
# tcs = 3461.87
# irctc = 792.37
# irfc = 24.86
# trident = 47.39
# svam_soft = 4.05
# ongc = 128.35
# hpcl = 275.65
# jeevan_sci = 101

STATIC_PATH = './static/images/'
# in the evening 5.00pm everyday
def get_prices(tickers):
  # tickers = ['TCS.NS','WIPRO.NS','IRCTC.NS']
  d = {}
  for ticker in tickers:
    print("Fetching for ",ticker)
    try:
      stock_info = yf.Ticker(ticker).info
      # stock_info.keys() for other properties you can explore
      market_price = stock_info['regularMarketPrice']
      previous_close_price = stock_info['regularMarketPreviousClose']
      d[ticker] = {'market_price': market_price,'previous_close_price':previous_close_price}
      
    except:
      print('ticker not found:',ticker)

  return pd.DataFrame(d)


def dftoimg(df,file_name):
    # file_name = "mytable.png"
    # 
    
    df_styled = df.style.background_gradient() 
    print("------->",STATIC_PATH+file_name)
    dfi.export(df_styled, STATIC_PATH+file_name,table_conversion="matplotlib")
    


# df = get_prices(tickers)
# df_styled = df.style.background_gradient() 
# dfi.export(df_styled,"mytable.png",table_conversion="matplotlib")
# bot.send_photo(message.chat.id,open("mytable.png",'rb'))