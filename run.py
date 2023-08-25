from main_menu import TerminalMenuApp
from termcolor import colored


def display_welcome():  # Welcome message
    welcome_text = """
Welcome to the Career Analyzer!
  ╔═╗┌─┐┬─┐┌─┐┌─┐┬─┐
  ║  ├─┤├┬┘├┤ ├┤ ├┬┘
  ╚═╝┴ ┴┴└─└─┘└─┘┴└─
  ╔═╗┌┐┌┌─┐┬ ┬ ┬┌─┐┌─┐┬─┐
  ╠═╣│││├─┤│ └┬┘┌─┘├┤ ├┬┘
  ╩ ╩┘└┘┴ ┴┴─┘┴ └─┘└─┘┴└─
    """
    colored_welcome_text = colored(
        welcome_text, "blue"
    )  # Apply blue color
    print(colored_welcome_text)


def main():  # Runs main function
    display_welcome()  # Display the welcome message
    menu = TerminalMenuApp()
    menu.main()


# Entry point
if __name__ == "__main__":
    main()
