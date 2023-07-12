from requests_html import HTMLSession
from datetime import date,datetime
import gspread
url='https://finance.yahoo.com/quote/NIFTYBEES.NS/'
s=HTMLSession()
r=s.get(url)
r.html.render(sleep=1)
stock_name=r.html.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1',first=True).text
# print(stock_name)
stock_price=r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]',first=True).text
# print(stock_price)
open_price=r.html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]',first=True).text
# print(open_price)
previous_close_price=r.html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]',first=True).text
# print(previous_close_price)
today = date.today()
date = today.strftime("%d/%m/%Y")
# print(date)
now= datetime.now()
current_time = now.strftime("%I:%M:%S %p")
# print(current_time)

gc=gspread.service_account(filename='creds.json')
sh=gc.open('stock_sheets').sheet1
stock_list=[date,current_time,stock_name,stock_price,open_price,previous_close_price]
sh.append_row(stock_list)








