from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bs4 import BeautifulSoup
import requests
import schedule
import threading
import time
import telegram
Token=""

redditLink='https://www.reddit.com/r/GameDeals/new/'

headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def run_threaded(job_function):  # run every schedule on different threads
    job_thread = threading.Thread(target=job_function)
    job_thread.start()

def run_schedules_on_bg_thread(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    print(update.effective_chat.id)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=""
    )

def SendTitlesToIonut():
    bot = telegram.Bot(token=Token)



    bot.sendMessage(
        chat_id=757202598,
        text="da"
    )
SendTitlesToIonut()
def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(Token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def GetRedditInfo():
    resp = requests.get(redditLink, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    response = []

    titlesFromReddit = soup.findAll("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
    print(len(titlesFromReddit))
    for title in titlesFromReddit:
        if "FREE" in title.text.upper():
            # response

schedule.every().hour.do(run_threaded, SendTitlesToIonut())

# run_schedules_on_bg_thread()
main()