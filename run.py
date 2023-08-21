from main_menu import TerminalMenuApp
from constants import Colors


def display_welcome():  # Welcome message
    welcome_text = """
    Welcome to the Career Analyzer!
                                                                   
     ,-----.                                                       
    '  .--./ ,--,--.,--.--. ,---.  ,---. ,--.--.                   
    |  |    ' ,-.  ||  .--'| .-. :| .-. :|  .--'                   
    '  '--'\\ '-'  ||  |   \   --.\   --.|  |                      
     `-----' `--`--'`--'    `----' `----'`--'                      
      ,---.                  ,--.                                  
     /  O  \ ,--,--,  ,--,--.|  |,--. ,--.,-----. ,---. ,--.--.    
    |  .-.  ||      \' ,-.  ||  | \  '  / `-.  / | .-. :|  .--'    
    |  | |  ||  ||  |\ '-'  ||  |  \   '   /  `-.\   --.|  |       
    `--' `--'`--''--' `--`--'`--'.-'  /   `-----' `----'`--'       
                                 `---'                                 
    """
    print(Colors.OKBLUE + welcome_text + Colors.ENDC)


def main():  # Runs menu
    display_welcome()  # Display the welcome message
    menu = TerminalMenuApp()
    menu.main()


if __name__ == "__main__":
    main()
