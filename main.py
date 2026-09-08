import requests, random, os, time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

verses = [
    {"text": "در دنيا برای شما زحمت خواهد بود، اما دل قوی داريد، زيرا من بر دنيا غالب آمده‌ام.", "addr": "یوحنا ۱۶:۳۳"},
    {"text": "خداوند شبان من است، محتاج به هیچ چیز نخواهم بود.", "addr": "مزمور ۲۳:۱"},
    {"text": "همهٔ چیزها برای خیریتِ آنانی که خدا را دوست می‌دارند، با هم در کار است.", "addr": "رومیان ۸:۲۸"},
    {"text": "نترس، زیرا من با تو هستم.", "addr": "اشعیا ۴۱:۱۰"},
    {"text": "او به خستگان قوت می‌بخشد و ناتوانان را نیرو می‌افزاید.", "addr": "اشعیا ۴۰:۲۹"},
]

# تست: 5 پیام هر 1 دقیقه
for i in range(5):
    chosen = random.choice(verses)
    message = f"✝️ تست {i+1}/5\n\n«{chosen['text']}»\n\n— {chosen['addr']}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
    print(f"Sent {i+1}: {r.text}")
    if i < 4:
        time.sleep(60)
