# Career Analyzer Readme 📚
![Devices Preview](#)

[Link to Live Site Here](#)

## 🤔 What is Career Analyzer?

 Welcome to Career Analyzer, a Python-based terminal application designed to help you gauge career satisfaction and assess the likelihood of a career or job change. Whether you're curious about your current job's alignment with your aspirations or considering a shift in your professional journey, Career Analyzer is here to assist.

## ⭐ Purpose and goals of the Application

 - Insightful Self-Assessment: The application's primary goal is to offer users a platform for self-assessment. Through a structured survey, users can evaluate their job satisfaction, identify factors driving potential changes, and express preferences for remote work. This enables users to gain a deeper understanding of their career perspectives.
 - Data-Driven Exploration: Career Analyzer aims to transform survey responses into meaningful insights. By analyzing survey data, the application generates statistical summaries that highlight trends, patterns, and participant demographics. This data-driven approach assists users in making informed decisions and encourages discussions about career satisfaction within the community.

## 🧑 User stories

 - As a professional, I'll use the Career Analyzer to complete the survey, assess my job satisfaction, and analyze statistics for insights.
 - As an individual considering a career change, I'll use the Career Analyzer to evaluate factors driving change and determine if it aligns with my aspirations.
 - To understand my remote work preference, I'll complete the survey and analyze statistics to compare my preference with others.
 - Researching career trends, I'll use the Career Analyzer's data analysis to learn about job satisfaction trends across industries.
 - As a career counselor, I'll recommend the Career Analyzer to clients for self-reflection, growth insights, and career discussions.

## 🗃 Content and Structure

Consists of four main Python files:
 - **run.py**: Entry point, displays welcome message and initializes menu.
 - **main_menu.py**: Defines the main menu structure and functionality.
 - **survey.py**: Conducts the survey and stores responses in Google Sheets.
 - **data_analysis.py**: Analyzes survey data and generates statistical summaries.

  <details>
   <summary>Click here to view a simplified flowchart with an Overview of the Application Content & Structure</summary>
   
   ![Simplified Program Flowchart](#)
  
   </details>

 ### 👾 Features

 **Take the Survey:**
  - Interactive survey covering career satisfaction, change factors, and remote work preference.
  - Responses stored and used for analysis.
  
 **View Survey Result Statistics:**
  - Statistical analysis of survey data, including count, demographics, and response percentages.
  - Displays trends and patterns in career sentiments.

 **About:**
  - Provides an overview of the application's purpose and functionality.
  - Introduces the creator and acknowledges contributions.
  
## 🖥 Technology

 The technology used in this project is as follows:

   - [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) Python is a versatile and high-level programming      language known for its simplicity and readability, suitable for a wide range of applications.
   - [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/p3-template) - GitHub repository template used to create the repository.
   - [Visual Studio Code](https://code.visualstudio.com/) - source code editor used to create, edit and publish the webpages with the assistance of Git/GitHub/GitPages.
   - [Google Sheets](https://www.google.com/sheets/about/) - Google Sheets is a cloud-based spreadsheet application by Google, offering collaborative data management, analysis, and visualization.
   - [Heroku](https://heroku.com/) - Cloud application hosting service.
   - [GitHub](https://github.com/) - Git repository hosting service with a web-based graphical interface.
   - [Google API Client Libraries:](https://developers.google.com/api-client-library)
     - `google-api-core`: Used for interacting with Google APIs and handling authentication.
     - `google-api-python-client`: Provides the Python client library for Google APIs.
     - `google-auth`: Used for authenticating with Google services.
     - `google-auth-httplib2`: Provides HTTP request handling for Google API authentication.
     - `google-auth-oauthlib`: Offers OAuth 2.0 handling for Google API authentication.
   - [GSpread](https://docs.gspread.org/en/v5.10.0/) - A library for working with Google Sheets and Google Drive, used for storing and retrieving survey data.
   - [simple-term-menu](https://pypi.org/project/simple-term-menu/) - Used for creating interactive terminal menus to facilitate user navigation within the application.
   - [termcolor](https://pypi.org/project/termcolor/) - Enables terminal text coloring for enhancing the user interface and readability.
   - [requests](https://pypi.org/project/requests/) - A popular library for making HTTP requests, which may be used for various purposes within the application.
   - [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) - Offers tools for building interactive command-line applications, enhancing user input and interaction.
   - [ipython](https://ipython.readthedocs.io/en/stable/) - Provides an interactive Python shell for a more user-friendly and feature-rich terminal experience.
    - [packaging](https://packaging.python.org/en/latest/) - Used for packaging and distributing Python software, potentially for distribution of your application.

## 🤖 Code

The majority of this program is written in Python 3.11.4 the code is organized into four distinct Python files to enhance modularity, readability, and maintainability. Each file serves a specific purpose, contributing to the overall functionality of the application:

 <details>
   <summary>Click here to view a technical flowchart with an Overview of the Program Content & Structure</summary>
   
   ![Technical Program Flowchart](#)
  
   </details>

 1. 🏃**run.py**: The run.py file serves as the entry point to the Career Analyzer application, initiating the program and orchestrating the overall flow.

    <details>
      <summary>run.py Code Summary</summary>

      <br>

      **Code Summary:**

      - `display_welcome()`: Defines a function to display a formatted welcome message when the program starts, enhancing user experience.
      - `main()`: Defines the main function responsible for running the application
        - Calls `display_welcome()` to show the welcome message.
        - Initializes an instance of `TerminalMenuApp` from `main_menu.py`.
        - Calls the `main()` method of the initialized menu app, which controls the flow of the application based on user selections.
      - `if __name__ == "__main__":` ensures that the code under this condition is executed only when the script is run directly, not when imported as a module.
    
     <br>

     **Loop in `run.py`:**

      - Type of Loop: `while` loop 
      - Description: The loop in `run.py` is implemented using a `while` loop. It runs the main menu of the application and continues until the user selects the "Exit" option. Inside the loop, the user can interact with different menu options.
    
     <br>

      </details>

 2. 📄 **main_menu.py**: The main_menu.py file defines the TerminalMenuApp class, responsible for creating and managing the main menu of the Career Analyzer application.

    <details>
      <summary>main_menu.py Summary</summary>

      <br>
      
      **Code Summary:**

      - `clear_console()`: Defines a function to clear the terminal/console screen, enhancing the user interface.
      - `TerminalMenuApp` class: Defines the main application class.
        - `__init__()`: Initializes the class with menu item options and creates an instance of `TerminalMenu`.
        - `take_survey()`: Initiates the survey process by creating an instance of the `Survey` class from `survey.py`.
        - `view_statistics()`: Invokes data analysis by creating an instance of the `DataAnalyzer` class from `data_analysis.py`.
        - `about()`: Displays an informative `About` text describing the application's purpose and features.
        - `main()`: Main loop that displays the menu and handles user selections, calling the appropriate methods based on the selected option.
      - `if __name__ == "__main__":`: Ensures the main menu is displayed when the script is run directly.
    
     <br>
  
      **Loop in `main_menu.py` (`TerminalMenuApp` class):**

      - Type of Loop: `while` loop
      - Description: The `main()` method of the `TerminalMenuApp` class contains a `while` loop. It continuously displays the main menu and waits for user input. The loop iterates until the user chooses the "Exit" option, allowing navigation through various actions.
    
     <br>
  
      </details>

 3. ✏ **survey.py**: The survey.py file defines the Survey class, responsible for conducting the survey, collecting responses, and storing them in Google Sheets.

    <details>
     <summary>survey.py Summary</summary>

      <br>

      **Code Summary:**

     - `get_google_sheet_client()`: Defines a function to authenticate and obtain a Google Sheets client for data storage.
     - `column_mapping`: Maps survey questions to corresponding columns in the Google Sheets.
     - `Survey` class: Manages the survey process.
       - `__init__()`: Initializes the class with various question options and lists for capturing survey responses.
       - `add_timestamp()`: Records the current timestamp and appends it to the list of responses.
       - `handle_name_input()`: Validates and handles user input for the respondent's name.
       - `handle_age_input()`: Validates and handles user input for the respondent's age.
       - `conduct_survey()`: Guides users through the survey by presenting questions and capturing their responses.
       - `store_results_in_google_sheet()`: Stores the collected survey responses in a Google Sheet.
       - `display_results()`: Displays the captured survey responses to the user.
     - `if __name__ == "__main__":`: Ensures survey logic is executed only when the script is run directly.
  
     <br>

      **Loop in `survey.py` (`Survey` class):**

     - Type of Loop: `for` loop
     - Description: The `conduct_survey()` method of the `Survey` class uses a `for` loop to iterate through the survey questions defined in the `column_mapping` dictionary. The loop prompts the user to answer each question and handles different question types using conditionals.
    
     <br>

     </details>


 4. 📊 **data_analysis.py**: The data_analysis.py file defines the DataAnalyzer class, responsible for analyzing survey data stored in Google Sheets and displaying statistics.

    <details>
     <summary>data_analysis.py Summary</summary>

     <br>

      **Code Summary:**

     - `answer_color_mapping`: Maps survey answer categories to corresponding emoji or symbols for visualization.
     - `SHEET`: Establishes a connection to the Google Sheet containing survey data.
     - `DataAnalyzer` class: Analyzes survey data and displays statistics.
       - `__init__()`: Initializes the class with the `column_mapping` dictionary for mapping columns.
       - `view_survey_statistics()`: Retrieves survey data, calculates and displays statistics for analysis.
     - `if __name__ == "__main__":`: Ensures data analysis logic is executed only when the script is run directly.
    
     <br>

      **Loop in `data_analysis.py` (`DataAnalyzer` class):**

     - Type of Loop: `for` loop
     - Description: The `view_survey_statistics()` method of the `DataAnalyzer` class employs a `for` loop to process survey data and generate statistics for each question in the `column_mapping` dictionary. The loop calculates averages, generates bar charts, and displays response percentages.
     
     The idea for this was taken from [here](https://alexwlchan.net/2018/ascii-bar-charts/). Edited to allow for emojis.
    
     <br>

     </details>

## 🚀 Deployment 

### 📖 Deployment Guide

Follow these steps to deploy the Career Analyzer application on your local machine. These instructions assume you have Python and pip installed. For detailed deployment to a hosting platform like Heroku, refer to the platform's documentation.

 1. Clone the Repository:
    Clone the Career Analyzer repository to your local machine using the following command:
    
    ```sh
    git clone https://github.com/emidombek/career-analyzer.git
    ```
  
 2. Create a Virtual Environment (Optional but Recommended):

    ```sh
    python -m venv career_analyzer_env
    ```

 3. Activate the Virtual Environment:

    On Windows:

    ```sh
    career_analyzer_env\Scripts\activate
    ```

    On macOS/Linux:

    ```sh
    source career_analyzer_env/bin/activate
    ```

 4. Install Dependencies:
    Navigate to the project directory and install the required dependencies:

    ```sh
    cd career-analyzer
    pip3 install -r requirements.txt
    ```

  5. Database Setup:
     To store and manage survey data, the Career Analyzer application utilizes Google Sheets as a simple and accessible database. Follow these steps to set up the Google Sheets integration:

     - Google Sheets Credentials:
        Obtain the necessary credentials to access your Google Sheets. This typically involves creating a service account and obtaining a JSON key file.

     - Configure Environment Variables:
        In the project directory, create a .env file to store your Google Sheets credentials and other configuration data. Ensure you include the required variables to authenticate with the Google Sheets API.

     - Access and Permissions:
        Share the Google Sheets document with the email address associated with your service account. This step ensures the application has the necessary permissions to read and write data.

        With these steps completed, the Career Analyzer application will be able to interact with Google Sheets as a database for storing and retrieving survey data. Don't forget to update the `get_google_sheet_client` function with your credentials and settings in the `survey.py` file.

  6. Run the Application:
     Start the application by running:

      ```sh
      python run.py
      ```

  7. Deployment to Hosting Platform (Optional):
      If you plan to deploy to a hosting platform like Heroku, refer to the platform's documentation for detailed deployment steps.

##  📦 Dependencies

The Career Analyzer application relies on the following external Python libraries and packages. To ensure proper functionality, make sure to install these dependencies in your environment:

 <details>
   <summary>Click here to view a list of Dependencies found in the requirements.txt</summary>

   <br>

   - [appnope==0.1.3](https://pypi.org/project/appnope/)
   - [asttokens==2.2.1](https://pypi.org/project/asttokens/)
   - [backcall==0.2.0](https://pypi.org/project/backcall/)
   - [cachetools==5.3.1](https://pypi.org/project/cachetools/)
   - [certifi==2023.7.22](https://pypi.org/project/certifi/)
   - [charset-normalizer==3.2.0](https://pypi.org/project/charset-normalizer/)
   - [comm==0.1.4](https://pypi.org/project/comm/)
   - [debugpy==1.6.7.post1](https://pypi.org/project/debugpy/)
   - [decorator==5.1.1](https://pypi.org/project/decorator/)
   - [executing==1.2.0](https://pypi.org/project/executing/)
   - [google-api-core==2.11.1](https://pypi.org/project/google-api-core/)
   - [google-api-python-client==2.96.0](https://pypi.org/project/google-api-python-client/)
   - [google-auth==2.22.0](https://pypi.org/project/google-auth/)
   - [google-auth-httplib2==0.1.0](https://pypi.org/project/google-auth-httplib2/)
   - [google-auth-oauthlib==1.0.0](https://pypi.org/project/google-auth-oauthlib/)
   - [googleapis-common-protos==1.60.0](https://pypi.org/project/googleapis-common-protos/)
   - [gspread==5.10.0](https://pypi.org/project/gspread/)
   - [httplib2==0.22.0](https://pypi.org/project/httplib2/)
   - [idna==3.4](https://pypi.org/project/idna/)
   - [ipykernel==6.25.1](https://pypi.org/project/ipykernel/)
   - [ipython==8.14.0](https://pypi.org/project/ipython/)
   - [jedi==0.19.0](https://pypi.org/project/jedi/)
   - [nest-asyncio==1.5.7](https://pypi.org/project/nest-asyncio/)
   - [oauthlib==3.2.2](https://pypi.org/project/oauthlib/)
   - [packaging==23.1](https://pypi.org/project/packaging/)
   - [parso==0.8.3](https://pypi.org/project/parso/)
   - [pexpect==4.8.0](https://pypi.org/project/pexpect/)
   - [pickleshare==0.7.5](https://pypi.org/project/pickleshare/)
   - [platformdirs==3.10.0](https://pypi.org/project/platformdirs/)
   - [prompt-toolkit==3.0.39](https://pypi.org/project/prompt-toolkit/)
   - [protobuf==4.24.0](https://pypi.org/project/protobuf/)
   - [psutil==5.9.5](https://pypi.org/project/psutil/)
   - [ptyprocess==0.7.0](https://pypi.org/project/ptyprocess/)
   - [pure-eval==0.2.2](https://pypi.org/project/pure-eval/)
   - [pyasn1==0.5.0](https://pypi.org/project/pyasn1/)
   - [pyasn1-modules==0.3.0](https://pypi.org/project/pyasn1-modules/)
   - [Pygments==2.16.1](https://pypi.org/project/Pygments/)
   - [pyparsing==3.1.1](https://pypi.org/project/pyparsing/)
   - [python-dateutil==2.8.2](https://pypi.org/project/python-dateutil/)
   - [pyzmq==25.1.1](https://pypi.org/project/pyzmq/)
   - [requests==2.31.0](https://pypi.org/project/requests/)
   - [requests-oauthlib==1.3.1](https://pypi.org/project/requests-oauthlib/)
   - [rsa==4.9](https://pypi.org/project/rsa/)
   - [simple-term-menu==1.6.1](https://pypi.org/project/simple-term-menu/)
   - [six==1.16.0](https://pypi.org/project/six/)
   - [stack-data==0.6.2](https://pypi.org/project/stack-data/)
   - [termcolor==2.3.0](https://pypi.org/project/termcolor/)
   - [tornado==6.3.3](https://pypi.org/project/tornado/)
   - [traitlets==5.9.0](https://pypi.org/project/traitlets/)
   - [uritemplate==4.1.1](https://pypi.org/project/uritemplate/)
   - [urllib3==1.26.16](https://pypi.org/project/urllib3/)
   - [wcwidth==0.2.6](https://pypi.org/project/wcwidth/)
  
   <br>

   </details>

To install these dependencies, you can use the following command:

 ```sh
 pip3 install -r requirements.txt
 ```

## 📝 Testing 



