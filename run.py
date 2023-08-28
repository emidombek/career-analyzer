from main_menu import TerminalMenuApp
from termcolor import colored


def display_welcome():
    """Display Welcome message"""
    welcome_text = """
Welcome to the Career Analyzer!
    """
    colored_welcome_text = colored(welcome_text, "blue")
    print(colored_welcome_text)


def main():
    """
    function that defines permission scope,
    credentials location, sheet location
    """
    display_welcome()
    menu = TerminalMenuApp()
    menu.main()


"""Entry point"""
if __name__ == "__main__":
    main()
