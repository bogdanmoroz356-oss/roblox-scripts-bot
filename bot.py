import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    print("ОШИБКА: Токен не найден!")
    exit()

bot = telebot.TeleBot(TOKEN)

scripts = {
    "blox fruits":
    """
**Blox Fruits скрипты:**

**Zynex Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/Hirokai-Script-make/Zynexhubbloxfruit/refs/heads/main/ZynexHub-BloxFruit-redz.lua"))()

**NHT Hub** `getgenv().Team = "Pirates" 

loadstring(game:HttpGet("https://raw.githubusercontent.com/trongdeptraihucscript/Main/refs/heads/main/Hoangtrongdepzai.lua"))()

**Zeus Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/Jadelly/bloxfruit/refs/heads/main/Zeusscript", true))()

**REDZ Hub ⛩** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/Omgshit/Scripts/main/MainLoader.lua"))()

**Speed Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/AhmadV99/Speed-Hub-X/main/Speed%20Hub%20X.lua", true))()

**Rat Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/Ratkinator/RatX/refs/heads/main/Loader.lua",true))()

**Rift Hub** 

loadstring(game:HttpGet("https://rifton.top/loader.lua"))()

**OsakaTP2V1** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/b8141444-ship-it/lua/main/LuaRBX"))()

**Vxeze Hub** 

loadstring(game:HttpGet("https://pandadevelopment.net/virtual/file/702a5c5488082e6f"))()

**Pepehook Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/GiftStein1/pepehook-loader/refs/heads/main/loader.lua"))()

**Carsonn Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/zenwhatudoing-crypto/CarsonnHub/refs/heads/main/Carsonn%20Hub.lua"))()

**Haze Hub** 

loadstring(game:HttpGet("https://haze.wtf/api/script"))()

**Chiyo Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/kaisenlmao/loader/refs/heads/main/chiyo.lua"))()

**VulnX Hub** 


loadstring(game:HttpGet("https://raw.githubusercontent.com/Yumiara/SSL-VulnX/refs/heads/main/APIs/M.lua"))();

**No Key (тел/ПК):** 

1. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/WhiteX1208/Scripts/refs/heads/main/BF-Beta.lua"))()

2.

loadstring(game:HttpGet("https://raw.githubusercontent.com/Dev-BlueX/BlueX-Hub/refs/heads/main/Main.lua"))()

3. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/REDzHUB/BloxFruits/main/redz9999"))()

4. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/flazhy/QuantumOnyx/refs/heads/main/QuantumOnyx.lua"))()

5. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/JonnyCheeser/bloxfruits/main/minhubv4"))()

6. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/acsu123/HOHO_H/main/Loading_UI"))()

7. 

loadstring(game:HttpGet("https://pastebin.com/raw/AHg2NLqG"))()

8. 

loadstring(game:HttpGet("https://raw.githubusercontent.com/xDepressionx/Free-Script/main/BloxFruit.lua"))()

9. 

loadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/d82a88737d4c79e00995ca9384bd098e.lua"))()

10.

loadstring(game:HttpGet("https://raw.githubusercontent.com/samuraa1/Solara-Hub/refs/heads/main/Solara Hub.lua"))()

11.

loadstring(game:HttpGet("https://pastebin.com/raw/p7Wiyps2"))()

""",
    "bee swarm sim":
    """
**Bee Swarm Simulator скрипты:**
**Beecon Hub**

loadstring(game:HttpGet("https://raw.githubusercontent.com/BaconBossScript/BeeconHub/main/BeeconHub"))()

**MacroV4**

`loadstring(game:HttpGet("https://scripts.macrov4.com/macrov4.lua"))()`
**Histy Hub** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/scriptpastebin/raw/main/Histy"))()

**Kron Hub** 

loadstring(game:HttpGet('https://raw.githubusercontent.com/DevKron/Kron_Hub/refs/heads/main/version_1.0'))("")

""",
    "ninja legends":
    """
**Ninja Legends скрипты:**
**AppleScript001** 

loadstring(game:HttpGet(("https://raw.githubusercontent.com/AppleScript001/Ninjas_Legends/main/README.md"),true))()

""",
    "фембой обби":
    """
**Фембой Обби скрипты:**
**VYLERA HUB** 

loadstring(game:HttpGet("https://raw.githubusercontent.com/vylerascripts/vylera-scripts/main/animefemboyobby.lua"))()

""",
    "99 ночей в лесу":
    """
**99 Ночей в Лесу:**

1. FARM CRYSTAL

loadstring(game:HttpGet("https://pastebin.com/raw/LPbPPNpC"))()

2. God Mode

loadstring(game:HttpGet("https://pastebin.com/raw/husyDTrd"))()

3. 99 Nights

loadstring(game:HttpGet("https://raw.githubusercontent.com/raygull3d/99-Nights-in-the-Forest-Script/refs/heads/main/99 Days Scirpt By Raygull.lua"))()

4. Voidware

loadstring(game:HttpGet("https://raw.githubusercontent.com/VapeVoidware/VWExtra/main/NightsInTheForest.lua", true))()

5. Фул 

loadstring(game:HttpGet("https://pastebin.com/raw/GreLQtfN"))()

6. Fast Hub

loadstring(game:HttpGet("https://raw.githubusercontent.com/adibhub1/99-nighit-in-forest/refs/heads/main/99 night in forest"))()

7. AXS HUB

loadstring(game:HttpGet("https://raw.githubusercontent.com/AXS-Main/AXS-Script/refs/heads/main/AXS-HUB/Main/Loader"))()

8. XVCHub 

loadstring(game:HttpGet("https://raw.githubusercontent.com/XVCHub/Games/main/99NightsintheForest"))()

9. FoxName 

loadstring(game:HttpGet("https://raw.githubusercontent.com/caomod2077/Script/refs/heads/main/FoxnameHub.lua"))()
"""
}


def get_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("Blox Fruits"))
    markup.add(KeyboardButton("Bee Swarm Sim"))
    markup.add(KeyboardButton("Ninja Legends"))
    markup.add(KeyboardButton("Фембой Обби"))
    markup.add(KeyboardButton("99 Ночей в Лесу"))
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот со скриптами для Roblox.\nВыбери игру или напиши название:",
        reply_markup=get_main_keyboard())


@bot.message_handler(func=lambda m: True)
def handle_message(message):
    text = message.text.lower().strip()
    normalized = text.replace(" ", "").replace("-", "").replace("_", "")

    for key in scripts:
        norm_key = key.replace(" ", "").replace("-", "").replace("_", "")
        if norm_key in normalized or normalized in norm_key:
            escaped = scripts[key].replace('\\', '\\\\').replace('_', '\\_').replace('*', '\\*') \
                .replace('[', '\\[').replace(']', '\\]').replace('(', '\\(').replace(')', '\\)') \
                .replace('~', '\\~').replace('`', '\\`').replace('>', '\\>').replace('#', '\\#') \
                .replace('+', '\\+').replace('-', '\\-').replace('=', '\\=').replace('|', '\\|') \
                .replace('{', '\\{').replace('}', '\\}').replace('.', '\\.').replace('!', '\\!')
            bot.reply_to(message,
                         escaped,
                         parse_mode='MarkdownV2',
                         disable_web_page_preview=True)
            return

    if "blox" in normalized or "fruits" in normalized or "блокс" in normalized or "фрукты" in normalized:
        key = "blox fruits"
    elif "bee" in normalized or "swarm" in normalized or "пчела" in normalized or "сим" in normalized:
        key = "bee swarm sim"
    elif "ninja" in normalized:
        key = "ninja legends"
    elif "фем" in normalized or "femboy" in normalized or "обби" in normalized:
        key = "фембой обби"
    elif "99" in normalized or "ноч" in normalized or "лес" in normalized:
        key = "99 ночей в лесу"
    else:
        bot.reply_to(message, "Не нашёл 😔\nПопробуй кнопки или название")
        return

    escaped = scripts[key].replace('\\', '\\\\').replace('_', '\\_').replace('*', '\\*') \
        .replace('[', '\\[').replace(']', '\\]').replace('(', '\\(').replace(')', '\\)') \
        .replace('~', '\\~').replace('`', '\\`').replace('>', '\\>').replace('#', '\\#') \
        .replace('+', '\\+').replace('-', '\\-').replace('=', '\\=').replace('|', '\\|') \
        .replace('{', '\\{').replace('}', '\\}').replace('.', '\\.').replace('!', '\\!')
    bot.reply_to(message,
                 escaped,
                 parse_mode='MarkdownV2',
                 disable_web_page_preview=True)


print("Бот запущен...")
bot.infinity_polling()
