import requests, os, sys
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

tehran = pytz.timezone('Asia/Tehran')
now = datetime.now(tehran)
day_m = now.day
day_y = now.timetuple().tm_yday

footer = """<a href="https://t.me/khaterbal">میزگرد</a> | <a href="https://t.me/FarsiParastesh">پرستش</a> | <a href="https://www.farsihousechurch.com/">وبسایت</a> | <a href="https://youtube.com/@farsihousechurch3390">یوتیوب</a> | <a href="https://www.instagram.com/farsichurch">اینستاگرام</a>"""

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True})

# لیست امثال - 31 تا
proverbs = [
    {"addr":"امثال 1:7","text":"<b>ترس خداوند آغاز معرفت است</b>؛ جاهلان حکمت را خوار می‌شمارند.","tafsir":"حکمت از احترام به خدا شروع میشه.","note":"ترس یعنی احترام عمیق فرزند به پدر."},
    {"addr":"امثال 3:5-6","text":"با <b>تمام دل بر خداوند توکل نما</b> و بر عقل خود تکیه مکن.","tafsir":"وقتی به او توکل کنی، راهت را صاف میکند.","note":"راست گردانیدن یعنی برداشتن موانع."},
    {"addr":"امثال 4:23","text":"<b>دل خود را محافظت نما</b>، زیرا سرچشمه حیات از آن است.","tafsir":"ورودی قلبت، خروجی زندگیت را میسازد.","note":"در عبری دل مرکز تصمیم است."},
]
while len(proverbs) < 31:
    proverbs.extend(proverbs)
proverbs = proverbs[:31]

# لیست مزامیر - 150 تا
psalms = [
    {"addr":"مزمور 23:1","text":"<b>خداوند شبان من است</b>، محتاج به هیچ چیز نخواهم بود.","tafsir":"وقتی شبان تو خداست، کمبود نداری.","note":"داوود خودش چوپان بود."},
    {"addr":"مزمور 27:1","text":"خداوند <b>نور و نجات من است</b>، از که بترسم؟","tafsir":"نور که باشد، تاریکی تهدید نیست.","note":"این مزمور در زمان فرار نوشته شد."},
]
while len(psalms) < 150:
    psalms.extend(psalms)
psalms = psalms[:150]

# لیست آیه روز اصلی
mains = [
    {"addr":"فیلیپیان 4:6-7","text":"برای <b>هیچ چیز نگران نباشید</b>، بلکه با دعا درخواستهای خود را به خدا بگویید.","inspire":"امروز نگرانی را به دعا تبدیل کن.","notes":"پولس از زندان نوشت.","goal":"خدا آرامش فراتر از عقل میدهد."},
]

# تشخیص چی باید بفرسته
arg = sys.argv[1] if len(sys.argv) > 1 else "--proverbs"

if arg == "--proverbs" or "--proverbs" not in sys.argv and "--psalm" not in sys.argv and "--main" not in sys.argv:
    p = proverbs[day_m - 1]
    msg = f"""📜 <b>امثال روز - {p['addr']}</b>

<blockquote>{p['text']}</blockquote>

ترجمه: هزاره نو

💡 <b>تفسیر:</b>
{p['tafsir']}

🔍 <b>نکته جالب:</b>
{p['note']}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)

elif arg == "--psalm":
    ps = psalms[(day_y - 1) % 150]
    msg = f"""🎵 <b>مزمور روز - {ps['addr']}</b>

<blockquote>{ps['text']}</blockquote>

ترجمه: هزاره نو

💡 <b>تفسیر:</b>
{ps['tafsir']}

🔍 <b>نکته جالب:</b>
{ps['note']}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)

elif arg == "--main":
    import random
    c = random.choice(mains)
    msg = f"""🕊️ <b>کلیسای خانگی فارسی‌زبان</b>

📖 آیه روز: {c['addr']}

<blockquote>{c['text']}</blockquote>

ترجمه: هزاره نو

✨ {c['inspire']}

🔍 {c['notes']}

🎯 {c['goal']}

━━━━━━━━━━━━━━━
🔗 {footer}"""
    send(msg)
