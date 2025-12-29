from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8397983079:AAHVIPRpfoK0IlLc_Wm9JCfFj9qydhUKQTc"
CHANNEL = "@yorzodablog"  # или ID канала

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text("✅ Вы подписаны! Доступ разрешён.")
        else:
            raise Exception

    except:
        keyboard = [
            [InlineKeyboardButton("📢 Подписаться", url=f"https://t.me/{CHANNEL.replace('@','')}")],
            [InlineKeyboardButton("🔄 Проверить подписку", callback_data="check")]
        ]
        await update.message.reply_text(
            "❌ Вы не подписаны на канал!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()