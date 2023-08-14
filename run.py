import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Load the service account credentials from the JSON file
CREDS = Credentials.from_service_account_file("creds.json")

# Authorize the credentials with the required scopes
SCOPED_CREDS = CREDS.with_scopes(["https://www.googleapis.com/auth/spreadsheets"])

# Authorize the gspread client with the scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Spreadsheet by its title
SHEET = GSPREAD_CLIENT.open("career_analyzer")


class Survey:
    def __init__(self):
        self.questions = [
            "What is your name?",
            "How old are you?",
            "Please select your career area:",
            "On a scale of 1 to 5, how satisfied are you with your career?",
            "Are you considering a career change? (yes/no)",
            "If yes, what factors are influencing your decision? (comma-separated)",
            "Do you prefer remote work? (yes/no)",
        ]
        self.career_areas = [
            "Technology",
            "Healthcare",
            "Finance",
            "Education",
            "Other",
        ]
        self.career_change_factors = [
            "Work-life balance",
            "Salary",
            "Opportunities for growth",
            "Company culture",
            "Location",
            "Other",
        ]
        self.answers = []

    def conduct_survey(self):
        print("Welcome to the survey!")
        for i, question in enumerate(self.questions):
            if i == 2:
                print(f"{question} (Select a number)")
                for idx, area in enumerate(self.career_areas, start=1):
                    print(f"{idx}. {area}")
                choice = input("Your choice: ")
                try:
                    choice_idx = int(choice) - 1
                    answer = self.career_areas[choice_idx]
                except (ValueError, IndexError):
                    answer = "Invalid choice"
            elif i == 5:  # Career change factors question
                print(
                    "Select career change factors (Enter the number(s) separated by spaces):"
                )
                for idx, factor in enumerate(self.career_change_factors, start=1):
                    print(f"{idx}. {factor}")
                choices = input("Your choice(s): ").split()
                selected_factors = []
                try:
                    for choice in choices:
                        choice_idx = int(choice) - 1
                        selected_factors.append(self.career_change_factors[choice_idx])
                    answer = ", ".join(selected_factors)
                except (ValueError, IndexError):
                    answer = "Invalid choice"
            else:
                answer = input(f"{question} ")
            self.answers.append(answer)

        print("Thank you for completing the survey!")

    def store_results_in_google_sheet(self):
        try:
            # Open the first sheet of the Google Spreadsheet
            worksheet = SHEET.get_worksheet(0)

            # Convert the survey answers into a list of lists for each row
            values = [self.answers]

            # Append the values to the Google Sheet
            worksheet.append_rows(values)

            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    def display_results(self):
        print("Survey Results:")
        for question, answer in zip(self.questions, self.answers):
            print(f"{question}\n- Answer: {answer}\n")


# Create a survey instance
survey = Survey()

# Conduct the survey
survey.conduct_survey()
# Store survey results in Google Sheet
survey.store_results_in_google_sheet()

# Display survey results
survey.display_results()
