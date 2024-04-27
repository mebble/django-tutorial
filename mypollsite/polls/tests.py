import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Question

# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        q = Question(question_text="Whats your problem man?", pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertIs(q.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        q = Question(question_text="Whats your problem man?", pub_date=timezone.now() - datetime.timedelta(days=1, seconds=1))
        self.assertIs(q.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        q = Question(question_text="Whats your problem man?", pub_date=timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59))
        self.assertIs(q.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    # note that each test case automatically starts with a clean slate. No need to "reset the DB in a beforeeach"

    url = reverse('polls:index')

    def test_no_questions(self):
        response = self.client.get(QuestionIndexViewTest.url)
        self.assertIs(response.status_code, 200)
        self.assertContains(response, "No polls")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


    def test_past_question(self):
        question = create_question("past question", days=-30)
        response = self.client.get(QuestionIndexViewTest.url)
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_future_question(self):
        create_question("past question", days=1) # future question
        response = self.client.get(QuestionIndexViewTest.url)
        self.assertContains(response, "No polls")
        self.assertQuerysetEqual( response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question("past question", days=-30) # past question
        create_question("past question", days=1) # future question
        response = self.client.get(QuestionIndexViewTest.url)
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_two_past_questions(self):
        q1 = create_question("past question", days=-30)
        q2 = create_question("past question", days=-40)
        response = self.client.get(QuestionIndexViewTest.url)
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [q1, q2]
        )

class QuestionDetailViewTest(TestCase):
    url = lambda id: reverse("polls:detail", args=(id,))

    def test_no_question(self):
        response = self.client.get(QuestionDetailViewTest.url(123))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question("What's up?", days=-30)
        response = self.client.get(QuestionDetailViewTest.url(question.id))
        self.assertEqual(response.status_code, 200)

    def test_future_question(self):
        question = create_question("What's up?", days=30)
        response = self.client.get(QuestionDetailViewTest.url(question.id))
        self.assertEqual(response.status_code, 404)
