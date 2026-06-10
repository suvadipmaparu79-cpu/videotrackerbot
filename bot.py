import telebot
import uuid

TOKEN = "8817022006:AAEmjA3t7pXiz90_bX70bmskwcJQDQ32O7w"

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

        track_id = str(uuid.uuid4())[:8]

        tracking_link = (
            f"https://videotrackerbot.onrender.com/t/{track_id}"
        )

        bot.reply_to(
            message,
            f"Video Link:\n{video_link}\n\n"
            f"Tracking Link:\n{tracking_link}"
        )

    except:
        bot.reply_to(
            message,
            "Usage:\n/track https://example.com/video.mp4"
        )

print("Bot Started...")
bot.infinity_polling()
