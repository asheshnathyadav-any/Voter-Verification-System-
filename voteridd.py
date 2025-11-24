name = input("Enter your name: ")
n = input("Enter the first letter of your name : ").lower()
age = int(input("Enter your age: "))
print("   ")
print("**ELECTION COMMISSION OF INDIA**")
print("   ")
print(" Welcome,", name)
print(" Your age is:", age)
print(" Your verification is being processed...")

if age >= 18:
    print(" You are eligible to vote.")
    EPIC_NO = int(input(" Enter your EPIC NO (1 to 7): ")) #EPIC_NO is a unique id no. assigned to each voter
    valid_voters = {
        1: (['a', 'b', 'c', 'd'], "Akbarpur", 12, "21.12.2025"),
        2: (['e', 'f', 'g', 'h'], "Ayodhya", 24, "25.12.2025"),
        3: (['i', 'j', 'k', 'l'], "Gomtinagar", 32, "28.12.2025"),
        4: (['m', 'n', 'o', 'p'], "Chinahat", 25, "29.12.2025"),
        5: (['q', 'r', 's', 't'], "Aisbagh", 54, "30.12.2025"),
        6: (['u', 'v', 'w', 'x'], "Hazratganj", 18, "31.12.2025"),
        7: (['y', 'z'], "Rajajipuram", 40, "01.01.2026"),
    }
    if EPIC_NO in valid_voters:
        letters, place, ward, date = valid_voters[EPIC_NO]
        if n in letters:
            print( f" Verification successful. You are a valid voter, {name}, with EPIC NO: {EPIC_NO}.")
            print( f" Place of voting booth: {place}")
            print( f" Ward no.: {ward}")
            print( f" Date of voting: {date}")
        else:
            print(" Invalid voter: First letter does not match EPIC NO.")
    else:
        print(" Invalid EPIC NO.")
else:
    print(" You are not eligible to vote.")
print("\n**THANK YOU FOR VISITING ELECTION COMMISSION OF INDIA**")
print("                **HAVE A NICE DAY**   ")
