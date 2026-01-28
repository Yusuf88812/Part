import requests
from django.conf import settings

def send_telegram_message(name, email, subject, message):
    token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_USER_ID', None)
    
    if not token or token == 'YOUR_BOT_TOKEN_HERE':
        print("Telegram bot token is not configured.")
        return False
        
    text = f"🚀 *Yangi xabar keldi!*\n\n" \
           f"👤 *Ism:* {name}\n" \
           f"📧 *Email:* {email}\n" \
           f"📝 *Mavzu:* {subject}\n\n" \
           f"💬 *Xabar:* \n{message}"
           
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Telegram API Error: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
        return False
