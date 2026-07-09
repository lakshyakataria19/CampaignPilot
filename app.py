import streamlit as st
import pandas as pd

from agents.planner import PlannerAgent
from agents.copywriter import CopywriterAgent

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="CampaignPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CampaignPilot AI")
st.caption("AI-Powered Customer Engagement Platform | Multi-Agent Marketing Automation")

st.divider()

# ----------------------------------------------------
# Load Customer Data
# ----------------------------------------------------

customers = pd.read_csv("data/customers.csv")

# ----------------------------------------------------
# Dashboard KPIs
# ----------------------------------------------------

total_customers = len(customers)
avg_spend = int(customers["Total_Spend"].mean())
avg_loyalty = round(customers["Loyalty_Score"].mean(), 1)
high_risk = len(customers[customers["Loyalty_Score"] < 50])

st.subheader("📊 Dashboard Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("👥 Customers", total_customers)
k2.metric("💰 Avg Spend", f"₹{avg_spend:,}")
k3.metric("⭐ Avg Loyalty", avg_loyalty)
k4.metric("⚠️ High Risk", high_risk)

st.divider()

# ----------------------------------------------------
# Customer Selection
# ----------------------------------------------------

customer_name = st.selectbox(
    "Select Customer",
    customers["Name"]
)

customer = customers[customers["Name"] == customer_name].iloc[0]

planner = PlannerAgent()
copywriter = CopywriterAgent()

left, right = st.columns(2)

# ----------------------------------------------------
# Customer Profile
# ----------------------------------------------------

with left:

    with st.container(border=True):

        st.subheader("👤 Customer Profile")

        c1, c2 = st.columns(2)

        with c1:
            st.write(f"**Name**")
            st.write(customer["Name"])

            st.write(f"**Age**")
            st.write(customer["Age"])

            st.write(f"**Gender**")
            st.write(customer["Gender"])

            st.write(f"**City**")
            st.write(customer["City"])

        with c2:
            st.write(f"**Segment**")
            st.write(customer["Segment"])

            st.write(f"**Spend**")
            st.write(f"₹{customer['Total_Spend']:,}")

            st.write(f"**Loyalty Score**")
            st.write(customer["Loyalty_Score"])

            st.write(f"**Preferred Channel**")
            st.write(customer["Preferred_Channel"])

# ----------------------------------------------------
# Generate Campaign
# ----------------------------------------------------

if st.button("🚀 Generate AI Campaign", use_container_width=True):

    with st.spinner("🧠 Planner Agent Thinking..."):
        strategy = planner.run(customer)

    with st.spinner("✍️ Copywriter Agent Writing..."):
        campaign = copywriter.run(customer, strategy)

    # ---------------------------------------------
    # AI Strategy Card
    # ---------------------------------------------

    with right:

        with st.container(border=True):

            st.subheader("🧠 AI Strategy")

            st.markdown(f"""
**🎯 Goal**

{strategy["goal"]}

---

**🎁 Offer**

{strategy["offer"]}

---

**🎨 Tone**

{strategy["tone"]}

---

**📩 Channel**

{strategy["channel"]}

---

**👉 CTA**

{strategy["cta"]}
""")

    st.divider()

    # ---------------------------------------------
    # Campaign Output
    # ---------------------------------------------

    tab1, tab2, tab3 = st.tabs(
        [
            "📧 Email",
            "💬 WhatsApp",
            "📱 Push Notification"
        ]
    )

    with tab1:

        with st.container(border=True):
            st.subheader("📧 Email Campaign")
            st.write(campaign["email"])

    with tab2:

        with st.container(border=True):
            st.subheader("💬 WhatsApp Campaign")
            st.write(campaign["whatsapp"])

    with tab3:

        with st.container(border=True):
            st.subheader("📱 Push Notification")
            st.write(campaign["push"])