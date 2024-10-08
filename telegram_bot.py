from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update: Update, context):
    await update.message.reply_text('Chào bạn tôi có thể giúp gì cho bạn?')
    
async def rebates(update: Update, context):
    await update.message.reply_text('Chiết khấu của bạn là 95%')



async def handle_message(update: Update, context):
    await update.message.reply_text(f'Bạn vừa nói: {update.message.text}')

if __name__ == '__main__':
    TOKEN = '7234732592:AAFZ8X0cogaaXU8VmFlGxHvjJeyLFt-k_Gg'
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('rebates', rebates))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    application.run_polling()
