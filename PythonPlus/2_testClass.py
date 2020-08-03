import unittest


class AnonymousSurvey:
    def __init__(self, question_):
        self.question = question_
        self.responseList = []

    def showQuestion(self):
        print(self.question)

    def saveResponse(self, newResponse):
        self.responseList.append(newResponse)

    def showResult(self):
        for resp in self.responseList:
            print('->  ', resp)
        if not self.responseList:
            print('TAT We got nothing')


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):  # 预先创建实例，设置属性
        question = 'What language do you first learn to write'
        self.my_survey = AnonymousSurvey(question)

    def testSaveSingle(self):

        self.my_survey.saveResponse('python')
        self.assertIn('python', self.my_survey.responseList)

    def testSaveMulti(self):
        resp = ['python', 'c', 'c++']
        for re in resp:
            self.my_survey.saveResponse(re)
        for re in resp:
            self.assertIn(re, self.my_survey.responseList)


unittest.main()
