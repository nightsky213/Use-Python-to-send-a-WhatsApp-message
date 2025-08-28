import requests

# Replace with your details
ACCESS_TOKEN = "YOUR_WHATSAPP_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
RECIPIENT_PHONE = "RECIPIENT_PHONE_NUMBER"  # Include country code, e.g., "919876543210"

def send_whatsapp_message(message):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_PHONE,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("✅ Message sent successfully:", response.json())
    else:
        print("❌ Error:", response.text)

if __name__ == "__main__":
    send_whatsapp_message("Hello! 🚀 This is an automated WhatsApp message sent using Python & WhatsApp Cloud API.")
