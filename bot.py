import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


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

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
