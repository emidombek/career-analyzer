from constants import Colors  # import colors class from constants module
from collections import column_mapping
from survey import get_google_sheet_client

SHEET = get_google_sheet_client(creds_file="creds.json", sheet_name="career_analyzer")


class DataAnalyzer:
    def __init__(self, column_mapping):
        self.column_mapping = column_mapping

    def view_survey_statistics(self):
        try:
            worksheet = SHEET.get_worksheet(0)
            data = worksheet.get_all_records()

            # Count unique timestamps and survey responses
            unique_timestamps = set()
            for row in data:
                timestamp = row["Timestamp"]
                if timestamp.startswith("20"):
                    unique_timestamps.add(timestamp)
            survey_count = len(unique_timestamps)
            print(f"\n{Colors.HEADER}Count of Surveys: {survey_count}{Colors.ENDC}")

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
                print(f"{Colors.OKGREEN}Average Age: {average_age:.2f}{Colors.ENDC}")

            # Create bar charts for questions (excluding name and age)
            for i, question in enumerate(self.questions):
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
                        print(
                            f"\n{Colors.HEADER}Statistics for Question: {question}{Colors.ENDC}"
                        )
                        for answer, count in answer_counts.items():
                            percentage = (count / total_responses) * 100
                            bar = "#" * int(percentage)
                            print(
                                f"{Colors.OKBLUE}{answer}:{Colors.OKGREEN} {bar} ({percentage:.2f}%)"
                            )
                        print()

        except Exception as e:
            print(f"{Colors.FAIL}Error analyzing survey data: {str(e)}{Colors.ENDC}")
