import gspread
from google.oauth2.service_account import Credentials
import asciichartpy
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")

SCOPED_CREDS = CREDS.with_scopes(
    [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]
)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("career_analyzer")


def display_welcome():
    welcome_text = """
    Welcome to the Career Analyzer!

     ██████╗ █████╗ ██████╗ ███████╗███████╗██████╗      █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
     ██║     ███████║██████╔╝█████╗  █████╗  ██████╔╝    ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
     ██║     ██╔══██║██╔══██╗██╔══╝  ██╔══╝  ██╔══██╗    ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
     ╚██████╗██║  ██║██║  ██║███████╗███████╗██║  ██║    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝                                                                                                                  
    """

    print(welcome_text)


def display_main_menu():
    print("\nMain Menu:")
    print("1. Take the Survey")
    print("2. View Survey Result Statistics")
    print("3. Exit")


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
            self.answers.insert(0, timestamp_str)
            print("Timestamp added to the survey answers.")
        except Exception as e:
            print("Error adding timestamp:", str(e))

    def conduct_survey(self):
        self.answers = []  # Reset the answers list
        print("Welcome to the survey!")
        self.add_timestamp()
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
            elif i == 3:  # Career satisfaction rating
                print("Select satisfaction rating:")
                for idx, factor in enumerate(self.career_satisfaction_ratings, start=1):
                    print(f"{idx}. {factor}")
                choices = input("Your choice(s): ").split()
                selected_factors = []
                try:
                    for choice in choices:
                        choice_idx = int(choice) - 1
                        selected_factors.append(
                            self.career_satisfaction_ratings[choice_idx]
                        )
                    answer = ", ".join(selected_factors)
                except (ValueError, IndexError):
                    answer = "Invalid choice"
            elif i == 5:  # Career change factors question
                print("Select career change factors:")
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
            worksheet = SHEET.get_worksheet(0)
            values = [self.answers]
            worksheet.append_rows(values)
            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    def display_results(self):
        print("Survey Results:")
        for question, answer in zip(self.questions, self.answers):
            print(f"{question}\n- Answer: {answer}\n")

    def display_statistics_as_bars(statistics):
        for question, data in statistics.items():
            print(f"Question: {question}")
            for answer, percentage in data.items():
                bar = "#" * int(percentage)
                print(f"{answer}: {bar} {percentage:.2f}%")
            print()

    def view_survey_statistics(self):
        answer_counts = {}
        total_responses = len(self.answers)
        for answer in self.answers:
            if answer in answer_counts:
                answer_counts[answer] += 1
            else:
                answer_counts[answer] = 1

        percentages = {
            answer: count / total_responses * 100
            for answer, count in answer_counts.items()
        }

        print("\nSurvey Result Statistics:")
        for answer, percentage in percentages.items():
            print(f"{answer}: {'#' * int(percentage)} ({percentage:.2f}%)")

    @staticmethod
    def main():
        display_welcome()
        survey = Survey()
        while True:
            display_main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                survey.add_timestamp()
                survey.conduct_survey()
                survey.store_results_in_google_sheet()
                survey.display_results()
            elif choice == "2":
                survey.view_survey_statistics()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    Survey.main()
