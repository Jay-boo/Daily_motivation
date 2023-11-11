import notify2
import logging
import requests
import configparser
from dotenv import load_dotenv
import os
from typing import Any

load_dotenv()
API_KEY=os.getenv('API_KEY')



def get_citation(category:str) ->Any |list[dict[str,str]]:
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})
    if response.status_code == requests.codes.ok:
        logging.info(f"Success {api_url} - {response.status_code} - {response.text}")
        mydict=response.json()[0]
    else:
        logging.info(f"Error {api_url} - {response.status_code} - {response.text}")
        mydict={"quote":"","author":"","category":""}

    return mydict


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    notify2.init("")
    parser=configparser.ConfigParser()
    parser.read("config-api.ini")
    citation=get_citation(parser["api-call"].get("category"))

    HOME=os.getenv("HOME")
    notification = notify2.Notification(
        summary="Daily 📚",
        message=f"{citation['quote']}\n from {citation['author']} ",
        icon=f"{HOME}/projects/daily_motiv/ressources/senssy_lee.png"
    )
    notification.show()

