from survey import get_google_sheet_client, column_mapping
from termcolor import colored

SHEET = get_google_sheet_client(creds_file="creds.json", sheet_name="career_analyzer")

# Emoji definitions
BORDER = "□"
BAR = "🟦"


class DataAnalyzer:  # Class that analyzes survey data stored in the googlespread
    def __init__(self, column_mapping):
        self.column_mapping = column_mapping

    def view_survey_statistics(self):
        try:
            worksheet = SHEET.get_worksheet(0)
            data = worksheet.get_all_records()

            # Count timestamps and survey responses
            unique_timestamps = set()  # Reset variable
            for row in data:  # Loop through Timestamp data
                timestamp = row["Timestamp"]  # Map to spreadsheet row
                if timestamp.startswith("20"):  # Check if entry is timestamp
                    unique_timestamps.add(timestamp)  # Add data
            survey_count = len(unique_timestamps)  # Count timestamps
            survey_count_text = colored(f"Count of Surveys: {survey_count}", "cyan")
            print(survey_count_text)

            # Average age calculation
            total_age = 0  # Set to 0
            age_count = 0  # Set to 0
            for row in data:  # Loop through survey data defined in column_mapping
                age = row[column_mapping["How old are you?"]]
                try:
                    age = int(age)  # Can age be converted to integer
                    total_age += age  # All of the ages added together
                    age_count += 1  # Number of entries into the age column
                except ValueError:
                    pass

            if (
                age_count > 0
            ):  # Checks entries before performing calculation to avoid divding by zero
                average_age = (
                    total_age / age_count
                )  # Total sum of ages divided by total entries
                avg_age_text = colored(
                    f"Average Age of Survey Participant: {average_age:.2f}", "green"
                )
                print(avg_age_text)

            # Create bar charts for questions (excluding name and age)
            for i, question in enumerate(column_mapping.keys()):
                if question in column_mapping:
                    column_name = column_mapping[question]
                    answer_counts = {}
                    total_responses = len(data)
                    for row in data:
                        answer = row[column_name]
                        if i == 4 or i == 6:
                            answer = answer.lower()
                        if answer in answer_counts:
                            answer_counts[answer] += 1
                        else:
                            answer_counts[answer] = 1

                    if question not in ["What is your name?", "How old are you?"]:
                        header_text = colored(
                            f"Statistics for Question: {question}", "cyan"
                        )
                        for answer, count in answer_counts.items():
                            percentage = (count / total_responses) * 100
                            bar_emoji = "🟦" * int(
                                percentage / 10
                            )  # Using a blue square emoji
                            percentage_text = colored(f"({percentage:.2f}%)", "green")
                            print(f"{answer}:{bar} {percentage_text}")
                        print()

        except Exception as e:
            error_message = colored(f"Error analyzing survey data: {str(e)}", "red")
            print(error_message)
