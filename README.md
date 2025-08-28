# WhatsApp Message Automation with Python

This project demonstrates how to send a **WhatsApp message** using **Python** and the **WhatsApp Cloud API**.

## 🚀 Setup Instructions

1. Create a **Meta Developer Account** at [Meta for Developers](https://developers.facebook.com/).
2. Set up a **WhatsApp Business Account** and register a phone number.
3. Get your **Access Token** with `whatsapp_business_messaging` permission.
4. Get your **Phone Number ID** from the WhatsApp Business settings.
5. Replace in `send_whatsapp.py`:
   - `YOUR_WHATSAPP_ACCESS_TOKEN`
   - `YOUR_PHONE_NUMBER_ID`
   - `RECIPIENT_PHONE_NUMBER` (with country code, e.g., `919876543210` for India)
6. Install dependencies:
   ```bash
   pip install requests
   ```
7. Run the script:
   ```bash
   python send_whatsapp.py
   ```

## ⚠️ Notes
- Messages can only be sent to **verified numbers** (or pre-approved sandbox numbers in test mode).  
- For production, your WhatsApp Business Account must be approved.  
- Keep your Access Token **secure**.  
