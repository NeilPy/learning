class AnonymousSurvey:
    """Cбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопросы и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохроняет один ответ на опрос."""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Servey results: ")
        for response in self.responses:
            print('- ' + response)
