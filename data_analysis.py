from survey import get_google_sheet_client, column_mapping
import time  # For display statistics timeout
from termcolor import colored  # Adds colored text and emoji support

SHEET = get_google_sheet_client(
    creds_file="creds.json", sheet_name="career_analyzer"
)

"""
Dictionary list that assigns colors for bar charts
"""
answer_color_mapping = {
    "Healthcare": "🟥",
    "Technology": "🟧",
    "Finance": "🟨",
    "Education": "🟩",
    "Unsatisfied": "🟥",
    "Unhappy": "🟧",
    "Somewhat Satisfied": "🟨",
    "Happy": "🟩",
    "Dreamjob": "🟦",
    "Company culture": "🟥",
    "Salary": "🟧",
    "Work-life balance": "🟨",
    "Other": "🟩",
    "Location": "🟦",
    "Opportunities for growth": "🟪",
    "yes": "🟩",
    "no": "🟥",
}


class DataAnalyzer:
    """Class that contains statistics logic creates bar charts"""

    def __init__(self, column_mapping):
        self.column_mapping = column_mapping

    def view_survey_statistics(self):
        """Calculate and display statistics based on survey data."""
        try:
            worksheet = SHEET.get_worksheet(0)
            data = worksheet.get_all_records()

            """
            Count timestamps and survey responses
            Reset variable
            Loop through Timestamp data
            Map to spreadsheet row
            Check if entry is timestamp
            Add data
            Count timestamps
            Print survey count
            Print empty line
            """
            unique_timestamps = set()
            for row in data:
                timestamp = row["Timestamp"]
                if timestamp.startswith("20"):
                    unique_timestamps.add(timestamp)
            survey_count = len(unique_timestamps)
            survey_count_text = colored(
                f"Count of Surveys: {survey_count}", "cyan"
            )
            print(survey_count_text)
            print()
            time.sleep(1)

            """
            Average age calculation
            Can age be converted to integer
            All of the ages added together
            Number of entries into the age column
            Total sum of ages divided by total entries
            Print avg age
            Print empty line
            Delay by 1 sec
            """
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
                avg_age_text = colored(
                    f"Average Age of Survey Participant: {average_age:.2f}",
                    "green",
                )
                print(avg_age_text)
                print()
                time.sleep(1)

            """
            Extract data from the Google Spreadsheet using column_mapping
            Ensure it's a string
            Remove extra spaces
            Get the index of the current question_column
            Print header text 
            Print empty line
            """
            question_columns = list(self.column_mapping.values())[2:]
            for question_column in question_columns:
                answer_counts = {}
                total_responses = len(data)
                for row in data:
                    answer = row[question_column]
                    if isinstance(answer, str):
                        answer = answer.strip()
                        if answer in answer_counts:
                            answer_counts[answer] += 1
                        else:
                            answer_counts[answer] = 1

                column_index = list(self.column_mapping.values()).index(
                    question_column
                )

                """Get the corresponding question title from column_mapping"""
                question_title = list(self.column_mapping.keys())[
                    column_index
                ]

                """Print the question before creating the bar chart"""
                header_text = colored(
                    f"Statistics for Question: {question_title}", "cyan"
                )
                print(header_text)
                print()

                """Prepare data for the bar chart"""
                chart_data = []
                for answer, count in answer_counts.items():
                    percentage = (count / total_responses) * 100
                    chart_data.append(
                        (f"{answer} ({percentage:.2f}%)", count)
                    )

                    """Find the longest label length for alignment"""
                    longest_label_length = max(
                        len(label) for label, _ in chart_data
                    )

                """ 
                Idea for this taken from:
                # https://alexwlchan.net/2018/ascii-bar-charts/
                """

                for label, count in chart_data:
                    """Calculate the percentage and prepare the label"""
                    percentage = (count / total_responses) * 100
                    formatted_label = f"{label:<{longest_label_length}}"

                    """Calculate the number of blocks and spaces needed"""
                    bar_blocks = int((percentage / 100) * 40)
                    space_blocks = 10 - bar_blocks

                    """
                    Get the appropriate colored block or emoji for the answer
                    Get the first word of the label (answer)
                    Default to blue block
                    Draw the bar with colored blocks or emojis and spaces
                    Delay for 2 seconds
                    """
                    answer = label.split()[0]
                    answer_color = answer_color_mapping.get(answer, "🟦")

                    bar = answer_color * bar_blocks
                    space = " " * space_blocks

                    formatted_label = f"{label:<{longest_label_length}}"
                    print(
                        f"{formatted_label} ▏ {count:#4d} {bar}{space}"
                    )
                print()
                time.sleep(2)

        except Exception as e:
            error_message = colored(
                f"Error analyzing survey data: {str(e)}", "red"
            )
            print(error_message)
