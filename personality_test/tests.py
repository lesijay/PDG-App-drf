from django.test import TestCase

# Create your tests here.
class SampleTest(TestCase):
    def test_that_the_app_is_working(self):
        response = 1+1
        self.assertEqual(response, 2)
 