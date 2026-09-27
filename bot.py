import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "Telegram bot is running!"


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Добро пожаловать в наш магазин 🛍️\n"
        "Скоро здесь появятся товары!"
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("Не найден BOT_TOKEN")

    print("Запускаю веб-сервер...")
threading.Thread(target=run_web_server, daemon=True).start()
print("Веб-сервер запущен!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
