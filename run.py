import gspread
from google.oauth2.service_account import Credentials
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

column_mapping = {
    "What is your name?": "Name",
    "How old are you?": "Age",
    "Please select your career area:": "CareerType",
    "On a scale of 1 to 5, how satisfied are you with your career?": "CareerSatisfaction",
    "Are you considering a career change? (yes/no)": "ConsideringChange",
    "If yes, what factors are influencing your decision?": "ChangeFactors",
    "Do you prefer remote work? (yes/no)": "RemoteWorkPreference",
}


# ANSI color codes
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def display_welcome():
    welcome_text = """
    Welcome to the Career Analyzer!                                                                                                      
          ,----..                                                                                        
         /   /   \                                                                                       
        |   :     :             __  ,-.                    __  ,-.                                       
        .   |  ;. /           ,' ,'/ /|                  ,' ,'/ /|                                       
        .   ; /--`   ,--.--.  '  | |' | ,---.     ,---.  '  | |' |                                       
        ;   | ;     /       \ |  |   ,'/     \   /     \ |  |   ,'                                       
        |   : |    .--.  .-. |'  :  / /    /  | /    /  |'  :  /                                         
        .   | '___  \__\/: . .|  | ' .    ' / |.    ' / ||  | '                                          
        '   ; : .'| ," .--.; |;  : | '   ;   /|'   ;   /|;  : |                                          
        '   | '/  :/  /  ,.  ||  , ; '   |  / |'   |  / ||  , ;                                          
        |   :    /;  :   .'   \---'  |   :    ||   :    | ---'                                           
         \   \ .' |  ,     .-./       \   \  /  \   \  /                                                 
          `---`    `--`---'            `----'    `----'                                                  
           ,---,                                ,--,                                                     
          '  .' \                             ,--.'|                                                     
         /  ;    '.          ,---,            |  | :                    ,----,            __  ,-.        
        :  :       \     ,-+-. /  |           :  : '                  .'   .`|          ,' ,'/ /|        
        :  |   /\   \   ,--.'|'   |  ,--.--.  |  ' |        .--,   .'   .'  .'   ,---.  '  | |' |        
        |  :  ' ;.   : |   |  ,"' | /       \ '  | |      /_ ./| ,---, '   ./   /     \ |  |   ,'        
        |  |  ;/  \   \|   | /  | |.--.  .-. ||  | :   , ' , ' : ;   | .'  /   /    /  |'  :  /          
        '  :  | \  \ ,'|   | |  | | \__\/: . .'  : |__/___/ \: | `---' /  ;--,.    ' / ||  | '           
        |  |  '  '--'  |   | |  |/  ," .--.; ||  | '.'|.  \  ' |   /  /  / .`|'   ;   /|;  : |           
        |  :  :        |   | |--'  /  /  ,.  |;  :    ; \  ;   : ./__;     .' '   |  / ||  , ;           
        |  | ,'        |   |/     ;  :   .'   \  ,   /   \  \  ; ;   |  .'    |   :    | ---'            
        `--''          '---'      |  ,     .-./---`-'     :  \  \`---'         \   \  /                  
                                   `--`---'                \  ' ;               `----'                   
                                                            `--`                                         
    """
    print(Colors.OKBLUE + welcome_text + Colors.ENDC)


def display_main_menu():
    border = "*" * 40  # Creating a border line
    print(Colors.BOLD + Colors.HEADER + "\nMain Menu:" + Colors.ENDC)
    print(border)  # Print the top border line
    print(Colors.OKBLUE + "1. " + Colors.OKGREEN + "Take the Survey" + Colors.ENDC)
    print(
        Colors.OKBLUE
        + "2. "
        + Colors.OKGREEN
        + "View Survey Result Statistics"
        + Colors.ENDC
    )
    print(Colors.OKBLUE + "3. " + Colors.OKGREEN + "Exit" + Colors.ENDC)
    print(border)  # Print the bottom border line


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

    def store_results_in_google_sheet(self):
        try:
            worksheet = SHEET.get_worksheet(0)
            values = [self.answers]
            worksheet.append_rows(values)
            print("Survey results stored in Google Sheet.")
        except Exception as e:
            print("Error storing survey results:", str(e))

    def display_results(self):
        print(Colors.OKBLUE + "Survey Results:" + Colors.ENDC)
        for question, answer in zip(self.questions, self.answers[1:]):
            print(
                f"{Colors.OKGREEN}{question}{Colors.ENDC}\n- {Colors.WARNING}Answer: {answer}{Colors.ENDC}\n"
            )
            print("-" * 40)

    def view_survey_statistics(self):
        try:
            worksheet = SHEET.get_worksheet(0)
            data = worksheet.get_all_records()

            # Count unique timestamps and survey responses
            unique_timestamps = set()
            for row in data:
                timestamp = row["Timestamp"]
                if timestamp.startswith("20"):
                    unique_timestamps.add(timestamp)
            survey_count = len(unique_timestamps)
            print(f"\n{Colors.HEADER}Count of Surveys: {survey_count}{Colors.ENDC}")

            total_age = 0
            age_count = 0
            for row in data:
                age = row[column_mapping["How old are you?"]]
                try:
                    age = int(age)
                    total_age += age
                    age_count += 1
                except ValueError:
                    pass

            if age_count > 0:
                average_age = total_age / age_count
                print(f"{Colors.OKGREEN}Average Age: {average_age:.2f}{Colors.ENDC}")

            # Create bar charts for questions (excluding name and age)
            for i, question in enumerate(self.questions):
                if question in column_mapping:
                    column_name = column_mapping[question]
                    answer_counts = {}
                    total_responses = len(data)
                    for row in data:
                        answer = row[column_name]
                        if i == 4 or i == 6:
                            answer = answer.lower()
                        if answer in answer_counts:
                            answer_counts[answer] += 1
                        else:
                            answer_counts[answer] = 1

                    if question not in ["What is your name?", "How old are you?"]:
                        print(
                            f"\n{Colors.HEADER}Statistics for Question: {question}{Colors.ENDC}"
                        )
                        for answer, count in answer_counts.items():
                            percentage = (count / total_responses) * 100
                            bar = "#" * int(percentage)
                            print(
                                f"{Colors.OKBLUE}{answer}:{Colors.OKGREEN} {bar} ({percentage:.2f}%)"
                            )
                        print()

        except Exception as e:
            print(f"{Colors.FAIL}Error analyzing survey data: {str(e)}{Colors.ENDC}")

    @staticmethod
    def main():
        display_welcome()
        survey = Survey()
        while True:
            display_main_menu()
            choice = input(Colors.BOLD + "Enter your choice: \n" + Colors.ENDC)

            if choice == "1":
                survey.conduct_survey()
                survey.store_results_in_google_sheet()
                survey.display_results()
            elif choice == "2":
                survey.view_survey_statistics()
            elif choice == "3":
                print(Colors.OKGREEN + "Goodbye!" + Colors.ENDC)
                break
            else:
                print(
                    Colors.FAIL
                    + "Invalid choice. Please select a valid option."
                    + Colors.ENDC
                )


if __name__ == "__main__":
    Survey.main()
