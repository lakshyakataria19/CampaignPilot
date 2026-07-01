import json
from services.gemini import ask_gemini


class PlannerAgent:

    def run(self, customer):

        prompt = f"""
You are an expert Product Marketing Manager.

Analyse this customer.

Name: {customer["Name"]}

Age: {customer["Age"]}

Segment: {customer["Segment"]}

City: {customer["City"]}

Last Purchase: {customer["Last_Purchase_Days"]} days ago

Preferred Channel: {customer["Preferred_Channel"]}

Total Spend: ₹{customer["Total_Spend"]}

Loyalty Score: {customer["Loyalty_Score"]}

Decide

1. Campaign Goal

2. Best Offer

3. Best Tone

4. Best Channel

5. CTA

Explain WHY.

Return ONLY valid JSON.

Format exactly like this:

{{
    "goal":"",
    "offer":"",
    "tone":"",
    "channel":"",
    "cta":"",
    "reason":""
}}

Do not add markdown.

Do not use ```.

Return only JSON.
"""

        response = ask_gemini(prompt)
        return json.loads(response)