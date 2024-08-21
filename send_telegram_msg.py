import requests



############## Bot Creditials ###############
# bot_id='6581965254:AAGc5AKyq_lL61sHtG8qOzWBcLyde2_RlJo'
bot_id='7164367063:AAGKfhLQrpd5YzbjcIeB1s71HPgAC5op3Mk'
group_chat_id='argusGanecos'


######################  #######################



def sending_Telegram_Message(message:str,bot_id:str=bot_id,group_chat_id:str=group_chat_id):
    try:
        url=f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id=@{group_chat_id}&text={message}'
        print(url)
        url_status=requests.get(url)
        print(url_status)
        print(url_status.json())
        return url_status.json().get('ok')
    except Exception as E:
        print(E)
        return False



if __name__ == '__main__':

    status=sending_Telegram_Message('`{Count_person} person found in front of feeder_machine`',bot_id=bot_id,group_chat_id=group_chat_id)
    print("its Status",status)