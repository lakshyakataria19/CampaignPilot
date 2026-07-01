import streamlit as st
import pandas as pd

from agents.planner import PlannerAgent
from agents.copywriter import CopywriterAgent

st.set_page_config(
    page_title="CampaignPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CampaignPilot AI")
st.subheader("AI Powered Customer Engagement Platform")

customers = pd.read_csv("data/customers.csv")

customer_name = st.selectbox(
    "Select Customer",
    customers["Name"]
)

customer = customers[customers["Name"] == customer_name].iloc[0]

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Customer Profile")

    st.write(f"**Name:** {customer['Name']}")
    st.write(f"**Age:** {customer['Age']}")
    st.write(f"**Segment:** {customer['Segment']}")
    st.write(f"**City:** {customer['City']}")
    st.write(f"**Total Spend:** ₹{customer['Total_Spend']}")
    st.write(f"**Preferred Channel:** {customer['Preferred_Channel']}")

planner = PlannerAgent()
copywriter = CopywriterAgent()

if st.button("🚀 Generate Campaign"):

    with st.spinner("Planner Agent Thinking..."):

        strategy = planner.run(customer)

    with st.spinner("Copywriter Agent Writing..."):

        campaign = copywriter.run(customer, strategy)

    with col2:

        st.subheader("AI Strategy")

        st.json(strategy)

    st.divider()

    st.subheader("📧 Email")

    st.write(campaign["email"])

    st.divider()

    st.subheader("💬 WhatsApp")

    st.write(campaign["whatsapp"])

    st.divider()

    st.subheader("📱 Push Notification")

    st.write(campaign["push"])