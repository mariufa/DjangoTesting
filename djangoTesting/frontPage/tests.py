from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class FrontPageTests(TestCase):

    def testIndexView(self):
        response = self.client.get(reverse('frontPage:index'))
        self.assertEqual(response.status_code, 200)
