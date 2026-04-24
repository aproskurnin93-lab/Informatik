import qrcode
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
import telebot
from telebot.types import InputFile
import io
import threading
T = '8298863267:AAHDX8Av4iu9Zp33yL0S_jctpHD-4es6Yhc'
bot = telebot.TeleBot(T)
def create_rounded_qr(qr_img,corner_radius=6):
    width, height = qr_img.size
    box_size = 18
    border = 3
    module_count = qr_img.size[0] // box_size
    module_size = qr_img.size[0] // module_count
    new_img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(new_img)
    for x in range(0, width, module_size):
        for y in range(0, height, module_size):
            if x + module_size <= width and y + module_size <= height:
                sample_x = x + module_size // 2
                sample_y = y + module_size // 2
                pixel = qr_img.getpixel((sample_x, sample_y))     
                if isinstance(pixel, tuple):
                    if pixel[0] < 128 or pixel[1] < 128 or pixel[2] < 128:
                        draw.rounded_rectangle([x, y, x + module_size, y + module_size],radius=corner_radius,fill=pixel)
                else:
                    if pixel < 128:
                        draw.rounded_rectangle([x, y, x + module_size, y + module_size],radius=corner_radius,fill=(0, 0, 0)) 
    return new_img

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message, "Привет! Отправь мне текст для QR-кода, и я создам его для тебя.")
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text
    
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    btn1 = telebot.types.InlineKeyboardButton("1-красный", callback_data=f"1|{text}")
    btn2 = telebot.types.InlineKeyboardButton("2-синий", callback_data=f"2|{text}")
    btn3 = telebot.types.InlineKeyboardButton("3-зеленый", callback_data=f"3|{text}")
    btn4 = telebot.types.InlineKeyboardButton("4-желтый", callback_data=f"4|{text}")
    btn5 = telebot.types.InlineKeyboardButton("5-фиолетовый", callback_data=f"5|{text}")
    btn6 = telebot.types.InlineKeyboardButton("6-оранжевый", callback_data=f"6|{text}")
    btn7 = telebot.types.InlineKeyboardButton("7-черный", callback_data=f"7|{text}")
    btn8 = telebot.types.InlineKeyboardButton("8-розовый", callback_data=f"8|{text}")
    btn9 = telebot.types.InlineKeyboardButton("9-ГОЛ1 (градиент)", callback_data=f"9|{text}")
    btn10 = telebot.types.InlineKeyboardButton("10-ГОЛ2 (градиент)", callback_data=f"10|{text}")
    btn11 = telebot.types.InlineKeyboardButton("11-ГОЛ3 (градиент)", callback_data=f"11|{text}")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    
    bot.reply_to(message, "Выберите цвет:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_color(call):
    data = call.data.split("|")
    col = data[0]
    text = data[1]
    
    bot.answer_callback_query(call.id, "...")
    
    qr = qrcode.QRCode(box_size=18, border=3)
    qr.add_data(text)
    qr.make(fit=True)
    
    if col == "9":
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        w, h = img.size
        red = (255, 0, 0)
        yel = (255, 255, 0)
        blue = (0, 0, 255)
        for x in range(w):
            for y in range(h):
                if img.getpixel((x, y)) == (0, 0, 0):
                    pos = (x/w + y/h) / 2
                    if pos < 0.5:
                        p = pos * 2
                        r = int(red[0]*(1-p) + yel[0]*p)
                        g = int(red[1]*(1-p) + yel[1]*p)
                        b = int(red[2]*(1-p) + yel[2]*p)
                    else:
                        p = (pos - 0.5) * 2
                        r = int(yel[0]*(1-p) + blue[0]*p)
                        g = int(yel[1]*(1-p) + blue[1]*p)
                        b = int(yel[2]*(1-p) + blue[2]*p)
                    img.putpixel((x, y), (r, g, b))
        img = create_rounded_qr(img, 6)
        color_name = "ГОЛ1"
    elif col == "10":
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        w, h = img.size
        red = (255, 0, 0)
        yel = (255, 255, 0)
        blue = (0, 0, 255)
        for x in range(w):
            for y in range(h):
                if img.getpixel((x, y)) == (0, 0, 0):
                    pos = (x/w + y/h) / 2
                    if pos < 0.5:
                        p = pos * 2
                        r = int(red[0]*(1-p) + yel[0]*p)
                        g = int(red[1]*(1-p) + yel[1]*p)
                        b = int(red[2]*(1-p) + yel[2]*p)
                    else:
                        p = (pos - 0.5) * 2
                        r = int(yel[0]*(1-p) + blue[0]*p)
                        g = int(yel[1]*(1-p) + blue[1]*p)
                        b = int(yel[2]*(1-p) + blue[2]*p)
                    img.putpixel((x, y), (b, r, g))
        img = create_rounded_qr(img, 6)
        color_name = "ГОЛ2"
    elif col == "11":
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        w, h = img.size
        red = (255, 0, 0)
        yel = (255, 255, 0)
        blue = (0, 0, 255)
        
        for x in range(w):
            for y in range(h):
                if img.getpixel((x, y)) == (0, 0, 0):
                    pos = (x/w + y/h) / 2
                    if pos < 0.5:
                        p = pos * 2
                        r = int(red[0]*(1-p) + yel[0]*p)
                        g = int(red[1]*(1-p) + yel[1]*p)
                        b = int(red[2]*(1-p) + yel[2]*p)
                    else:
                        p = (pos - 0.5) * 2
                        r = int(yel[0]*(1-p) + blue[0]*p)
                        g = int(yel[1]*(1-p) + blue[1]*p)
                        b = int(yel[2]*(1-p) + blue[2]*p)
                    img.putpixel((x, y), (g, b, r))
        img = create_rounded_qr(img, 6)
        color_name = "ГОЛ3"
    else:
        colors = {"1":"red", "2":"blue", "3":"green", "4":"yellow", 
                  "5":"purple", "6":"orange", "7":"black", "8":"pink"}
        color = colors.get(col, "black")
        img = qr.make_image(fill_color=color, back_color="white")
        img = create_rounded_qr(img.convert('RGB'), 6)
        color_name = color
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    bot.send_photo(call.message.chat.id, InputFile(img_buffer, filename='qrcode.png'), caption=f"Текст: {text}\nЦвет: {color_name}")

def run_bot():
    bot.infinity_polling()
if __name__ == "__main__":
    print("Бот запущен")
    run_bot()
