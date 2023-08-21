import datetime  # Imports built in datetime module
from constants import Colors  # Import colors class from constants module
import gspread  # Imports Google sheets API
from google.oauth2.service_account import (
    Credentials,
)  # Imports Google service account Credentials
from simple_term_menu import TerminalMenu


# function that defines permission scope, credentials location, sheet location
def get_google_sheet_client(creds_file="creds.json", sheet_name="career_analyzer"):
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    CREDS = Credentials.from_service_account_file(creds_file)
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)

    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open(sheet_name)

    return SHEET


# list that maps survey questions to columns in the google spreadsheet
column_mapping = {
    "What is your name?": "Name",
    "How old are you?": "Age",
    "Please select your career area:": "CareerType",
    "On a scale of 1 to 5, how satisfied are you with your career?": "CareerSatisfaction",
    "Are you considering a career change? (yes/no)": "ConsideringChange",
    "What factors influenced your decision?": "ChangeFactors",
    "Do you prefer remote work? (yes/no)": "RemoteWorkPreference",
}


# Survey class that runs the survey
class Survey:
    def __init__(self):
        self.career_areas = [
            "Technology",
            "Healthcare",
            "Finance",
            "Education",
            "Other",
        ]
        self.career_satisfaction_ratings = [
            "Unhappy",
            "Unsatisfied",
            "Somewhat Satisfied",
            "Happy",
            "Dreamjob",
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

    def add_timestamp(self):
        try:
            timestamp = datetime.datetime.now()
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            self.answers.append(timestamp_str)  # Append the timestamp to the list
            print("Timestamp added to the survey answers.")
        except Exception as e:
            print("Error adding timestamp:", str(e))

    def conduct_survey(self):
        self.answers = []
        print(Colors.OKBLUE + "Welcome to the survey!" + Colors.ENDC)
        self.add_timestamp()

        for i, question in enumerate(column_mapping.keys()):
            if question in self.career_areas:
                # Handle career area selection using TerminalMenu
                career_area_menu = TerminalMenu(self.career_areas, title=question)
                selected_index = career_area_menu.show()
                answer = self.career_areas[selected_index]
                self.answers.append(answer)

            elif (
                question
                == "On a scale of 1 to 5, how satisfied are you with your career?"
            ):
                # Handle satisfaction rating using TerminalMenu
                satisfaction_menu = TerminalMenu(
                    self.career_satisfaction_ratings, title=question
                )
                selected_index = satisfaction_menu.show()
                answer = self.career_satisfaction_ratings[selected_index]
                self.answers.append(answer)

            elif question == "Are you considering a career change? (yes/no)":
                # Handle yes/no question using TerminalMenu
                yes_no_menu = TerminalMenu(["yes", "no"], title=question)
                selected_index = yes_no_menu.show()
                answer = ["yes", "no"][selected_index]
                self.answers.append(answer)

            elif question == "If yes, what factors are influencing your decision?":
                # Handle multiple choice question using TerminalMenu
                factor_menu = TerminalMenu(
                    self.career_change_factors, title=question, multi_select=True
                )
                selected_indices = factor_menu.show()
                selected_factors = [
                    self.career_change_factors[idx] for idx in selected_indices
                ]
                answer = ", ".join(selected_factors)
                self.answers.append(answer)

            elif question == "Do you prefer remote work? (yes/no)":
                # Handle yes/no question using TerminalMenu
                yes_no_menu = TerminalMenu(["yes", "no"], title=question)
                selected_index = yes_no_menu.show()
                answer = ["yes", "no"][selected_index]
                self.answers.append(answer)

        print(Colors.OKBLUE + "Thank you for completing the survey!" + Colors.ENDC)

    def store_results_in_google_sheet(self):  # Store results in googlesheet
        try:
            SHEET = get_google_sheet_client()
            worksheet = SHEET.get_worksheet(0)
            values = [self.answers]
            worksheet.append_rows(values)
            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    def display_results(self):  # Display survey answers to user at the end of survey
        print(Colors.OKBLUE + "Survey Results:" + Colors.ENDC)
        for question, answer in zip(column_mapping.keys(), self.answers[1:]):
            print(
                f"{Colors.OKGREEN}{question}{Colors.ENDC}\n- {Colors.WARNING}Answer: {answer}{Colors.ENDC}\n"
            )
            print("-" * 40)
