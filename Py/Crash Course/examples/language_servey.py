from examples.survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousServey
question = "What language did you first learn to speck?"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранения ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Вывод результатов опроса.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()