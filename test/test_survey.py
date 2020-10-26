import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """"""
    def setUp(self):
#测试之前创建的对象
        question = "What's your favoreit language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'chinese', 'python']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()