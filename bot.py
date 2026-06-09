import telebot

TOKEN = "8817022006:AAHtPydGRB3Df_z-NQ0iwQmfGtTSKKtLVII"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is working!")

print("Bot Started...")
bot.infinity_polling()
