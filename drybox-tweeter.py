import os
import gspread
import tweepy
from dotenv import load_dotenv
import datetime
import time


load_dotenv('./.env')
gc = gspread.service_account("./creds.json")

TW_API_KEY = os.getenv('API_KEY') 
TW_API_SECRET = os.getenv('API_SECRET')
TW_ACCESS_KEY = os.getenv('ACCESS_TOKEN')
TW_ACCESS_SECRET = os.getenv('ACCESS_SECRET')
SS_KEY = os.getenv('SPREADSHEET_KEY')

auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_SECRET)
auth.set_access_token(TW_ACCESS_KEY, TW_ACCESS_SECRET)
tw_api = tweepy.API(auth=auth, wait_on_rate_limit=True)

sht = gc.open_by_key(SS_KEY).sheet1


while True:
    last_row = sht.get_all_values()[-1]
    try:
        tw_api.verify_credentials()
        print("Authentication OK")
        # tw_api.update_status("Test")
        tw_api.update_status(f"3D Printer Filament Drybox\n\nRelative Humidity: {last_row[0]}%\nTemperature: {last_row[1]}\nLast Update: {last_row[2]}")
    except:
        print("Error during authentication")

    print("Sleeping for an hour")
    time.sleep(3600)
    