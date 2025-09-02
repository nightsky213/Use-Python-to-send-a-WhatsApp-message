import requests
import pandas as pd

# Replace with your details
ACCESS_TOKEN = "YOUR_WHATSAPP_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"

def send_marketing_message(recipient_phone, customer_name, promo_link):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_phone,
        "type": "template",
        "template": {
            "name": "promo_offer",  # <-- Your approved template name
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": customer_name},
                        {"type": "text", "text": promo_link}
                    ]
                }
            ]
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ Sent to {recipient_phone}: {response.json()}")
    else:
        print(f"❌ Error sending to {recipient_phone}: {response.text}")

def bulk_send(csv_file, promo_link):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        send_marketing_message(row['phone'], row['name'], promo_link)

if __name__ == "__main__":
    bulk_send("customers.csv", "https://yourstore.com/sale")
