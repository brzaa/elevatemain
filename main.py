from flask import Flask, render_template, redirect, url_for, request
from plot import *
import datetime
import json
import requests
app = Flask(__name__)
from datetime import date

# Static Page
@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/blog/berita1/')
def berita1():
    return render_template('berita1.html')

@app.route('/blog/berita2/')
def berita2():
    return render_template('berita2.html')

@app.route('/blog/berita3/')
def berita3():
    return render_template('berita3.html')

@app.route('/blog/berita4/')
def berita4():
    return render_template('berita4.html')

@app.route('/blog/berita5/')
def berita5():
    return render_template('berita5.html')

@app.route('/tentangkami/')
def tentangkami():
    return render_template('tentangkami.html')

#Dinamic Page
@app.route('/dashboard/')
def dashboard():
    #ambil data sentimen
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'bitcoin'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'bitcoin'})
    save = open('static/images/wordcloud/bitcoin.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'bitcoin'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    
    script, div = main('bitcoin','01/07/2010',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

@app.route('/dashboard/eth')
def dashboard_eth():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'ethereum'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'ethereum'})
    save = open('static/images/wordcloud/ethereum.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'ethereum'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('ethereum','01/03/2016',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_eth.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

@app.route('/dashboard/bnb')
def dashboard_bnb():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'binance coin'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'binance coin'})
    save = open('static/images/wordcloud/binance coin.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'binance coin'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('binance coin','01/11/2017',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_bnb.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

@app.route('/dashboard/usdt')
def dashboard_usdt():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'tether'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'tether'})
    save = open('static/images/wordcloud/tether.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'tether'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('tether','01/04/2017',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_usdt.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

@app.route('/dashboard/sol')
def dashboard_sol():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'solana'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'solana'})
    save = open('static/images/wordcloud/solana.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'solana'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('solana','01/07/2020',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_sol.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

@app.route('/dashboard/usdc')
def dashboard_usdc():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'usd coin'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'usd coin'})
    save = open('static/images/wordcloud/usd coin.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'usd coin'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('usd coin','01/12/2018',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_usdc.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)
@app.route('/dashboard/ada')
def dashboard_ada():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'cardano'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'cardano'})
    save = open('static/images/wordcloud/cardano.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'cardano'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('cardano','01/12/2017',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_ada.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)
@app.route('/dashboard/xrp')
def dashboard_xrp():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'xrp'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'xrp'})
    save = open('static/images/wordcloud/xrp.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'xrp'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('xrp','21/01/2015',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_xrp.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)
@app.route('/dashboard/dot')
def dashboard_dot():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'polkadot'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'polkadot'})
    save = open('static/images/wordcloud/polkadot.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'polkadot'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('polkadot','01/02/2021',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_dot.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)
    
@app.route('/dashboard/doge')
def dashboard_doge():
    r = requests.post('https://elevatecrypto-api.herokuapp.com/api/datasentiment', json={'status': 'minta datanya dong','koin':'dogecoin'})
    data = r.json()
    tanggals=data['tanggal']
    jams=data['jam']
    #ambil gambar wordcloud
    r2 = requests.post('https://elevatecrypto-api.herokuapp.com/api/wordcloud', json={'status': 'minta datanya dong','koin':'dogecoin'})
    save = open('static/images/wordcloud/dogecoin.png', 'wb').write(r2.content)
    #ambil data forecast
    r3 = requests.post('https://elevatecrypto-api.herokuapp.com/api/forecast', json={'status': 'minta datanya dong','koin':'dogecoin'})
    dataf = r3.json()
    fscript, fdiv = forecast(dataf)
    tanggalf=dataf['date']
    jamf=dataf['jam']
    now = datetime.datetime.now()
    tanggal = date.today()
    sekarang = tanggal.strftime("%d/%m/%Y")
    script, div = main('dogecoin','01/06/2017',sekarang)
    dates = f'{now.day}/{now.month}/{now.year}'
    time = f'{now.strftime("%H")}:{now.strftime("%M")}'
    table1s,table1d = tablenow(f'{now.day-2}/{now.month}/{now.year}',f'{now.day}/{now.month}/{now.year}')
    table2s,table2d = tablecoming(f'{now.day}/{now.month}/{now.year}',f'{now.day+7}/{now.month}/{now.year}')
    pie = piechart(data)
    return render_template('dashboard_doge.html',script=script,div=div,date=dates,time=time,
                           table1s=table1s,table1d=table1d,table2s=table2s,table2d=table2d,
                           pie=pie,fscript=fscript,fdiv=fdiv,jams=jams,tanggals=tanggals,
                           tanggalf=tanggalf,jamf=jamf)

if __name__ == "__main__":
    app.run(host="localhost", port=8000,debug=True)