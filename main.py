import requests, random, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

print(f"BOT exists: {bool(BOT_TOKEN)}")
print(f"CHANNEL_ID raw: '{CHANNEL_ID}'")

verses = [
    {"text": "در دنيا برای شما زحمت خواهد بود، اما دل قوی داريد، زيرا من بر دنيا غالب آمده‌ام.", "addr": "یوحنا ۱۶:۳۳"},
    {"text": "خداوند شبان من است، محتاج به هیچ چیز نخواهم بود.", "addr": "مزمور ۲۳:۱"},
    {"text": "همهٔ چیزها برای خیریتِ آنانی که خدا را دوست می‌دارند، با هم در کار است.", "addr": "رومیان ۸:۲۸"},
    {"text": "نترس، زیرا من با تو هستم.", "addr": "اشعیا ۴۱:۱۰"},
    {"text": "او به خستگان قوت می‌بخشد و ناتوانان را نیرو می‌افزاید.", "addr": "اشعیا ۴۰:۲۹"},
]

chosen = random.choice(verses)
message = f"✝️ آیه امروز\n\n«{chosen['text']}»\n\n— {chosen['addr']}"

# تمیز کردن آیدی
if CHANNEL_ID:
    CHANNEL_ID = CHANNEL_ID.strip()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
print(f"Sending to: {CHANNEL_ID}")
resp = requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
print(f"Telegram response: {resp.status_code}")
print(f"Telegram body: {resp.text}")

if resp.status_code != 200:
    print("FAILED - check if bot is admin and CHANNEL_ID is correct")
else:
    print("SUCCESS")
