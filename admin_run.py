from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/login')
def showlogin():
        return render_template('add_login.html')

@app.route('/')
def showdata():
        DataFrame = pd.read_csv('Data.csv')
        DataFrame.fillna('', inplace=True)
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('index_login.html' ,datas=rows)

# Route for handling the login page logic
@app.route('/addmin', methods=['POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != 'admin' or password != 'admin':
            return render_template('login_errors.html')
        else:
            return redirect(url_for('showdata'))

@app.route('/login_errors')
def login_errors():
        return render_template('login_errors.html')

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
        id_data = int(id_data)
        DataFrame = pd.read_csv('Data.csv')
        DataFrame = DataFrame.drop(id_data).reset_index(drop=True)
        DataFrame.to_csv('Data.csv', index=False)
        return redirect(url_for('showdata'))
        
@app.route('/anw', methods=['POST'])
def anw():
    if request.method=="POST" :
        id_update = int(request.form['id'])
        TheAnswer = request.form['TheAnswer']
        DataFrame = pd.read_csv('Data.csv')
        DataFrame.loc[id_update,'TheAnswer'] = TheAnswer
        DataFrame.to_csv('Data.csv', index=False)
        return redirect(url_for('showdata'))

@app.route('/กฎหมายการละเมิด(Personal Rights)')
def tag1():
        DataFrame = pd.read_csv('Data.csv')
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        DataFrame = DataFrame[DataFrame['tag'] == 'กฎหมายการละเมิด(Personal Rights)'].reset_index(drop=True)
        DataFrame.fillna('', inplace=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('select_login.html', datas=rows)

@app.route('/กฎหมายครอบครัว(Family)')
def tag2():
        DataFrame = pd.read_csv('Data.csv')
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        DataFrame = DataFrame[DataFrame['tag'] == 'กฎหมายครอบครัว(Family)'].reset_index(drop=True)
        DataFrame.fillna('', inplace=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('select_login.html', datas=rows)

@app.route('/กฎหมายแรงงาน(Labor)')
def tag3():
        DataFrame = pd.read_csv('Data.csv')
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        DataFrame = DataFrame[DataFrame['tag'] == 'กฎหมายแรงงาน(Labor)'].reset_index(drop=True)
        DataFrame.fillna('', inplace=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('select_login.html', datas=rows)

@app.route('/กฎหมายเอกเทศสัญญา(Contract)')
def tag4():
        DataFrame = pd.read_csv('Data.csv')
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        DataFrame = DataFrame[DataFrame['tag'] == 'กฎหมายเอกเทศสัญญา(Contract)'].reset_index(drop=True)
        DataFrame.fillna('', inplace=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('select_login.html', datas=rows)

@app.route('/กฎหมายอาญา(Criminal)')
def tag5():
        DataFrame = pd.read_csv('Data.csv')
        #DataFrame = DataFrame[DataFrame['SatisfactionInSearch'] == False].reset_index(drop=True)
        DataFrame = DataFrame[DataFrame['tag'] == 'กฎหมายอาญา(Criminal)'].reset_index(drop=True)
        DataFrame.fillna('', inplace=True)
        rows = []
        for i in range(len(DataFrame)-1,-1,-1) :
                x = (i,DataFrame.at[i,'ID'],DataFrame.at[i,'name'],DataFrame.at[i,'message'],DataFrame.at[i,'tag'],DataFrame.at[i,'time'],DataFrame.at[i,'TheAnswer'])
                rows.append(x)
        rows = tuple(rows)
        return render_template('select_login.html', datas=rows)

if __name__ == "__main__":
     app.run(debug=True, port=5600)
    #app.run(host='0.0.0.0', port=5008)

