import pandas as pd

from agents.planner import PlannerAgent
from agents.copywriter import CopywriterAgent


# Load customer data
customers = pd.read_csv("data/customers.csv")

# Select first customer
customer = customers.iloc[0]

# Create AI agents
planner = PlannerAgent()
copywriter = CopywriterAgent()

print("=" * 60)
print("CUSTOMER")
print("=" * 60)
print(customer)

# Planner creates strategy
strategy = planner.run(customer)

print("\n" + "=" * 60)
print("AI STRATEGY")
print("=" * 60)
print(strategy)

# Copywriter generates campaign
campaign = copywriter.run(customer, strategy)

print("\n" + "=" * 60)
print("EMAIL")
print("=" * 60)
print(campaign["email"])

print("\n" + "=" * 60)
print("WHATSAPP")
print("=" * 60)
print(campaign["whatsapp"])

print("\n" + "=" * 60)
print("PUSH NOTIFICATION")
print("=" * 60)
print(campaign["push"])