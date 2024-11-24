import logging
from telegram.ext import *
from telegram import Update
import responses

API_KEY = '8069338249:AAGRHm53zWEgRgzXfWgdWv42u9ZoX_4ksmA'

#Configuracion del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Iniciando bot....')

async def start_command(update: Update, context):
    await update.message.reply_text('hola aca estamos para ayudarte dime en que y lo haremos posible')

async def help_command(update: Update, context):
    await update.message.reply_text('Escribe el problema que tengas y yo hare lo posible por resolverlo')

async def custom_command(update: Update, context):
    await update.message.reply_text('Este es un comando con el que puedes escribir, todo lo que desees.')
    
async def handle_message(update: Update, context):
    texto = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) escribe: {texto}')
    response = responses.get_response(texto)
    
    #Las respuestas del Bot
    await update.message.reply_text(response)
    
async def error(update: Update, context):
    #Los errores que estan en el log 
    logging.error(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    application = Application.builder().token(API_KEY).build()
    
    #Comandos 
    application.add_handler(CommandHandler('start',start_command))
    application.add_handler(CommandHandler('help',help_command))
    application.add_handler(CommandHandler('custom',custom_command))
    
    #Mensajes
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Todos los errores en el log
    application.add_error_handler(error)
    
    #Ejecucion del bot 
    application.run_polling(poll_interval=0.0)