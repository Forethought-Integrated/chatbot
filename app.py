from flask import Flask, render_template, request, jsonify
import os
from dbquery import *
import time
#from bs4 import BeautifulSoup4
import json
from tf_idf import *
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello():
	return render_template('hello.html')
	#bot_name,bot_image,company_name,welcome_msg,count =  InitialData('abc123');
	#print(bot_name)
	#ques,option,response,value = Dialogue('abc123',1)
	#print(ques,option,response)
	#return render_template('index.html',count=count,bot_name=bot_name,bot_image=bot_image,company_name=company_name,welcome_msg=welcome_msg,ques=ques,option=option,response=response,value=value)
	#return render_template('index.html',bot_name=bot_name,bot_image=bot_image,company_name=company_name,welcome_msg=welcome_msg)
#


#  ______________________________________________________________________________________________  #


# @app.route('/eela/<unique_id>',methods=['POST','GET'])
# def Initialize(unique_id):
# 	bot_name,bot_image,company_name,welcome_msg,count =  InitialData(unique_id);
# 	#print(bot_name)
# 	ques,option,response,value = Dialogue(unique_id,1)
# 	#print(ques,option,response)
# 	return render_template('index.html',count=count,bot_name=bot_name,bot_image=bot_image,company_name=company_name,welcome_msg=welcome_msg,ques=ques,option=option,response=response,value=value)
#
#
# @app.route("/ask/<unique_id>", methods=['POST','GET'])
# def ask(unique_id):
# 	message = str(request.form['chatmessage'])
# 	count = int(request.form['count'])
# 	#print(count)
# 	option = [1,2,3,4]
# 	bot_response = "bot response"
# 	ques,option,response,value = Dialogue(unique_id,count)
# 	return jsonify({'status':'ok','answer':bot_response,'option':option,'respond':"respond",'ques':ques,'option':option,'response':response,'value':value})
#
#
# @app.route("/submit",methods=['GET','POST'])
# def submission():
# 	#lead = request.data['lead']
# 	data = request.get_json()
# 	LeadInsertion(data)
# 	msg,fb,ln,tw,insta = FinalMessage('abc123')
# 	#print(msg,fb,ln,tw,insta)
# 	return jsonify({'status':'ok','message':msg,'facebook':fb,'linkedin':ln,'tweet':tw,'insta':insta})
#
# @app.route("/askbot",methods=['GET','POST'])
# def AskBot():
# 	message = str(request.form['chatmessage'])
# 	bot_response,score = previous_chats(message)
# 	print(bot_response)
# 	return jsonify({'status':'ok','answer':bot_response})
#
# @app.route("/showlead")
# def ShowLead():
# 	data = ShowLeadGeneration()
# 	return render_template("leaddata.html",data=data)

#  _____________________________________________________________________________________________________________________  #


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
