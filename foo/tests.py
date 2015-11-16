from django.test import LiveServerTestCase

from foo.models import Actor


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        super(FunctionalTest, self).setUp()
        print("\n##### Actors: %s" % Actor.objects.all())

    def test_b(self):
        print("##### TEST B #####")

    def test_a(self):
        print("##### TEST A #####")
