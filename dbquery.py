# from dbconnect import *
# from MySQLdb import escape_string as thwart
import ast

# cursor,conn = connection()


def LeadInsertion(data):
    # print("########### INSERTION DATA ##############")
    # name = data['lead']['name']
    # company_name= data['lead']['company']
    # email = data['lead']['email']
    # _query = """ INSERT INTO lead_generation (name, email, company) VALUES (%s, %s,%s) """
    # args = (name, email ,company_name)
    # try:
    #     cursor.execute(_query,args)
    #     conn.commit()
    #     print("########### Data INSERTED ###############")
    # except Exception as e:
    #     #print(e)
    #     print("########### Data NOT INSERTED ###############")
    return


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


def ShowLeadGeneration():
    # cursor.execute( "SELECT * FROM `lead_generation`")
    # data = cursor.fetchall()
    # return data
    return


def InitialData(unique_id):
    # print("----------")
    # #sql = """SELECT * FROM `bot_registration` WHERE unique_id=%s""" % (unique_id)
    # # print(sql)
    # # cursor.execute(sql)
    # # print("+++++++++++++")
    # # records = cursor.fetchall()
    # _query = cursor.execute("SELECT * FROM bot_registration WHERE unique_id= (%s)",[(thwart(unique_id))])
    # records = cursor.fetchall()
    # for row in records:
    #     company_name = row[1]
    #     bot_name = row[2]
    # # company_name = "Forethought"
    # # bot_name = "Eela"
    # # #welcome_msg = "Welcome to Forethought"
    # _query = cursor.execute("SELECT * FROM init_data WHERE unique_id = (%s)",[(thwart(unique_id))])
    # #cursor.execute("SELECT * FROM init_data LIMIT 1 WHERE `unique_id` = %s",unique_id)
    # print("number",int(_query))
    # init_message = cursor.fetchall()
    # print("-->",init_message)
    # for row in init_message:
    #     bot_image = row[1]
    #     welcome_msg = row[2]
    # print(bot_name,bot_image)
    # print(type(bot_name))
    # count = count_dialogues(unique_id)
    # print("count ",count)
    bot_name = "Eela"
    bot_image = "img.jpeg"
    company_name = "Foethought"
    welcome_msg = "Welcome to Forethought!"
    count = 6
    return bot_name,bot_image,company_name,welcome_msg,count

def FinalMessage(unique_id):
    # _query = cursor.execute("SELECT * FROM final_data WHERE unique_id = (%s)",[(thwart(unique_id))])
    # records = cursor.fetchall()
    # for row in records:
    #     msg = row[2]
    #     fb = row[3]
    #     ln = row[4]
    #     tw = row[5]
    #     insta = row[6]
    #
    # return msg,fb,ln,tw,insta
    return


def count_dialogues(unique_id):
    # _query = cursor.execute("SELECT * FROM dialogues")
    # count = int(_query)
    # return count
    return

def Dialogue(unique_id,count):
    # cursor.execute("SELECT * FROM dialogues WHERE id = (%s) ",[count])
    # records = cursor.fetchall()
    # #print (data)
    # for row in records:
    #     ques = row[1]
    #     option = convert_to_list(row[2])
    #     response = row[3]
    #     value = row[4]
    # print(option)
    # return ques,option,response,value
    return
