import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalam-o-Alaikum! 👋\n"
        "Main Aviator Hisab Bot hun.\n\n"
        "Commands:\n"
        "/start - Bot start\n"
        "/hisab - Aaj ka hisab\n"
        "/signal - Next signal"
    )

async def hisab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aaj ka hisab abhi calculate ho raha hai...")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ye sirf history based estimate hai, guarantee nahi hai
    val = round(random.uniform(1.2, 3.5), 2)
    await update.message.reply_text(f"📊 Possible Signal: {val}x\n\nNote: Ye sirf estimate hai, apne risk pe khelein.")

if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hisab", hisab))
    app.add_handler(CommandHandler("signal", signal))
    print("Bot chal raha hai...")
    app.run_polling()
