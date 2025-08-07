from django.test import TestCase
from .forms import QuestionCreateForm


# only need to test the createform as both it and the edit forms are identical
# bar a couple of html classes
# i also know the dates update correctly from manual testing
class TestCreateForm(TestCase):

    # test each field being empty
    def test_title_empty(self):
        create_form = QuestionCreateForm({"title": "",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": 1,
                                          "approved": 0})
        self.assertTrue(create_form.is_valid(), msg="Title Empty")

    def test_summary_empty(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "",
                                          "content": "ValidContent",
                                          "difficulty": 1,
                                          "approved": 0})
        self.assertTrue(create_form.is_valid(), msg="Summary Empty")

    def test_content_empty(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "ValidSummary",
                                          "content": "",
                                          "difficulty": 1,
                                          "approved": 0})
        self.assertTrue(create_form.is_valid(), msg="Content Empty")   

    def test_difficulty_empty(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": "",
                                          "approved": 0})
        self.assertTrue(create_form.is_valid(), msg="Difficulty Empty")

    def test_approved_empty(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": 1,
                                          "approved": ""})
        self.assertTrue(create_form.is_valid(), msg="Approved Empty")

    # test title and summary being too long
    def test_title_too_long(self):
        create_form = QuestionCreateForm({"title": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": 1,
                                          "approved": 1})
        self.assertTrue(create_form.is_valid(), msg="Title Too Long")

    def test_summary_too_long(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "content": "ValidContent",
                                          "difficulty": 1,
                                          "approved": 1})
        self.assertTrue(create_form.is_valid(), msg="Summary Too Long")    

    # test setting difficulty and status to invalid values
    def test_difficulty_invalid(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": "-1",
                                          "approved": 0})
        self.assertTrue(create_form.is_valid(), msg="Difficulty Invalid")

    def test_approved_invalid(self):
        create_form = QuestionCreateForm({"title": "ValidTitle",
                                          "summary": "ValidSummary",
                                          "content": "ValidContent",
                                          "difficulty": "1",
                                          "approved": 2})
        self.assertTrue(create_form.is_valid(), msg="Approved Invalid")
