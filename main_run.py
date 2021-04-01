from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import pandas as pd
from datetime import datetime

app = Flask(__name__)

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
        return render_template('index.html' ,datas=rows)

@app.route('/question')
def showform():
        return render_template('addquestion.html')

@app.route('/showsimilar')
def showsimilar():
        DataFrame = pd.read_csv('Data_similarity.csv')
        rows = []
        index = len(DataFrame)-1
        rows = []
        x = (index ,DataFrame.at[index,'ID'], DataFrame.at[index,'name'],DataFrame.at[index,'message'],DataFrame.at[index,'tag'],DataFrame.at[index,'time'],DataFrame.at[index,'ques_similar1'],DataFrame.at[index,'anws_similar1'],DataFrame.at[index,'ques_similar2'],DataFrame.at[index,'anws_similar2'],DataFrame.at[index,'ques_similar3'],DataFrame.at[index,'anws_similar3'],DataFrame.at[index,'SatisfactionInSearch'])
        rows.append(x)
        rows = tuple(rows)
        return render_template('similarity.html',rows=rows)

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
        id_data = int(id_data)
        DataFrame = pd.read_csv('Data.csv')
        DataFrame = DataFrame.drop(id_data).reset_index(drop=True)
        DataFrame.to_csv('Data.csv', index=False)
        return redirect(url_for('showdata'))

@app.route('/insert', methods=['POST'])
def insert():
    if request.method=="POST" :
        DataFrame = pd.read_csv('Data.csv')
        name = request.form['name']
        message = request.form['question']
        Tag = requests.post("http://65e11ee57c6f.ngrok.io/predict", data={'text': message})
        Tag = Tag.json()
        Tag = Tag['result']
        dict_tag = {'Personal Rights':'กฎหมายการละเมิด(Personal Rights)', 'family':'กฎหมายครอบครัว(Family)', 'labor':'กฎหมายแรงงาน(Labor)', 'contract':'กฎหมายเอกเทศสัญญา(Contract)', 'criminal':'กฎหมายอาญา(Criminal)'}
        Tag = dict_tag[Tag]
        time = datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
        print(Tag)
        print(time)
        add = pd.DataFrame([[name,message,Tag,time]],columns=['name','message','tag','time'])
        DataFrame = DataFrame.append(add).reset_index(drop=True)
        DataFrame.to_csv('Data.csv', index=False)
        return redirect(url_for('showdata')) 

@app.route('/update', methods=['POST'])
def update():
    if request.method=="POST" :
        id_update = int(request.form['id'])
        name = request.form['name']
        message = request.form['question']
        time = datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
        DataFrame = pd.read_csv('Data.csv')
        DataFrame.loc[id_update,'name'] = name
        DataFrame.loc[id_update,'message'] = message
        DataFrame.loc[id_update,'time'] = time
        DataFrame.sort_values(by=['time'], inplace=True, ascending=True)
        DataFrame = DataFrame.reset_index(drop=True)
        DataFrame.to_csv('Data.csv', index=False)
        return redirect(url_for('showdata'))

@app.route('/similarity', methods=['POST'])
def similarity():
    if request.method=="POST" :
        DataFrame = pd.read_csv('Data_similarity.csv')
        name = request.form['name']
        message = request.form['question']
        r = requests.post("http://127.0.0.1:5006/predictLegalBERTth", data={'text': message})
        response =r.json()
        ID = len(DataFrame)+1
        Tag = response['result_tag']
        Q_similar1 = response['result_Q1']
        A_similar1 = response['result_A1']
        Q_similar2 = response['result_Q2']
        A_similar2 = response['result_A2']
        Q_similar3 = response['result_Q3']
        A_similar3 = response['result_A3']
        dict_tag = {'Personal Rights':'กฎหมายการละเมิด(Personal Rights)', 'family':'กฎหมายครอบครัว(Family)', 'labor':'กฎหมายแรงงาน(Labor)', 'contract':'กฎหมายเอกเทศสัญญา(Contract)', 'criminal':'กฎหมายอาญา(Criminal)'}
        Tag = dict_tag[Tag]
        time = datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
        #print(Tag)
        #print(time)
        #print(Q_similar1)
        #print(A_similar1)
        #print(Q_similar2)
        #print(A_similar2)
        #print(Q_similar3)
        #print(A_similar3)
        add = pd.DataFrame([[ID, name, message, Tag, time, Q_similar1, A_similar1, Q_similar2, A_similar2, Q_similar3, A_similar3]],columns=['ID', 'name', 'message','tag', 'time', 'ques_similar1', 'anws_similar1', 'ques_similar2', 'anws_similar2', 'ques_similar3', 'anws_similar3'])
        DataFrame = DataFrame.append(add).reset_index(drop=True)
        DataFrame.to_csv('Data_similarity.csv', index=False)
        #addTag = pd.DataFrame([[name,message,Tag,time]],columns=['name','message','tag','time'])
        #DataTag = addTag.append(addTag).reset_index(drop=True)
        #DataTag.to_csv('Data_tag.csv', index=False)
        return redirect(url_for('showsimilar'))

@app.route('/saveresult(happy)')
def happy():
        DataFrame = pd.read_csv('Data_similarity.csv')
        DataFrame.loc[[len(DataFrame)-1],'SatisfactionInSearch'] = 'true'
        DataFrame.to_csv('Data_similarity.csv', index=False)
        #DataTag = pd.read_csv('Data_tag.csv')
        #DataTag.drop(DataTag.tail(1).index, inplace = True) 
        #DataTag.to_csv('Data_tag.csv', index=False)
        return redirect(url_for('showdata'))

@app.route('/saveresult(unhappy)')
def unhappy():
        DataFrame = pd.read_csv('Data_similarity.csv')
        DataFrame.loc[[len(DataFrame)-1],'SatisfactionInSearch'] = 'false'
        data = pd.read_csv('Data.csv')
        ID = len(data)+1
        name = DataFrame['name'][len(DataFrame)-1]
        message = DataFrame['message'][len(DataFrame)-1]
        tag = DataFrame['tag'][len(DataFrame)-1]
        time = DataFrame['time'][len(DataFrame)-1]
        add = pd.DataFrame([[ID, name, message, tag, time]],columns=['ID', 'name', 'message','tag', 'time'])
        data = data.append(add).reset_index(drop=True)
        data.to_csv('Data.csv', index=False)
        DataFrame.to_csv('Data_similarity.csv', index=False)
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
        return render_template('select.html', datas=rows)

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
        return render_template('select.html', datas=rows)

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
        return render_template('select.html', datas=rows)

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
        return render_template('select.html', datas=rows)

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
        return render_template('select.html', datas=rows)

if __name__ == "__main__":
    app.run(debug=True, port=5007)