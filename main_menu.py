from survey import Survey
from data_analysis import DataAnalyzer, column_mapping
from simple_term_menu import (
    TerminalMenu,
)  # Import the TerminalMenu class
import os
from termcolor import colored  # Adds colored text and emoji support


# Function to clear the console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# Class that contains menu logic/about text
class TerminalMenuApp:
    def __init__(self):
        self.menu_items = [
            "Take the Survey",
            "View Survey Result Statistics",
            "About",
            "Exit",
        ]
        self.menu = TerminalMenu(self.menu_items)

    def handle_go_back(self):
        """
        Function to handle user input for going back
        """
        go_back_menu = TerminalMenu(
            ["Back to Main Menu"], title="Go Back"
        )
        selected_index = go_back_menu.show()
        return selected_index == 0

    # Runs survey
    def take_survey(self):
        """
        Function to run sequence of take survey events
        """
        clear_console()
        survey = Survey()
        survey.conduct_survey()
        survey.store_results_in_google_sheet()
        survey.display_results()
        self.handle_go_back()
        clear_console()

    def view_statistics(self):
        """
        Function to run sequence of view statistics events
        """
        clear_console()
        data_analyzer = DataAnalyzer(column_mapping)
        data_analyzer.view_survey_statistics()
        self.handle_go_back()
        clear_console()

    # About text
    def about(self):
        """
        Function to run sequence of about events
        Displays about text
        """
        clear_console()
        about_text = """
        ╔═╗┌─┐┬─┐┌─┐┌─┐┬─┐  ╔═╗┌┐┌┌─┐┬ ┬ ┬┌─┐┌─┐┬─┐
        ║  ├─┤├┬┘├┤ ├┤ ├┬┘  ╠═╣│││├─┤│ └┬┘┌─┘├┤ ├┬┘
        ╚═╝┴ ┴┴└─└─┘└─┘┴└─  ╩ ╩┘└┘┴ ┴┴─┘┴ └─┘└─┘┴└─
        - About
        This is a Python based terminal programme,
        that aims to gauge Career Satisfaction
        and the likelyhood of a career or job change happening as a result.
        There is an option to complete a survey under 'Take Survey'.
        The survey asks about job satisfaction
        and the driving factors behind a potential change in employment
        as well as preferences in regareds to remote work.
        The data is stored in a google spreadsheet and analyzed.
        Basic statistics such as count of surveys,
        average age of participant
        and answer percentages can be viewed via the 'View Statistics' option.
        Created by Emilia Dombek

        """
        print(colored(about_text, "cyan"))
        self.handle_go_back()
        clear_console()

    def main(self):
        """
        Function that contains loops that runs the program
        Displays Text and Main Menu
        Handles Menu selections
        """
        while True:
            print(
                colored(
                    """
Welcome to the Career Analyzer!
  ╔═╗┌─┐┬─┐┌─┐┌─┐┬─┐
  ║  ├─┤├┬┘├┤ ├┤ ├┬┘
  ╚═╝┴ ┴┴└─└─┘└─┘┴└─
  ╔═╗┌┐┌┌─┐┬ ┬ ┬┌─┐┌─┐┬─┐
  ╠═╣│││├─┤│ └┬┘┌─┘├┤ ├┬┘
  ╩ ╩┘└┘┴ ┴┴─┘┴ └─┘└─┘┴└─
""",
                    "blue",
                )
            )
            selected_index = self.menu.show()

            if selected_index == 0:
                self.take_survey()
            elif selected_index == 1:
                self.view_statistics()
            elif selected_index == 2:
                self.about()
            elif selected_index == 3:
                clear_console()
                thank_you_message = colored("Thank You!", "green")
                goodbye_message = colored("Goodbye!", "green")
                print(thank_you_message)
                print(goodbye_message)
                break


# Starts program
if __name__ == "__main__":
    app = TerminalMenuApp()
    app.main()
