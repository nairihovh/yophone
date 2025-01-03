from yohealthbot.bot import YoHealthBot

bot = YoHealthBot("your-api-key")

# Send a message
bot.send_message(chat_id=12345, text="Hello from YoHealthBot!")

# Get updates
updates = bot.get_updates()
print(updates)

