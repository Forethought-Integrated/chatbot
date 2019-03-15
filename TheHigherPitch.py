from flask import Flask,render_template,request,jsonify
from tf_idf import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test.html')

@app.route("/speech_page",methods=['POST','GET'])
def speech():
    msg = str(request.form['data'])
    bot_response = previous_chats(msg)
    return jsonify({"status":"ok","answer":bot_response})


@app.route("/ask", methods=['POST','GET'])
def ask():
	message = str(request.form['chatmessage'])
	# # if message == "save":
	# #     kernel.saveBrain("bot_brain.brn")
	# #     return jsonify({"status":"ok", "answer":"Brain Saved"})
	# # elif message == "reload":
	# # 	load_kern(True)
	# # 	return jsonify({"status":"ok", "answer":"Brain Reloaded"})
	# # elif message == "quit":
	# # 	exit()
	# # 	return jsonify({"status":"ok", "answer":"exit Thank You"})
	# #
	# # # kernel now ready for use
	# else:
		# while True:
		#bot_response = kernel.respond(message)
		# print bot_response
	bot_response = previous_chats(message)
	# try:
	# 	c,conn = connection()
	# 	# sql="""INSERT INTO messages(msg_from_user,msg_to_user) VALUES('%s')""" % message
	# 	print("below query")
	# 	c.execute("INSERT INTO messages(msg_from_user,msg_to_user) VALUES(%s,%s)",(thwart(message),thwart(bot_response)))
	# 	print("i m in try block")
	# 	conn.commit()
	# 	print("inserted")
	# 	c.close()
	# except Exception as e:
	# 	print(e)
	#print(type(message))
	#return message
	#time.sleep(1)
	#status = bool(BeautifulSoup(bot_response, "html.parser").find());
	return jsonify({'status':'OK','answer':bot_response})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port = 5000, debug = True, use_reloader = False)
    except Exception as e:
        print (e)
