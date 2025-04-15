from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# Token del bot
TOKEN = '7768926356:AAEPYmvSQugnRAvX36lFrv__bQX_b5zS8Zc'

# Lista de IDs permitidos
USUARIOS_PERMITIDOS = [
    1066302759, 5542122484, 7300876085, 7311864062,
    6635811497, 5024400656, 6350743838, 1231763111, 1963522615, 1996246512, 1166066370, 5986305450
]

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in USUARIOS_PERMITIDOS:
        await update.message.reply_text(
            "✅ ¡Bienvenido! Tienes acceso a los nuevos Tokens de Claro Chile.\n\n"
            "🔑 *Nuevo Token:* ✔️\n"
            "`UR8M+MXRXPdCihY5FSanSIRLq6C2pJOYMXXSb/0TwhBP1RevGtmqhaBjcN9IzVkFXmgRNI2Db74aCFYkjCfJxA==`",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "🚫 Solo los miembros que compraron la config tienen acceso a los nuevos tokens. Contacta a @JGrrey"
        )

# Comando /id
async def my_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"🆔 Tu ID es: {user.id}")

# Bot de Telegram
bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("id", my_id))

# Servidor web con Flask
web_app = Flask('')

@web_app.route('/')
def home():
    return "🤖 Bot activo y funcionando."

def run():
    web_app.run(host='0.0.0.0', port=8080)

# Iniciar el servidor Flask en segundo plano
Thread(target=run).start()

print("✅ Bot corriendo...")
# Iniciar el bot de Telegram
bot_app.run_polling()
