import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """测试AnonymousSurvey类"""
    
    def setUp(self):
        """创建实例和一组答案，以供后面测试使用"""
        quesion="What's language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(quesion)
        self.responses=['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """测试单个答案的存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个答案的存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        """
            for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        """
        self.assertEqual(self.responses, self.my_survey.responses)

unittest.main()
    