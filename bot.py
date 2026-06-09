import telebot

TOKEN = "8817022006:AAEgE97JIa6glzU_g7dWsP6Gdo-N6omjYLE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Send:\n/track https://example.com/video.mp4"
    )

@bot.message_handler(commands=['track'])
def track(message):
    try:
        video_link = message.text.split(" ", 1)[1]

        tracking_link = (
            "https://videotrackerbot.onrender.com/t/123"
        )

        bot.reply_to(
            message,
            f"Video Link:\n{video_link}\n\nTracking Link:\n{tracking_link}"
        )

    except:
        bot.reply_to(
            message,
            "Usage:\n/track https://example.com/video.mp4"
        )

print("Bot Started...")
bot.infinity_polling()
