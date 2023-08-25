import datetime  # Imports built in datetime module
import gspread  # Imports Google sheets API
from google.oauth2.service_account import (
    Credentials,
)  # Imports Google service account Credentials
from simple_term_menu import TerminalMenu
from termcolor import colored


"""function that defines permission scope,
credentials location, sheet location"""


def get_google_sheet_client(
    creds_file="creds.json", sheet_name="career_analyzer"
):
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


# Survey class that contains survey logic
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

    # Function that retrieves datetime and appends it to the list
    def add_timestamp(self):
        try:
            timestamp = datetime.datetime.now()  # get current datetime
            timestamp_str = timestamp.strftime
            ("%Y-%m-%d %H:%M:%S")  # format timestamp
            # Append the timestamp to the list
            self.answers.append(timestamp_str)
            print("Timestamp added to the survey answers.")
        except Exception as e:
            print("Error adding timestamp:", str(e))

    # Function that handles name input validation
    def handle_name_input(self, question):
        while True:
            answer = input(colored(question + "\n", "green"))

            # Check for minimum length
            if len(answer.strip()) < 2:  # Minimum 2 characters
                error_message = (
                    "Please provide a valid name (at least 2 characters)."
                )
                print(colored(error_message, "red"))
                continue

            # Check for alphabetic characters only
            if not answer.isalpha():
                error_message = "Please provide a valid name (letters only)."
                print(colored(error_message, "red"))
                continue

            # Capitalize the first letter
            formatted_name = answer.capitalize()

            self.answers.append(formatted_name)
            break

    # Function that handles age validation
    def handle_age_input(self, question):
        while True:
            answer = input(colored(question + "\n", "green"))
            try:
                age = int(answer)
                if 18 <= age <= 122:  # A reasonable age range
                    self.answers.append(str(age))
                    break
                else:
                    error_message = "Please provide a valid age."
                    print(colored(error_message, "red"))
            except ValueError:
                error_message = "Please provide a valid age."
                print(colored(error_message, "red"))

    # Function that contains the survey questions and adds answers to the list
    def conduct_survey(self):
        self.answers = []
        welcome_message = "Welcome to the survey!"
        print(colored(welcome_message, "blue"))
        self.add_timestamp()

        for i, question in enumerate(
            column_mapping.keys()
        ):  # looping through column_mapping list
            if question == "What is your name?":
                self.handle_name_input(question)

            elif question == "How old are you?":
                self.handle_age_input(question)

            elif question == "Please select your career area:":
                # Handle career area selection using TerminalMenu
                career_area_menu = TerminalMenu(
                    self.career_areas, title=question
                )
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

            elif question == "What factors influenced your decision?":
                # Handle single choice question using TerminalMenu
                factor_menu = TerminalMenu(
                    self.career_change_factors, title=question
                )
                selected_index = factor_menu.show()
                selected_factor = self.career_change_factors[selected_index]
                answer = self.career_change_factors[selected_index]
                self.answers.append(answer)

            elif question == "Do you prefer remote work? (yes/no)":
                # Handle yes/no question using TerminalMenu
                yes_no_menu = TerminalMenu(["yes", "no"], title=question)
                selected_index = yes_no_menu.show()
                answer = ["yes", "no"][selected_index]
                self.answers.append(answer)

        thank_you_message = "Thank you for completing the survey!"
        print(colored(thank_you_message, "blue"))

    # Store results in googlesheet
    def store_results_in_google_sheet(self):
        try:
            SHEET = get_google_sheet_client()
            worksheet = SHEET.get_worksheet(0)
            values = [self.answers]
            worksheet.append_rows(values)
            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    # Display the results at the end of the survey
    def display_results(self):
        survey_results_message = colored("Survey Results:", "blue")
        print(survey_results_message)

        for question, answer in zip(
            column_mapping.keys(), self.answers[1:]
        ):  # pair answers to questions
            question_colored = colored(question, "green")
            answer_colored = colored(answer, "yellow")
            print(f"{question_colored}\n- Answer: {answer_colored}\n")
            print("-" * 40)
