import json
from services.gemini import ask_gemini


class CopywriterAgent:

    def run(self, customer, strategy):

        prompt = f"""
You are an expert marketing copywriter.

Customer Details

Name: {customer["Name"]}

Segment: {customer["Segment"]}

City: {customer["City"]}

Campaign Strategy

Goal: {strategy["goal"]}

Offer: {strategy["offer"]}

Tone: {strategy["tone"]}

Channel: {strategy["channel"]}

CTA: {strategy["cta"]}

Write

1. Marketing Email

2. WhatsApp Message

3. Push Notification

Return ONLY valid JSON.

Format:

{{
    "email":"",
    "whatsapp":"",
    "push":""
}}

Do not add markdown.

Return only JSON.
"""

        response = ask_gemini(prompt)

        return json.loads(response)