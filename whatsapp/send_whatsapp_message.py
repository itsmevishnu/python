import webbrowser as web
import time
from urllib.parse import quote
import requests
from pyautogui import click, hotkey, press, size
import pyperclip

WIDTH, HEIGHT = size()

class SendWhatsappMessage:
    
    def __init__(self, receiver: str) -> None:
        """Opens WhatsApp Web based on the Receiver"""
        try:
            web.open("https://web.whatsapp.com/accept?code=" + receiver)
        except Exception as error:
            print(f"Some error has occurred {error}")
            exit(0)


    def send_messages(self, messages: str) -> None:
        """Parses and Sends the Message"""
        time.sleep(10)
        click(WIDTH / 2 + 50, HEIGHT / 2 + 50)
        
        for message in messages:
            pyperclip.copy(message)
            hotkey("ctrl", "v")
            press("enter")

        time.sleep(10)
    
    @staticmethod
    def close_window():
        hotkey("ctrl", "w")