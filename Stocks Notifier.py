import requests
import smtplib
import html
def art():
    global loops
    news = requests.get('https://newsapi.org/v2/everything?q=tesla stocks&from=2024-08-09&sortBy=publishedAt&apiKey=ac4ad73e79354760b4545de3417c3211')
    news_j = news.json()
    for articles in news_j['articles']:
        loops +=1
        if loops <= 3:
            unescape_description = html.unescape(articles['description'])
            unescape_title = html.unescape(articles['title'])
            connection.sendmail(from_addr='your_email', to_addrs='your_email', msg=f'Subject:{unescape_title} \n\n{unescape_description}')
        else:
            break

connection = smtplib.SMTP('smtp@mail.com')
connection.starttls()
connection.login(user='your_email',password='your_password')
stocks = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=QAY1F7BDCJ71MOWX')
st_j = stocks.json()
closing_stocks_yesterday =float(st_j['Time Series (Daily)'][list(st_j['Time Series (Daily)'])[1]]['4. close'])
closing_stocks_before = float(st_j['Time Series (Daily)'][list(st_j['Time Series (Daily)'])[2]]['4. close'])
difference = closing_stocks_yesterday - closing_stocks_before
diff_percent = (difference / closing_stocks_before) * 100
loops = 0
if diff_percent >=5:
    print(f'Tesla Stocks are up to {abs(round(diff_percent))}%. News are being sent to your email now')
    art()
elif diff_percent <= -5:
    print(f'Tesla Stocks are down to {abs(round(diff_percent))}%. News are being sent to your email now')
    art()
else:
    print(f'Tesla Stocks are stable at {abs(round(diff_percent))}%.News are being sent to your email now')
    art()







