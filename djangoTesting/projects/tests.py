from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class ProjectsTests(TestCase):

    def testIndexView(self):
        response = self.client.get(reverse('projects:index'))
        statusCodeOk = 200
        self.assertEqual(response.status_code, statusCodeOk)