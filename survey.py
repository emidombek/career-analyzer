import datetime  # Imports built in datetime module
from constants import Colors  # Import colors class from constants module
import gspread  # Imports Google sheets API
from google.oauth2.service_account import (
    Credentials,
)  # Imports Google service account Credentials


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
    "If yes, what factors are influencing your decision?": "ChangeFactors",
    "Do you prefer remote work? (yes/no)": "RemoteWorkPreference",
}


# Survey class that runs the survey
class Survey:
    def __init__(self):
        self.questions = [
            "What is your name?",
            "How old are you?",
            "Please select your career area:",
            "On a scale of 1 to 5, how satisfied are you with your career?",
            "Are you considering a career change? (yes/no)",
            "If yes, what factors are influencing your decision?",
            "Do you prefer remote work? (yes/no)",
        ]
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
        self.answers = []  # Reset the answers list
        print(Colors.OKBLUE + "Welcome to the survey!" + Colors.ENDC)
        self.add_timestamp()
        for i, question in enumerate(self.questions):
            if i == 0:  # What is your name?
                while True:
                    answer = input(Colors.OKGREEN + f"{question} \n" + Colors.ENDC)
                    if answer.strip():  # Check if not empty
                        self.answers.append(answer)
                        break
                    else:
                        print(
                            Colors.FAIL + "Please provide a valid name." + Colors.ENDC
                        )

            elif i == 1:  # How old are you?
                while True:
                    answer = input(Colors.OKGREEN + f"{question} \n" + Colors.ENDC)
                    try:
                        age = int(answer)
                        if 0 <= age <= 120:  # A reasonable age range
                            self.answers.append(str(age))
                            break
                        else:
                            print(
                                Colors.FAIL
                                + "Please provide a valid age."
                                + Colors.ENDC
                            )
                    except ValueError:
                        print(Colors.FAIL + "Please provide a valid age." + Colors.ENDC)

            elif i == 2:  # Please select your career area
                while True:
                    print(
                        Colors.OKGREEN + f"{question} (Select a number)" + Colors.ENDC
                    )
                    for idx, area in enumerate(self.career_areas, start=1):
                        print(Colors.WARNING + f"{idx}. {area}" + Colors.ENDC)
                    choice = input("Your choice: \n")
                    try:
                        choice_idx = int(choice) - 1
                        if 0 <= choice_idx < len(self.career_areas):
                            answer = self.career_areas[choice_idx]
                            self.answers.append(answer)
                            break
                        else:
                            print(
                                Colors.FAIL
                                + "Please provide a valid choice."
                                + Colors.ENDC
                            )
                    except ValueError:
                        print(
                            Colors.FAIL + "Please provide a valid choice." + Colors.ENDC
                        )

            elif (
                i == 3
            ):  # On a scale of 1 to 5, how satisfied are you with your career?
                while True:
                    print(Colors.OKGREEN + f"{question}" + Colors.ENDC)
                    for idx, rating in enumerate(
                        self.career_satisfaction_ratings, start=1
                    ):
                        print(Colors.WARNING + f"{idx}. {rating}" + Colors.ENDC)
                    answer = input("Your choice: \n")
                    try:
                        rating_idx = int(answer) - 1
                        if 0 <= rating_idx < len(self.career_satisfaction_ratings):
                            answer = self.career_satisfaction_ratings[rating_idx]
                            self.answers.append(answer)
                            break
                        else:
                            print(
                                Colors.FAIL
                                + "Please provide a valid rating choice."
                                + Colors.ENDC
                            )
                    except ValueError:
                        print(
                            Colors.FAIL
                            + "Please provide a valid rating choice."
                            + Colors.ENDC
                        )

            elif i == 4:  # Are you considering a career change? (yes/no)
                while True:
                    answer = input(
                        Colors.OKGREEN + f"{question} \n" + Colors.ENDC
                    ).lower()
                    if answer == "yes" or answer == "no":
                        self.answers.append(answer)
                        break
                    else:
                        print(
                            Colors.FAIL
                            + "Please provide a valid choice (yes or no)."
                            + Colors.ENDC
                        )

            elif i == 5:  # If yes, what factors are influencing your decision?
                while True:
                    print(
                        Colors.OKGREEN
                        + f"{question} (Select numbers separated by space)"
                        + Colors.ENDC
                    )
                    for idx, factor in enumerate(self.career_change_factors, start=1):
                        print(Colors.WARNING + f"{idx}. {factor}" + Colors.ENDC)
                    choices = input("Your choice(s): \n").split()
                    selected_factors = []
                    valid_choices = set(
                        str(idx)
                        for idx in range(1, len(self.career_change_factors) + 1)
                    )
                    if all(choice in valid_choices for choice in choices):
                        selected_factors = [
                            self.career_change_factors[int(choice) - 1]
                            for choice in choices
                        ]
                        answer = ", ".join(selected_factors)
                        self.answers.append(answer)
                        break
                    else:
                        print(
                            Colors.FAIL + "Please provide valid choices." + Colors.ENDC
                        )

            elif i == 6:  # Do you prefer remote work? (yes/no)
                while True:
                    answer = input(
                        Colors.OKGREEN + f"{question} \n" + Colors.ENDC
                    ).lower()
                    if answer == "yes" or answer == "no":
                        self.answers.append(answer)
                        break
                    else:
                        print(
                            Colors.FAIL
                            + "Please provide a valid choice (yes or no)."
                            + Colors.ENDC
                        )

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
        for question, answer in zip(self.questions, self.answers[1:]):
            print(
                f"{Colors.OKGREEN}{question}{Colors.ENDC}\n- {Colors.WARNING}Answer: {answer}{Colors.ENDC}\n"
            )
            print("-" * 40)
