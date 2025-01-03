from yophonebot.bot import YoPhoneBot


bot = YoPhoneBot("YOUR_API_KEY")

@bot.command_handler("/start")
def start_command(message):
    bot.send_message(message.chat_id, f"Welcome, {message.sender.first_name}! This is the YoPhone Bot.")

@bot.command_handler("/help")
def help_command(message):
    bot.send_message(message.chat_id, "Available commands:\n/start - Start the bot\n/help - Show help information")

@bot.message_handler
def echo_bot(message):
    bot.send_message(message.chat_id, message.text)


# Start polling
if __name__ == "__main__":
    bot.start_polling()
