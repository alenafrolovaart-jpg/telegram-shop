import os
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "Telegram bot is running!"


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✅Открыть витрину"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Добро пожаловать🫶🏼\n\n",
        reply_markup=reply_markup
    )


async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✅Открыть витрину"],
        ["🔙 Назад"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🛍 Каталог\n\n"
        "Выберите категорию:",
        reply_markup=reply_markup
    )


async def ribbons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎀 Ленты\n\n"
        "Здесь будут разные виды лент."
    )


async def beads(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📿 Бусы\n\n"
        "Здесь будут разные виды бус."
    )


async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Мои заказы\n\n"
        "Здесь будут отображаться ваши заказы."
    )


async def cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Корзина\n\n"
        "Ваша корзина пока пуста."
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Связаться с нами\n\n"
        "Напишите нам, и мы обязательно ответим!"
    )


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("Не найден BOT_TOKEN")

    print("Запускаю веб-сервер...")

    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True
    )
    web_thread.start()

    print("Веб-сервер запущен!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🛍 Каталог$"),
            catalog
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🎀 Ленты$"),
            ribbons
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📿 Бусы$"),
            beads
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📦 Мои заказы$"),
            orders
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🛒 Корзина$"),
            cart
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📞 Связаться с нами$"),
            contact
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🔙 Назад$"),
            back
        )
    )

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
