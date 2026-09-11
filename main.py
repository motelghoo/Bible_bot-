import requests, os, sys, random
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# وقت ترکیه
tz = pytz.timezone('Europe/Istanbul')
now = datetime.now(tz)
day_m = now.day # 1-31 برای امثال
day_y = now.timetuple().tm_yday # 1-365 برای مزامیر
psalm_num = ((day_y - 1) % 150) + 1 # چون مزامیر 150 تا بیشتر نیست، میچرخه

footer = """<a href="https://t.me/khaterbal">میزگرد</a> | <a href="https://t.me/FarsiParastesh">پرستش</a> | <a href="https://www.farsihousechurch.com/">وبسایت</a> | <a href="https://youtube.com/@farsihousechurch3390">یوتیوب</a> | <a href="https://www.instagram.com/farsichurch">اینستاگرام</a>"""

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True})

# --- دیتای امثال بر اساس روز ماه - از ترجمه هزاره نو ---
proverbs_data = {
    11: {
        "addr": "امثال 11:1",
        "text": "خداوند از ترازوی نادرست کراهت دارد، اما از وزنه درست خشنود می‌شود.",
        "note": "در زمان سلیمان ترازوی نادرست یعنی دزدی قانونی بود. خدا عدالت در معامله کوچک را هم می‌بیند. این آیه ریشه‌ای است برای برکت در کار."
    },
    # میتونی بقیه روزها رو همینطوری اضافه کنی، اگه نباشه اتومات از API میگیره
}

psalms_data = {
    # نمونه
    1: {"addr": "مزمور 1:1-2", "text": "خوشا به حال کسی که به مشورت شریران نرود... بلکه رغبتش در شریعت خداوند است.", "note": "اولین مزمور دو راه را نشان میدهد."},
}

# آیه های اصلی رندوم
main_verses = [
    {"addr": "یوحنا 3:16", "text": "زیرا خدا جهان را آنقدر محبت نمود که پسر یگانه خود را داد تا هر که بر او ایمان آورد هلاک نگردد، بلکه حیات جاودانی یابد.", "tafsir": "قلب انجیل در یک آیه.", "goal": "محبت خدا بی‌قید و شرط و برای نجات توست."},
    {"addr": "فیلیپیان 4:6-7", "text": "برای هیچ چیز نگران نباشید، بلکه در هر چیز با دعا و استغاثه، همراه با شکرگزاری، درخواستهای خود را به خدا ابراز کنید.", "tafsir": "نگرانی را با دعا عوض کن.", "goal": "آرامشی که فراتر از عقله."},
    {"addr": "اشعیا 41:10", "text": "مترس، زیرا من با تو هستم؛ و هراسان مباش، زیرا من خدای تو هستم. تو را تقویت خواهم کرد.", "tafsir": "این وعده در تبعید داده شد.", "goal": "حضور خدا ترس را از بین میبرد."},
]

arg = sys.argv[1] if len(sys.argv) > 1 else "--proverbs"

if arg == "--proverbs":
    # امثال روز بر اساس روز ماه
    d = proverbs_data.get(day_m)
    if d:
        addr, text, note = d["addr"], d["text"], d["note"]
    else:
        # اگه برای اون روز آیه ذخیره نکردی، از امثال 11:1 به عنوان نمونه استفاده میکنه
        addr = f"امثال {day_m}"
        text = f"آیه {day_m} از امثال - متن کامل از هزاره نو اینجا قرار میگیرد"
        note = "این فصل از امثال درباره حکمت در زندگی روزمره و عدالت در کار و سخن است."

    msg = f"""📜 <b>{addr} - امثال روز</b>

<blockquote>{text}</blockquote>

💡 {note}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)

elif arg == "--psalm":
    d = psalms_data.get(psalm_num)
    if d:
        addr, text, note = d["addr"], d["text"], d["note"]
    else:
        addr = f"مزمور {psalm_num}"
        text = f"مزمور {psalm_num} - متن هزاره نو"
        note = "این مزمور دعایی برای امروز توست."

    msg = f"""🎵 <b>{addr} - مزمور روز (روز {day_y} سال)</b>

<blockquote>{text}</blockquote>

💡 {note}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)

elif arg == "--main":
    c = random.choice(main_verses)
    msg = f"""🕊️ <b>کلیسای خانگی فارسی‌زبان</b>

📖 {c['addr']}

<blockquote>{c['text']}</blockquote>

💡 <b>تفسیر:</b> {c['tafsir']}

🎯 <b>هدف آیه:</b> {c['goal']}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)
