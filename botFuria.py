import telebot
from dotenv import load_dotenv
import os



# === CONFIGURAÇÃO ===

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env onde esta a chave da API do BoT

CHAVE_API = os.getenv("CHAVE_API")
bot = telebot.TeleBot(CHAVE_API)

# Guarda nicknames e estados dos usuários
user_nick = {}
user_states = {}

# === COMANDOS DE INÍCIO E NICK ===

@bot.message_handler(commands=['start'])
def start(mensagem):
    user_id = mensagem.from_user.id
    bot.reply_to(mensagem, "Fala FURIOSO(A)! Digite seu nickname no CS:GO pra começar!")
    user_states[user_id] = "awaiting_nick"

@bot.message_handler(commands=['nickname'])
def mostrar_nickname(mensagem):
    user_id = mensagem.from_user.id
    nick = user_nick.get(user_id)

    if nick:
        bot.reply_to(mensagem, f"🎯 Seu nickname registrado é: {nick}")
    else:
        bot.reply_to(mensagem, "😕 Você ainda não cadastrou seu nickname! Use /start pra fazer isso.")

@bot.message_handler(commands=['info'])
def info_criador(mensagem):
    user_id = mensagem.from_user.id
    nick = user_nick.get(user_id)

    if nick:
        resposta = (f"🎮 Nickname cadastrado: {nick}\n\n"
                    "Bot da FURIA criado por: @tiagosts99\n"
                    "Linkedin: https://www.linkedin.com/in/tiagosts99/\n"
                    "GitHub: https://github.com/tiagosts99\n"
                    "Instagram: https://www.instagram.com/tiagosts99/\n"
                    "🔥 #GOFURIA")
    else:
        resposta = "Você ainda não cadastrou seu nickname! Digite /start para começar."

    bot.reply_to(mensagem, resposta)

# === COMANDOS SOBRE A FURIA ===

@bot.message_handler(commands=['time'])
def info_time(mensagem):
    resposta = ("🔥 Time atual da FURIA (CS:GO):\n"
                "- KSCERATO\n- yuurih\n- arT\n- chelo\n- FalleN👑\n\n"
                "🖤 Bora apoiar nossos guerreiros!")
    bot.reply_to(mensagem, resposta)

@bot.message_handler(commands=['logo'])
def enviar_logo(mensagem):
    logo_url = "https://pt.wikipedia.org/wiki/Ficheiro:Furia_Esports_logo.png"
    bot.send_photo(mensagem.chat.id, logo_url, caption="🖤 Logo oficial da FURIA pra você, FURIOSO(A)!")

@bot.message_handler(commands=['redesocial'])
def redes_sociais(mensagem):
    resposta = ("🔥 Redes sociais da FURIA:\n\n"
                "Twitter: https://twitter.com/FURIA\n"
                "Instagram: https://www.instagram.com/furia/\n"
                "Facebook: https://www.facebook.com/FURIAesports/\n"
                "YouTube: https://www.youtube.com/c/FURIA\n"
                "Twitch: https://www.twitch.tv/furia\n\n"
                "🖤 Poste sua foto com a camisa mais FURIOSA e marque a FURIA nas redes Sociais!")
    bot.reply_to(mensagem, resposta)

@bot.message_handler(commands=['ultimosjogos'])
def ultimos_jogos(mensagem):
    resposta = ("🔥 Últimos jogos da FURIA:\n\n"
                "🏆 FURIA 2 x 0 MIBR\n"
                "🏆 FURIA 1 x 2 NAVI\n"
                "🏆 FURIA 2 x 1 Liquid\n"
                "🏆 FURIA 0 x 2 G2\n\n"
                "🛡️ Próximo objetivo: dominar tudo! 🚀")
    bot.reply_to(mensagem, resposta)

@bot.message_handler(commands=['proximosjogos'])
def proximos_jogos(mensagem):
    resposta = ("🔥 Próximos jogos da FURIA:\n\n"
                "🏆 FURIA vs MIBR\n"
                "🏆 FURIA vs NAVI\n"
                "🏆 FURIA vs Liquid\n"
                "🏆 FURIA vs G2\n\n"
                "🛡️ Bora apoiar a tropa! 🚀")
    bot.reply_to(mensagem, resposta)

@bot.message_handler(commands=['grito'])
def grito(mensagem):
    resposta = ("🔥 FURIOSO(A)!\n\n"
                "🛡️ NÃO TEM TEMOR!\n"
                "NÃO TEM RENDIÇÃO!\n"
                "SOMOS FÚRIA, SOMOS CAMPEÕES! 🔥🐆\n"
                "#GOFURIA\n\n"
                "🖤 Solta teu grito nas redes também com a Camisa mais FURIOSA!")
    # Enviar a resposta do comando
    bot.reply_to(mensagem, resposta)


# === MENSAGENS NÃO COMANDADAS ===

@bot.message_handler(func=lambda m: True)
def mensagens_gerais(mensagem):
    user_id = mensagem.from_user.id
    texto = mensagem.text

    if user_states.get(user_id) == "awaiting_nick":
        user_nick[user_id] = texto
        user_states[user_id] = "registered"

        bot.reply_to(mensagem, f"🔥 Nickname '{texto}' salvo com sucesso!")        
        bot.send_message(user_id, """🖤 Seja bem-vindo(a) à tropa da FURIA!\n\n
         "Use os comandos para explorar:
         1️⃣ Ver informações do time com /time
         2️⃣ Mostrar seu nickname com /nickname
         3️⃣ Encontrar as redes Sociais da Furia! /redesocial
         4️⃣ Receber a logo da FURIA /logo
         5️⃣ Ver os últimos resultados com /ultimosjogos
         6️⃣ Ver os próximos jogos com /proximosjogos
         7️⃣ Solta o grito dos FURIOSOS! /grito
         8️⃣ Ver informações do criador do bot com /info\n\n""")
    else:
        bot.reply_to(mensagem, "Fala FURIOSO(A)! Use /start para começar!")

# === EXECUTA O BOT ===
bot.polling()
