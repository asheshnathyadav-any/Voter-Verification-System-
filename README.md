# Voter-Verification-System-
README for Voting Verification Project
Project Title
Election Commission of India - Voter Verification System in Python
Student : Ashesh Nath Yadav
Registration Number: 25BSA10068
VIT Bhopal
Supervisor:Professor Santosh Kumar
Project Description
This Python project simulates a voter verification system for the Election Commission of India that checks voter eligibility based on age and validates the EPIC (Electoral Photo Identity Card) number and first letter of the voter's name. The project ensures only eligible and valid voters can proceed for voting by verifying their credentials.
Features
•	Accepts voter details interactively via input.
•	Validates age eligibility (18 years or older).
•	Verifies EPIC number against a dictionary containing valid voters' details.
•	Matches first letter of name with allowed letters for the given EPIC number.
•	Prints voter details and confirmation if validated.
•	Provides appropriate error messages for invalid inputs or ineligibility.
Prerequisites
•	Python 3.x environment
•	Basic knowledge of Python input/output and conditionals
How to Run
1.	Run the Python script in any IDE or command line.
2.	Enter your name, the first letter of your name, and your age as prompted.
3.	If eligible, enter your EPIC NO when prompted.
4.	The program will verify and display voting booth details or error message.
Example Output
text
**ELECTION COMMISSION OF INDIA**

 Welcome, Ashesh
 Your age is: 21
 Your verification is being processed...

 You are eligible to vote.
 Enter your EPIC NO (1 to 7): 1
 Verification successful. You are a valid voter, Ashesh, with EPIC NO: 1.
 Place of voting booth: Akbarpur
 Ward no.: 12
 Date of voting: 21.12.2025

**THANK YOU FOR VISITING ELECTION COMMISSION OF INDIA**
                **HAVE A NICE DAY**  
Pseudocode
text
START

INPUT name
INPUT first letter of name (lowercase)
INPUT age

DISPLAY Election Commission header and welcome message

IF age >= 18 THEN
    DISPLAY "You are eligible to vote."
    INPUT EPIC_NO
    
    DEFINE valid_voters dictionary with EPIC numbered keys and values as tuples containing:
        - list of allowed letters
        - place of voting booth
        - ward number
        - date of voting
    
    IF EPIC_NO in valid_voters THEN
        EXTRACT letters, place, ward, and date from valid_voters[EPIC_NO]
        IF first letter in letters THEN
            DISPLAY successful verification with details
        ELSE
            DISPLAY "Invalid voter: First letter does not match EPIC NO."
        ENDIF
    ELSE
        DISPLAY "Invalid EPIC NO."
    ENDIF
ELSE
    DISPLAY "You are not eligible to vote."
ENDIF

DISPLAY thank you message

END
Code Snippet
python
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
    EPIC_NO = int(input(" Enter your EPIC NO (1 to 7): ")) 
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
            print(f" Verification successful. You are a valid voter, {name}, with EPIC NO: {EPIC_NO}.")
            print(f" Place of voting booth: {place}")
            print(f" Ward no.: {ward}")
            print(f" Date of voting: {date}")
        else:
            print(" Invalid voter: First letter does not match EPIC NO.")
    else:
        print(" Invalid EPIC NO.")
else:
    print(" You are not eligible to vote.")
print("\n**THANK YOU FOR VISITING ELECTION COMMISSION OF INDIA**")
print("                **HAVE A NICE DAY**   ")
Workflow and Flowchart
•	The workflow diagram illustrates steps from taking user input to verification and final response.
•	Flowchart shows decision points for age eligibility, EPIC number verification, and letter matching.
•	(Insert your uploaded screenshots of workflow and flowchart here, e.g. workflow.png, flowchart.png)
Important Points
•	Age validation is mandatory to ensure legal eligibility.
•	EPIC NO acts as a unique identifier with predefined valid entries.
•	Matching the first letter adds an extra layer of authentication.
•	User-friendly prompts guide the voter through verification stages.
Future Enhancements
•	Add database integration for live voter records.
•	Incorporate biometric verification.
•	Extend to web or mobile app platform.
•	Enable real-time voting status updates.
References
•	Election Commission of India official guidelines.
•	Python input/output and dictionaries documentation.
