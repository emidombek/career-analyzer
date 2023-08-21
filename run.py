from survey import Survey
from data_analysis import DataAnalyzer


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

        /$$$$$$                                                                       
       /$$__  $$                                                                      
      | $$  \__/ /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$                       
      | $$      |____  $$ /$$__  $$/$$__  $$ /$$__  $$ /$$__  $$                      
      | $$       /$$$$$$$| $$  \__/ $$$$$$$$| $$$$$$$$| $$  \__/                      
      | $$    $$/$$__  $$| $$     | $$_____/| $$_____/| $$                            
      |  $$$$$$/  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$| $$                            
       \______/ \_______/|__/      \_______/ \_______/|__/                            
        /$$$$$$                      /$$                                              
       /$$__  $$                    | $$                                              
      | $$  \ $$ /$$$$$$$   /$$$$$$ | $$ /$$   /$$ /$$$$$$$$  /$$$$$$   /$$$$$$       
      | $$$$$$$$| $$__  $$ |____  $$| $$| $$  | $$|____ /$$/ /$$__  $$ /$$__  $$      
      | $$__  $$| $$  \ $$  /$$$$$$$| $$| $$  | $$   /$$$$/ | $$$$$$$$| $$  \__/      
      | $$  | $$| $$  | $$ /$$__  $$| $$| $$  | $$  /$$__/  | $$_____/| $$            
      | $$  | $$| $$  | $$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$| $$            
      |__/  |__/|__/  |__/ \_______/|__/ \____  $$|________/ \_______/|__/            
                                         /$$  | $$                                    
                                        |  $$$$$$/                                    
                                         \______/                                     
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
