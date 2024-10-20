# from pywhatkit.core import core, exceptions, log
import time
from tqdm import tqdm
import os
from dotenv import load_dotenv
from send_whatsapp_message import SendWhatsappMessage

load_dotenv()

WAIT_TIME = 10

def send_messages(group_id: str, messages: list) -> None:
    send_whatsapp_message = SendWhatsappMessage(receiver=group_id)
    send_whatsapp_message.send_messages(messages=messages)
    # close_window()


def read_messages_from_file(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        
        if not content:
            raise ValueError("No message to send!")
        
        messages = [message.strip() for message in content.split("---")]
        return messages

def main() -> None:
    group_id_string = os.getenv("GROUP_IDS", "")
    group_ids = group_id_string.split(",") if group_id_string else None

    
    if group_ids is None:
        print("There is no group id found!")
        return
    

    try:
        messages = read_messages_from_file("offers.txt")
    except Exception as error:
        print(str(error))
        return


    with tqdm(total=len(messages) * len(group_ids)) as progress:
        for group_id in group_ids:
            progress.update(1)
            send_messages(group_id=group_id, messages=messages)

if __name__ == "__main__":
    main()
   
