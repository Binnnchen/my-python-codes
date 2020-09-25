class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """展示问题"""
        print(self.question)
    
    def store_response(self, response):
        """存储答案"""
        self.responses.append(response)
    
    def show_results(self):
        """显示收集到的所有答案"""
        for response in self.responses:
            print("- "+response)
