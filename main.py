try:
    import telebot,time,requests,threading,subprocess,datetime,random,threading,os,json
    from datetime import datetime, timedelta
    from telebot import types
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    TOKEN_BOT = "7326920590:AAGF43qN_a2tElft2mSQEDRfOy8qM8hjIyw"
    chat_id = -1002170831477
    ADMIN_ID = [6452283369]
    VIP_FILE = "vip.json"
    bot = telebot.TeleBot(TOKEN_BOT)

    def load_vip_data():
        with open(VIP_FILE, 'r') as f:
            return json.load(f)
    def save_vip_data(vip_data):
        with open(VIP_FILE, 'w') as f:
            json.dump(vip_data, f, indent=4)
    def checkvip(user_id):
        homnay = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        vip_data = load_vip_data()
        if user_id in vip_data:
            if homnay < vip_data[user_id]['tghethan']:
                return True
            else:
                return False
        else:
            return False
    bot = telebot.TeleBot(TOKEN_BOT)

    def xoatn(message,dl): 
        time.sleep(dl) 
        bot.delete_message(message.chat.id, message.message_id) 

    @bot.message_handler(commands=['getkey'])
    def getkey_cmd(message):
        user_id = int(message.from_user.id)
        full_name = message.from_user.full_name
        ngay = int(datetime.now().strftime('%d'))
        keyso = str(ngay*8276383 + 93732373*user_id+user_id*user_id-ngay)
        key = "BOT/"+keyso
        print(user_id,key)
        url = f"https://traffic24h.net/Getapi.php?api=twiBqSUdaDfbNsKrejJVZuTEHpgIchXAMYkxLOvlyGzQmRConFWP&url=https://tienich.x10.bz/hdt.html?key={key}"
        data = requests.get(url).json()
        linkvuot = data['shortenedUrl']
        tgsuccess = datetime.now().strftime("%d/%m/%Y")
        video = random.choice(["https://offvn.click/1.mp4"])
        help_text = f'''Xin Chào ! <a href="tg://user?id={user_id}">{full_name}</a>\n<blockquote>» Link Key Ngày {tgsuccess} Là : {linkvuot}\n» ⚠️ Vượt xong nhập key sau lệnh /key\n💭 Ví dụ: /key BOT/42236748505343623944</blockquote>'''
        bot.send_video(message.chat.id, video=video, caption=help_text, reply_to_message_id=message.message_id, supports_streaming=True,parse_mode='Html')
        threading.Thread(target=xoatn, args=(message,0)).start()
    @bot.message_handler(commands=['key'])
    def nhapkey(message):
        if len(message.text.split()) < 2:
            bot.reply_to(message, "⚠️ Vui Lòng Sử Dụng Key Sau Lệnh /key.\n💬 Ví Dụ: /key BOT/123456789.")
            threading.Thread(target=xoatn, args=(message,0)).start()
            return
        user_id = int(message.from_user.id)
        ngay = int(datetime.now().strftime('%d'))
        keyso = str(ngay*8276383 + 93732373*user_id+user_id*user_id-ngay)
        key = "BOT/"+keyso
        ghifile = f"{user_id}|{key}\n"
        if message.text.split()[1] == key:
            with open('user.txt', 'a') as key:
                key.write(ghifile)
            bot.reply_to(message, "<blockquote>Chúc Mừng Bạn Đã Nhập Key Chính Xác !\nVà Giờ Có Thể Sử Dụng Lệnh /spam</blockquote>",parse_mode='Html')
            threading.Thread(target=xoatn, args=(message,0)).start()
        else:
            bot.reply_to(message, "⚠️ Key Bạn Nhập Không Chính Xác\nVui Lòng Nhập Lại.")
        bot.reply_to(message, parse_mode="HTML")

    last_used = {}
    @bot.message_handler(commands=['spam'])
    def handle_sms_command(message):
        user_id = int(message.from_user.id)
        full_name = message.from_user.full_name
        current_time = time.time()
        if user_id in last_used:
            elapsed_time = current_time - last_used[user_id]
            if elapsed_time < 300:
                remaining_time = 300 - elapsed_time
                bot.reply_to(message, f"💬 Lưu Ý : Lệnh FREE Đợi 300 Giây, Mới Được Sử Dụng Lại.\n⚠️ Vui lòng thử lại sau {int(remaining_time)} giây.")
                return

        ngay = int(datetime.now().strftime('%d'))
        keyso = str(ngay*8276383 + 93732373*user_id+user_id*user_id-ngay)
        key = "BOT/"+keyso
        with open('user.txt', 'a') as ok:
            pass
        with open('user.txt', 'r') as file:
            try:
                all_key = file.read().split("\n")
                allowed_users = [line.split('|')[1] for line in all_key if line.startswith(str(user_id))]
            except:
                allowed_users = "Trống"
            if str(key) not in allowed_users:
                bot.reply_to(message, "⚠️ Bạn Chưa Lấy Key Ngày Hôm Nay.\n💬 Vui Lòng Nhập Lệnh /getkey\nĐể Lấy Key Ngày Hôm Nay.")
                return
            if len(message.text.split()) < 3:
                bot.reply_to(message, "⚠️ Hướng Dẫn Sử Dụng Lệnh /spam\n💬 Ví Dụ: /spam 0969549113 5")
                return
            phone_number = message.text.split()[1]
            solan = int(message.text.split()[2])
            chesdt = list(phone_number)
            dache = ''.join(chesdt[0:0])+"********"+''.join(chesdt[8:])
            if solan > 5:
                bot.reply_to(message, "⚠️ Chỉ Có Lệnh VIP Mới Được Sử Dụng Số Lặp Lớn Hơn 5. \n💬 Mua VIP Xin Liên Hệ: @off_vn Hoặc Nhập Lệnh /muavip.")
                return

            tgsuccess = datetime.now().strftime("%d/%m/%Y")
            gio = datetime.now().strftime("%H:%M:%S")
            video = random.choice(["https://offvn.io.vn/sms.mp4"])
            keyboard1 = InlineKeyboardMarkup(row_width=2)
            keyboard1.add(
                InlineKeyboardButton(text="💬 Liên Hệ ADMIN", url='https://t.me/off_vn'),
    )
            guidi = f"⚡<b>TẤN CÔNG ĐÃ GỬI ĐI</b>⚡\n<blockquote>╭───────────────╮\n│» <b>👤 Name</b>: <a href='tg://user?id={user_id}'>{full_name}</a>\n│» <b>🆔 ID</b>: <a href='tg://user?id={user_id}'>{user_id}</a>\n│» <b>🗓️ Ngày</b>: {tgsuccess}\n│» <b>⏰ Giờ</b>: {gio}\n├───────────⭓\n│» ☎️ <b>SĐT</b>: {dache}\n│» 🔄 <b>LẶP</b>: {solan}\n│» 💳 <b>GÓI</b>: <b>FREE</b>\n╰───────────────╯</blockquote>"
            bot.send_video(message.chat.id, video=video, caption=guidi, reply_to_message_id=message.message_id, supports_streaming=True,parse_mode='Html', reply_markup=keyboard1)
            threading.Thread(target=xoatn, args=(message,0)).start()
            last_used[user_id] = current_time
            process = subprocess.Popen(['python', 'free.py', phone_number, str(solan)])
            process.wait()
            threading.Thread(target=run_subprocess, args=(phone_number, solan, message)).start()

    @bot.message_handler(commands=['adduser'])
    def adduser(message):
        user_id = message.from_user.id
        if user_id not in ADMIN_ID:
            bot.reply_to(message, "Bạn không được phép sử dụng lệnh này!")
            return
        if len(message.text.split()) < 3:
            bot.reply_to(message, "Sử dụng: /adduser {nhập id} {số ngày}")
            return

        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''
        username = message.from_user.username or None
        user_id_add = message.text.split()[1]
        songay = int(message.text.split()[2])
        homnay = datetime.now()
        ngayhethan = homnay + timedelta(days=songay)
        ngayhethan_int = int(ngayhethan.strftime("%Y%m%d%H%M%S"))
        ngayhethan_str = ngayhethan.strftime("%Y-%m-%d %H:%M:%S")
        vip_data = load_vip_data()
        vip_data[str(user_id_add)] = {"fullname": f"{first_name} {last_name}", "username": "@"+username, "tghethan": ngayhethan_int}
        save_vip_data(vip_data)
        bot.reply_to(message, f"💬 Đã thêm người dùng có id {user_id_add} vào danh sách VIP!\n🗓️ Thời gian hết hạn: {ngayhethan_str}")
        threading.Thread(target=xoatn, args=(message,0)).start()

    last_used = {}
    @bot.message_handler(commands=['spamvip'])
    def handle_sms_command(message):
        user_id = str(message.from_user.id)
        full_name = message.from_user.full_name or None
        current_time = time.time()
        if user_id in last_used:
            elapsed_time = current_time - last_used[user_id]
            if elapsed_time < 250:
                remaining_time = 250 - elapsed_time
                bot.reply_to(message, f"💬 Lưu Ý : Lệnh VIP Đợi 250 Giây, Mới Được Sử Dụng Lại.\n⚠️ Vui lòng thử lại sau {int(remaining_time)} giây.")
                return
        if True != checkvip(user_id):
            bot.reply_to(message, "⚠️ Bạn Chưa Mua Vip Bạn Chưa Được Phép Sử Dụng Lệnh Này!\n💬 Hãy Nhập Lệnh /muavip Để Mua VIP")
            return
        if len(message.text.split()) < 3:
            bot.reply_to(message, "⚠️ Hướng Dẫn Sử Dụng Lệnh /spamvip\n💬 Ví Dụ: /spamvip 0969549113 50")
            return
        phone_number = message.text.split()[1]
        solan = int(message.text.split()[2])
        chesdt = list(phone_number)
        dache = ''.join(chesdt[0:0])+"********"+''.join(chesdt[8:])
        if solan > 50:
            bot.reply_to(message, "⚠️ Lệnh VIP Được Sử Dụng Số Lặp Tối Đa 50. \n💬 Ví Dụ: /spamvip 0969549113 50")
            return

        tgsuccess = datetime.now().strftime("%d/%m/%Y")
        gio = datetime.now().strftime("%H:%M:%S")
        video = random.choice(["https://offvn.io.vn/sms.mp4"])
        keyboard1 = InlineKeyboardMarkup(row_width=2)
        keyboard1.add(
            InlineKeyboardButton(text="💬 Liên Hệ ADMIN", url='https://t.me/off_vn'),
    )
        guidi = f"⚡<b>TẤN CÔNG ĐÃ GỬI ĐI</b>⚡\n<blockquote>╭───────────────╮\n│» <b>👤 Name</b>: <a href='tg://user?id={user_id}'>{full_name}</a>\n│» <b>🆔 ID</b>: <a href='tg://user?id={user_id}'>{user_id}</a>\n│» <b>🗓️ Ngày</b>: {tgsuccess}\n│» <b>⏰ Giờ</b>: {gio}\n├───────────⭓\n│» ☎️ <b>SĐT</b>: {dache}\n│» 🔄 <b>LẶP</b>: {solan}\n│» 💳 <b>GÓI</b>: <b>VIP</b>\n╰───────────────╯</blockquote>"
        bot.send_video(message.chat.id, video=video, caption=guidi, reply_to_message_id=message.message_id, supports_streaming=True,parse_mode='Html', reply_markup=keyboard1)
        threading.Thread(target=xoatn, args=(message,0)).start()
        last_used[user_id] = current_time
        process = subprocess.Popen(['python', 'sms.py', phone_number, str(solan)])
        process.wait()
        threading.Thread(target=run_subprocess, args=(phone_number, solan, message)).start()
    
    @bot.message_handler(commands=['stop'])
    def stop(message):
        user_id = message.from_user.id
        if user_id not in ADMIN_ID:
            bot.reply_to(message, "Bạn không được phép sử dụng lệnh này!")
            return
        
        bot.reply_to(message, "⚠️ Bot Spam Call SMS Đã Tắt...")
        bot.stop_polling()
    
    bot.infinity_polling()
except:
    import os
    os.system('pip install telebot && pip install requests')