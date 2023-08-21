from constants import Colors
from survey import Survey
from data_analysis import DataAnalyzer
from simple_term_menu import TerminalMenu  # Import the TerminalMenu class


class TerminalMenuApp:
    def __init__(self):
        self.menu_items = [
            "Take the Survey",
            "View Survey Result Statistics",
            "About",
            "Exit",
        ]
        self.menu = TerminalMenu(self.menu_items)

    def take_survey(self):  # Runs survey
        survey = Survey()
        survey.conduct_survey()
        survey.store_results_in_google_sheet()
        survey.display_results()

    def view_statistics(self):  # View stats from survey
        data_analyzer = DataAnalyzer()
        data_analyzer.view_survey_statistics()

    def about(self):  # About with placeholder text will be changed later
        about_text = """ 
        Career Analyzer - Terminal Menu

        This program allows you to take a survey about your career and view statistics
        about the survey results.

        Created by Your Name 

        """
        print(Colors.OKBLUE + about_text + Colors.ENDC)

    def main(self):
        while True:
            selected_index = self.menu.show()

            if selected_index == 0:
                self.take_survey()
            elif selected_index == 1:
                self.view_statistics()
            elif selected_index == 2:
                self.about()
            elif selected_index == 3:
                print(Colors.OKGREEN + "Thank You!" + Colors.ENDC)
                print(Colors.OKGREEN + "Goodbye!" + Colors.ENDC)
                break


if __name__ == "__main__":
    app = TerminalMenuApp()
    app.main()
