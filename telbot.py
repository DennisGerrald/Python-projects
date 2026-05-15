from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

updater = None  # not used in new version

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Enter the text you want to show the user when they start bot"
    )

# Help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Your message")

# Additional commands
async def gmail_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("gmail link here")

async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Youtube link here")

async def linkedin_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("linkedin url here")

# Unknown text
async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry I cant recognise what you said '%s'" % update.message.text
    )

# Unknown command
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text
    )

# Build app
app = ApplicationBuilder().token("BOT_TOKEN HERE").build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("youtube", youtube_url))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("linkedin", linkedin_url))
app.add_handler(CommandHandler("gmail", gmail_url))

app.add_handler(MessageHandler(filters.COMMAND, unknown))
app.add_handler(MessageHandler(filters.TEXT, unknown_text))

# Run bot
app.run_polling()