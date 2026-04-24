import qrcode
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
import telebot
import urllib.request
import io

print('круглый QR?')
print('да(1)')
print('нет(2)')
j = str(input(''))
def create_rounded_qr(qr_img, corner_radius=6):
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
                        draw.rounded_rectangle([x, y, x + module_size, y + module_size], radius=corner_radius, fill=pixel)
                else:
                    if pixel < 128:
                        draw.rounded_rectangle([x, y, x + module_size, y + module_size], radius=corner_radius, fill=(0, 0, 0)) 
    return new_img

def add_logo(qr_img, logo_type):
    try:
        logos = {"telegram": "https://cdn-icons-png.flaticon.com/512/2111/2111646.png",
            "youtube": "https://cdn-icons-png.flaticon.com/512/1384/1384060.png",
            "vk": "https://cdn-icons-png.flaticon.com/512/145/145813.png",
            "yandex": "https://cdn-icons-png.flaticon.com/512/5968/5968859.png",
            "tiktok": "https://cdn-icons-png.flaticon.com/512/3046/3046126.png",
            "rutube": "https://cdn-icons-png.flaticon.com/512/906/906344.png",
            "whatsapp": "https://cdn-icons-png.flaticon.com/512/733/733585.png",
            "facebook": "https://cdn-icons-png.flaticon.com/512/733/733547.png",
            "instagram": "https://cdn-icons-png.flaticon.com/512/2111/2111463.png"}
        
        url = logos.get(logo_type, logos["telegram"])
        with urllib.request.urlopen(url) as response:
            logo_data = response.read()
        logo = Image.open(io.BytesIO(logo_data)).convert("RGBA")
        
        logo = logo.resize((qr_img.size[0] // 6, qr_img.size[1] // 6))
        
        qr_img = qr_img.convert("RGBA")
        
        pos_x = (qr_img.size[0] - logo.size[0]) // 2
        pos_y = (qr_img.size[1] - logo.size[1]) // 2
        
        for x in range(logo.size[0]):
            for y in range(logo.size[1]):
                pixel = logo.getpixel((x, y))
                if pixel[3] > 0:
                    qr_img.putpixel((pos_x + x, pos_y + y), pixel)
        
        return qr_img.convert("RGB")
    except:
        return qr_img

text = input('Введите текст для QR-кода: ')
print('\nВыберите цвет:')
print('1-красный')
print('2-синий')
print('3-зеленый')
print('4-желтый')
print('5-фиолетовый')
print('6-оранжевый')
print('7-черный')
print('8-розовый')
print('9-ГОЛ1')
print('10-ГОЛ2')
print('11-ГОЛ3')
col = input('цвет: ')

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
    if j == '1' or j == 'да' or j == 'Да':
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
    if j == '1' or j == 'да' or j == 'Да':
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
    if j == '1' or j == 'да' or j == 'Да':
        img = create_rounded_qr(img, 6)
    color_name = "ГОЛ3"
else:
    colors = {"1":"red", "2":"blue", "3":"green", "4":"yellow", 
              "5":"purple", "6":"orange", "7":"black", "8":"pink"}
    color = colors.get(col, "black")
    img = qr.make_image(fill_color=color, back_color="white")
    if j == '1' or j == 'да' or j == 'Да':
        img = create_rounded_qr(img.convert('RGB'), 6)
    else:
        img = img.convert('RGB')
    color_name = color

if "t.me" in text.lower() or "telegram" in text.lower():
    img = add_logo(img, "telegram")
elif "youtube.com" in text.lower() or "youtu.be" in text.lower():
    img = add_logo(img, "youtube")
elif "vk.com" in text.lower() or "vkontakte" in text.lower():
    img = add_logo(img, "vk")
elif "yandex" in text.lower():
    img = add_logo(img, "yandex")
elif "tiktok" in text.lower():
    img = add_logo(img, "tiktok")
elif "rutube" in text.lower():
    img = add_logo(img, "rutube")
elif "whatsapp" in text.lower() or "вацап" in text.lower():
    img = add_logo(img, "whatsapp")
elif "facebook" in text.lower() or "fb" in text.lower():
    img = add_logo(img, "facebook")
elif "instagram" in text.lower() or "insta" in text.lower():
    img = add_logo(img, "instagram")

print('Готово!')
window = tk.Tk()
img_tk = ImageTk.PhotoImage(img)
label_img = tk.Label(window, image=img_tk)
label_img.pack(pady=10)
label_text = tk.Label(window, text=text, font=("Arial", 40, "bold"))
label_text.pack(pady=10)
window.mainloop()
