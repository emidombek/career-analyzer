
class Survey:
    def __init__(self):
        self.questions = [
            "What is your name?",
            "How old are you?",
            "Please select your career area:",
            "On a scale of 1 to 5, how satisfied are you with your career?",
            "Are you considering a career change? (yes/no)",
            "If yes, what factors are influencing your decision? (comma-separated)",
            "Do you prefer remote work? (yes/no)"
        ]
        self.career_areas = ["Technology", "Healthcare", "Finance", "Education", "Other"]
        self.career_change_factors = ["Work-life balance", "Salary", "Opportunities for growth", "Company culture", "Location", "Other"]
        self.answers = []

    def conduct_survey(self):
        print("Welcome to the survey!")
        for i, question in enumerate(self.questions):
            if i == 2:
                print(f"{question} (Select a number)")
                for idx, area in enumerate(self.career_areas, start=1):
                    print(f"{idx}. {area}")
                choice = input("Your choice: ")
                try:
                    choice_idx = int(choice) - 1
                    answer = self.career_areas[choice_idx]
                except (ValueError, IndexError):
                    answer = "Invalid choice"
            else:
                answer = input(f"{question} ")
            self.answers.append(answer)
        print("Thank you for completing the survey!")

    def display_results(self):
        print("Survey Results:")
        for question, answer in zip(self.questions, self.answers):
            print(f"{question}\n- Answer: {answer}\n")

# Create a survey instance
survey = Survey()

# Conduct the survey
survey.conduct_survey()

# Display survey results
survey.display_results()

