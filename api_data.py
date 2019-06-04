import requests



def count_dialogues():
    URL = "http://techeela.com/chatbot/api/dialogues"
    r = requests.get(url = URL)
    print("################## Count Data  ################")
    data = r.json()
    print(type(data))
    return data


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
    count = count_dialogues()
    return bot_name,bot_image,company_name,welcome_msg,count
