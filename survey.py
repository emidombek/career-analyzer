import datetime  # Imports built in datetime module
import time  # For delay on display answers timeout
import gspread  # Imports Google sheets API
from google.oauth2.service_account import (
    Credentials,
)  # Imports Google service account Credentials
from simple_term_menu import TerminalMenu  # Adds selectable menu
from termcolor import colored  # Adds colored text


def get_google_sheet_client(
    creds_file="creds.json", sheet_name="career_analyzer"
):
    """
    Function that defines permission scope,
    credentials location, sheet location
    Example taken from the Love Sandwiches project,
    see readme resources
    """

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
    "How satisfied are you with your career?": "CareerSatisfaction",
    "Are you considering a career change? (yes/no)": "ConsideringChange",
    "What factors influenced your decision?": "ChangeFactors",
    "Do you prefer remote work? (yes/no)": "RemoteWorkPreference",
}


# Survey class that contains survey logic
class Survey:
    def __init__(self):
        # List of answers
        self.career_areas = [
            "Technology",
            "Healthcare",
            "Finance",
            "Education",
            "Other (Question 3)",
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
            "Other (Question 6)",
        ]
        self.answers = []

    def add_timestamp(self):
        """
        Function that retrieves datetime and appends it to the list
        Get current datetime
        Format timestamp
        Append the timestamp to the list
        """
        try:
            timestamp = datetime.datetime.now()
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            self.answers.append(timestamp_str)
            print("Timestamp added to the survey answers.")
        except Exception as e:
            print("Error adding timestamp:", str(e))

    def handle_name_input(self, question):
        """
        Function that handles name input validation
        Check for minimum length 2
        Check for alphabetic characters only
        Capitalize the first letter
        """
        while True:
            answer = input(colored(question + "\n", "green"))

            if len(answer.strip()) < 2:
                error_message = (
                    "Please provide a valid name (2+ characters)."
                )
                print(colored(error_message, "red"))
                continue

            if not all(c.isalpha() or c.isspace() for c in answer):
                error_message = (
                    "Please provide a valid name (letters only)."
                )
                print(colored(error_message, "red"))
                continue

            formatted_name = answer.capitalize()

            self.answers.append(formatted_name)
            break

    def handle_age_input(self, question):
        """
        Function that handles age input validation
        Checks if age in range
        """
        while True:
            answer = input(colored(question + "\n", "green"))
            try:
                age = int(answer)
                if 18 <= age <= 122:  # age range
                    self.answers.append(str(age))
                    break
                else:
                    error_message = "Please provide a valid age."
                    print(colored(error_message, "red"))
            except ValueError:
                error_message = "Please provide a valid age."
                print(colored(error_message, "red"))

    def conduct_survey(self):
        """
        Function that contains survey logic
        Reset answers
        Display welcome
        Add timestamp
        Loop through column_mapping list
        Handle choice questions using TerminalMenu
        Append answers
        Display Thank You
        """
        self.answers = []
        welcome_message = "Welcome to the survey!"
        print(colored(welcome_message, "blue"))
        self.add_timestamp()

        for i, question in enumerate(column_mapping.keys()):
            if question == "What is your name?":
                self.handle_name_input(question)

            elif question == "How old are you?":
                self.handle_age_input(question)

            elif question == "Please select your career area:":
                career_area_menu = TerminalMenu(
                    self.career_areas, title=question
                )
                selected_index = career_area_menu.show()
                answer = self.career_areas[selected_index]
                self.answers.append(answer)

            elif question == "How satisfied are you with your career?":
                satisfaction_menu = TerminalMenu(
                    self.career_satisfaction_ratings, title=question
                )
                selected_index = satisfaction_menu.show()
                answer = self.career_satisfaction_ratings[
                    selected_index
                ]
                self.answers.append(answer)

            elif (
                question
                == "Are you considering a career change? (yes/no)"
            ):
                yes_no_menu = TerminalMenu(
                    ["yes", "no"], title=question
                )
                selected_index = yes_no_menu.show()
                answer = ["yes", "no"][selected_index]
                self.answers.append(answer)

            elif question == "What factors influenced your decision?":
                factor_menu = TerminalMenu(
                    self.career_change_factors, title=question
                )
                selected_index = factor_menu.show()
                selected_factor = self.career_change_factors[
                    selected_index
                ]
                answer = self.career_change_factors[selected_index]
                self.answers.append(answer)

            elif question == "Do you prefer remote work? (yes/no)":
                yes_no_menu = TerminalMenu(
                    ["yes", "no"], title=question
                )
                selected_index = yes_no_menu.show()
                answer = ["yes", "no"][selected_index]
                self.answers.append(answer)

        thank_you_message = "Thank you for completing the survey!"
        print(colored(thank_you_message, "blue"))

    def store_results_in_google_sheet(self):
        """
        Function thats stores answers in google sheet
        Using get_google_sheet_client
        Gets google worksheet
        Maps values to answers
        Appends survey data stored in values
        """
        try:
            SHEET = get_google_sheet_client()
            worksheet = SHEET.get_worksheet(0)
            values = [self.answers]
            worksheet.append_rows(values)
            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    def display_results(self):
        """
        Function that displays results
        Pairs questions and answers
        Assigns different colors
        Displays results
        """
        survey_results_message = colored("Survey Results:", "blue")
        print(survey_results_message)

        for question, answer in zip(
            column_mapping.keys(), self.answers[1:]
        ):
            question_colored = colored(question, "green")
            answer_colored = colored(answer, "yellow")
            print(f"{question_colored}\n- Answer: {answer_colored}\n")
            print("-" * 40)
            # Add a delay between question-answer pairs
            time.sleep(1)
