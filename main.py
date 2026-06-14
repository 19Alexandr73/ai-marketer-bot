import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8928171237:AAGvs1yBiwhTBK-YHX1pnFf4Wde7Fjxtr9U"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

WELCOME_TEXT = (
    "Привет! Я AI-маркетолог для малого бизнеса.\n\n"
    "Что я могу:\n"
    "/audit — бесплатный аудит ниши\n"
    "/post — идея для продающего поста\n"
    "/contacts — оставить заявку на стратегию\n\n"
    "Напиши /audit и опиши свой бизнес."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def audit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/audit", "").strip()
    if not text:
        await update.message.reply_text("Напишите: /audit Ваш бизнес (например, /audit кофейня в Минске)")
        return
    await update.message.reply_text(
        f"Анализирую: {text}\n\n"
        "Целевая аудитория: люди 25-40 лет, средний доход.\n"
        "Боли: нехватка времени, дорого, сложно выбрать.\n"
        "Идеи:\n"
        "1. Лид-магнит «Скидка 20% на первое посещение»\n"
        "2. Таргет на район в радиусе 2 км\n"
        "3. Партнёрство с ближайшим бизнесом\n\n"
        "Хотите полную стратегию? /contacts"
    )

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Продающий пост:\n\n"
        "«Устали тратить бюджет на рекламу?\n"
        "AI-маркетолог анализирует ваш бизнес и даёт стратегию за 5 минут.\n"
        "Бесплатный аудит — пиши в бот».\n\n"
        "Адаптируйте под свой бизнес."
    )

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Оставьте заявку:\n"
        "Имя, телефон/email, описание бизнеса.\n"
        "Я свяжусь с вами."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Используйте команды: /audit, /post, /contacts, /start")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("audit", audit))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CommandHandler("contacts", contacts))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
