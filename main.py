from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bs4 import BeautifulSoup
import requests


redditLink='https://www.reddit.com/r/GameDeals/new/'

headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'content-length': '2903'
}


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=""
    )


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1181226483:AAEsRfQ-kWk400lnzgsV52DhIvD3nFzwOaE", use_context=True)

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

    titlesFromReddit = soup.findAll("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
    print(len(titlesFromReddit))
    for title in titlesFromReddit:
        if "FREE" in title.text.upper():
            print(title.text)

GetRedditInfo()
#main()