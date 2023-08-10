from flask import Flask

from skpy import SkypeEventLoop, SkypeNewMessageEvent
import schedule
import time
import datetime

app = Flask(__name__)

class SkypeHomeworkBot(SkypeEventLoop):
    def __init__(self, user, password, reporting_group_id, main_group_id, time):
        super(SkypeHomeworkBot, self).__init__(user, password)
        self.reporting_group_id = reporting_group_id
        self.main_group_id = main_group_id
        self.time = time
        group_chat = self.chats[reporting_group_id]
        group_chat.sendMsg("Scheduled to send 'Good morning' message every working day at " + time + " AM.")
        self.schedule_good_morning()

    def send_good_morning(self):
        if datetime.datetime.today().weekday() < 5:
            group_chat = self.chats[self.main_group_id]
            group_chat.sendMsg("おはようございます。")
            group_chat2 = self.chats[self.reporting_group_id]
            group_chat2.sendMsg("Good morning message sent to main group.")

    def schedule_good_morning(self):
        schedule.every().day.at(self.time).do(self.send_good_morning)

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

@app.route('/')
def home():
    return "Skype Homework Bot is running!"

if __name__ == '__main__':
    user = "murad@linkstaff.co.jp"  # Skype user
    password = "LINKregiM1@"  # Password skype
    REPORTING_GROUP_ID = "19:c378e6799eb041e796fa1c2373dadc5d@thread.skype"  # Reporting group id
    MAIN_GROUP_ID = "19:c378e6799eb041e796fa1c2373dadc5d@thread.skype"  # Main group id
    TIME = "01:23"

    sk = SkypeHomeworkBot(user, password, REPORTING_GROUP_ID, MAIN_GROUP_ID, TIME)
    sk.run_schedule()
    app.run(debug=True)
