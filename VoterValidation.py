# FIRST: define the function
def check_voter_eligibility(age, citizen, felony):
    if age < 18:
        print("You must be at least 18 years old to vote.")
        return False
    elif not citizen:
        print("You must be a citizen to vote.")
        return False
    elif felony:
        print("People with felony convictions may not be eligible.")
        return False
    else:
        return True

# THEN: ask the user and use the function
try:
    age = int(input("How old are you? "))
    citizen_input = input("Are you a citizen? (yes/no): ").lower()
    felony_input = input("Do you have a felony record? (yes/no): ").lower()

    citizen = citizen_input == "yes"
    felony = felony_input == "yes"

    result = check_voter_eligibility(age, citizen, felony)

    if result:
        print("✅ You are eligible to vote!")
    else:
        print("❌ You are NOT eligible to vote.")
except ValueError:
    print("Please enter a valid number for age.")
