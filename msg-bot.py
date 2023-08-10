from skpy import SkypeEventLoop, SkypeNewMessageEvent
import re
import schedule
import time
import datetime

# varabile
user = "murad@linkstaff.co.jp"  # Skype user
password = "LINKregiM1@"  # Password skype
REPORTING_GROUP_ID = "19:c378e6799eb041e796fa1c2373dadc5d@thread.skype" # Reporting group id
# MAIN_GROUP_ID = "19:0404d69a274f4de1bc5c88396086f95a@thread.skype" # Main group id
MAIN_GROUP_ID = "19:c378e6799eb041e796fa1c2373dadc5d@thread.skype" # Main group id
TIME = "01:10"

# Skype Events
class SkypeHomeworkBot(SkypeEventLoop):
    def __init__(self):
        super(SkypeHomeworkBot, self).__init__(user, password)
        group_chat = self.chats[REPORTING_GROUP_ID]
        group_chat.sendMsg("Scheduled to send 'Good morning' message every working day at "+ TIME +" AM.")
        self.schedule_good_morning()


    def send_good_morning(self):
        if datetime.datetime.today().weekday() < 5:
            group_chat = self.chats[MAIN_GROUP_ID]
            group_chat.sendMsg("おはようございます。")
            group_chat2 = self.chats[REPORTING_GROUP_ID]
            group_chat2.sendMsg("Good morning message sent to main group.")

    def schedule_good_morning(self):
        schedule.every().day.at(TIME).do(self.send_good_morning)

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


sk = SkypeHomeworkBot()
sk.run_schedule()