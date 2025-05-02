def analyze_campaign(budget, ad_cost):
    ads = budget // ad_cost
    leftover = budget % ad_cost
    double_ad_cost = ad_cost * 2
    increased_budget = budget * 1.10

    print(f"You can run {ads} full ads.")
    print(f"You will have ${leftover} left over.")
    print(f"If ad prices doubled, they would cost ${double_ad_cost}.")
    print(f"If your budget increased by 10%, it would be ${increased_budget:.2f}.")

try:
    budget = int(input("What is your total campaign budget in dollars? "))
    ad_cost = int(input("How much does each ad cost? "))

    # ✅ THIS is what was missing!
    analyze_campaign(budget, ad_cost)

except ValueError:
    print("Please enter numbers only - no words or symbols.")