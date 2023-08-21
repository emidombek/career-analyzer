from constants import Colors
from survey import Survey
from data_analysis import DataAnalyzer


class TerminalMenu:
    def display_menu(self):
        print("\n" + Colors.HEADER + "Welcome to the Career Analyzer!" + Colors.ENDC)
        print("1. " + Colors.OKGREEN + "Take the Survey" + Colors.ENDC)
        print("2. " + Colors.OKGREEN + "View Survey Result Statistics" + Colors.ENDC)
        print("3. " + Colors.OKGREEN + "About" + Colors.ENDC)
        print("4. " + Colors.OKGREEN + "Exit" + Colors.ENDC)

    def take_survey(self):
        survey = Survey()
        survey.conduct_survey()
        survey.store_results_in_google_sheet()
        survey.display_results()

    def view_statistics(self):
        data_analyzer = DataAnalyzer()
        data_analyzer.view_survey_statistics()

    def about(self):
        about_text = """
        Career Analyzer - Terminal Menu

        This program allows you to take a survey about your career and view statistics
        about the survey results.

        Created by Your Name

        """
        print(Colors.OKBLUE + about_text + Colors.ENDC)

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.take_survey()
            elif choice == "2":
                self.view_statistics()
            elif choice == "3":
                self.about()
            elif choice == "4":
                print(Colors.OKGREEN + "Goodbye!" + Colors.ENDC)
                break
            else:
                print(
                    Colors.FAIL
                    + "Invalid choice. Please select a valid option."
                    + Colors.ENDC
                )


if __name__ == "__main__":
    menu = TerminalMenu()
    menu.main()
