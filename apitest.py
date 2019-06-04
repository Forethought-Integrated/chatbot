import requests

def convert_to_list(string):
    length = len(string)
    print(string)
    #temp = str(string)
    option = []
    print(type(string))
    try:
        string.index('null')
        return option
    except Exception as e:
        option = string[1:(length-1)]
        option = ast.literal_eval(option)
        return option


# def bot_registration():
#     URL = "http://techeela.com/chatbot/api/bot"
#     #r = requests.get(url = URL)
#     data = (requests.get(url = URL)).json()[0]
#     print(data)
#     return

def InitialData(unique_id):
    print("################## InitialData  ################")
    unique_id = "4dcd94a0-8206-11e9-b9b2-e1fe73766166"
    URL = "http://techeela.com/chatbot/api/bot/"  + unique_id
    #r = requests.get(url = URL)
    bot_data = (requests.get(url = URL)).json()
    company_name = bot_data['company_name']
    bot_name = bot_data['bot_name']

    URL ="http://techeela.com/chatbot/api/inits-all/"+unique_id
    data = (requests.get(url = URL)).json()[0]
    bot_image = data['image']
    welcome_msg = data['welcome_msg']
    #data = r[0]
    print("###############################################")
    print(company_name,bot_name,bot_image,welcome_msg)
    return

def final_data():
    URL = " "
    r = requests.get(url = URL)
    data = r.json()
    print("################## Final Data  ################")
    print(data)
    return

def count_dialogues():
    URL = "http://techeela.com/chatbot/api/dialogues"
    r = requests.get(url = URL)
    print("################## Count Data  ################")
    data = r.json()
    print(type(data))
    return

def Dialogues():
    print("################## Dialogues  ################")
    URL = "http://techeela.com/chatbot/api/dialogues/1"
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    return

def default():
    return "Incorrect Number"
#
# switcher = {
#     1: bot_registration,
#     2: init_data,
#     3: final_data,
#     4: count_dialogues,
#     5: Dialogues
#     }
#
# def switch(case):
#     return switcher.get(case, default)()
#
# while True:
#     a = input("Enter testing number: ")
#     switcher(a)

#bot_registration()
InitialData(1)
# count_dialogues()
# Dialogues()
