from constants import Colors
from survey import Survey
from data_analysis import DataAnalyzer, column_mapping
from simple_term_menu import TerminalMenu  # Import the TerminalMenu class
import os


def clear_console():  # function to clear the console
    os.system("cls" if os.name == "nt" else "clear")


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
        clear_console()
        survey = Survey()
        survey.conduct_survey()
        survey.store_results_in_google_sheet()
        survey.display_results()

    def view_statistics(self):  # View stats from survey
        clear_console()
        data_analyzer = DataAnalyzer(column_mapping)  # Pass column_mapping here
        data_analyzer.view_survey_statistics()

    def about(self):  # About text
        clear_console()
        about_text = """ 
        Career Analyzer - About 

        This is a Python based terminal programme, 
        that aims to gauge Career Satisfaction and the likelyhood of a career or job change happening as a result. 
        There is an option to complete a survey under 'Take Survey'. 
        The survey asks about job satisfaction and the driving factors behind a potential change in employment 
        as well as preferences in regareds to remote work.
        The data is stored in a google spreadsheet and analyzed.
        Basic statistics such as count of surveys, average age of participant and answer percentages can be viewed via the 'View Statistics' option. 

        Created by Emilia Dombek

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
                clear_console()
                print(Colors.OKGREEN + "Thank You!" + Colors.ENDC)
                print(Colors.OKGREEN + "Goodbye!" + Colors.ENDC)
                break


if __name__ == "__main__":
    app = TerminalMenuApp()
    app.main()
