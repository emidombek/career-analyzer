from survey import get_google_sheet_client, column_mapping
from termcolor import colored

SHEET = get_google_sheet_client(creds_file="creds.json", sheet_name="career_analyzer")

answer_color_mapping = {
    "Healthcare": "🟥",
    "Technology": "🟧",
    "Finance": "🟨",
    "Education": "🟩",
    "Other": "🟦",
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
            # Print empty line
            print()

            # Average age calculation
            total_age = 0  # Set to 0
            age_count = 0  # Set to 0
            for row in data:
                age = row[column_mapping["How old are you?"]]
                try:
                    age = int(age)  # Can age be converted to integer
                    total_age += age  # All of the ages added together
                    age_count += 1  # Number of entries into the age column
                except ValueError:
                    pass

            if age_count > 0:
                average_age = (
                    total_age / age_count
                )  # Total sum of ages divided by total entries
                avg_age_text = colored(
                    f"Average Age of Survey Participant: {average_age:.2f}", "green"
                )
                print(avg_age_text)
                # Print empty line
                print()

            # Extract data from the Google Spreadsheet using column_mapping
            question_columns = list(self.column_mapping.values())[2:]
            for question_column in question_columns:
                answer_counts = {}
                total_responses = len(data)
                for row in data:
                    answer = row[question_column]
                    if isinstance(answer, str):  # Ensure it's a string
                        answer = answer.strip()  # Remove extra spaces
                        if answer in answer_counts:
                            answer_counts[answer] += 1
                        else:
                            answer_counts[answer] = 1

                # Get the index of the current question_column
                column_index = list(self.column_mapping.values()).index(question_column)

                # Get the corresponding question title from column_mapping
                question_title = list(self.column_mapping.keys())[column_index]

                # Print the question before creating the bar chart
                header_text = colored(
                    f"Statistics for Question: {question_title}", "cyan"
                )
                print(header_text)
                # Print empty line
                print()

                # Prepare data for the bar chart
                chart_data = []
                for answer, count in answer_counts.items():
                    percentage = (count / total_responses) * 100
                    chart_data.append((f"{answer} ({percentage:.2f}%)", count))

                    # Find the longest label length for alignment
                    longest_label_length = max(len(label) for label, _ in chart_data)

                """
                Idea for this taken from:
                https://alexwlchan.net/2018/ascii-bar-charts/
                """
                for label, count in chart_data:
                    # Calculate the percentage and prepare the label
                    percentage = (count / total_responses) * 100
                    formatted_label = f"{label:<{longest_label_length}}"

                    # Calculate the number of blocks and spaces needed
                    bar_blocks = int((percentage / 100) * 40)
                    space_blocks = 10 - bar_blocks

                    # Get the appropriate colored block or emoji for the answer
                    answer = label.split()[
                        0
                    ]  # Get the first word of the label (answer)
                    answer_color = answer_color_mapping.get(
                        answer, "🟦"
                    )  # Default to blue block

                    # Draw the bar with colored blocks or emojis and spaces
                    bar = answer_color * bar_blocks
                    space = " " * space_blocks

                    formatted_label = f"{label:<{longest_label_length}}"
                    print(f"{formatted_label} ▏ {count:#4d} {bar}{space}")
                print()

        except Exception as e:
            error_message = colored(f"Error analyzing survey data: {str(e)}", "red")
            print(error_message)
