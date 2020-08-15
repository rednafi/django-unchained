from django.test import TestCase
from todos.models import Todo

# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", body="a body here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = todo.title
        self.assertEquals(expected_object_name, "first todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = todo.body
        self.assertEquals(expected_object_body, "a body here")
