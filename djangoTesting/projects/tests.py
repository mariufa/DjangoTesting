from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from .models import Project

class ProjectsTests(TestCase):

    def setUp(self):
        """
        Setup a test project.
        """
        self.testProject = Project(title = "test title", description = "test description")
        self.testProject.save()

    def testIndexView(self):
        """
        Test to see if the index view for projects are loaded.
        """
        response = self.client.get(reverse('projects:index'))
        statusCodeOk = 200
        self.assertEqual(response.status_code, statusCodeOk)

    def testNewProjectIntoDb(self):
        """
        Check if number of projects larger than one.
        A test project should be added in setUp() and deleted in tearDown()
        """
        numProjects = len(Project.objects.all())
        leastNumProjects = 1
        self.assertGreaterEqual(numProjects, leastNumProjects)

    def testOnlyOneProject(self):
        """
        Check to see if only 1 project in db
        """
        numProjects = len(Project.objects.all())
        expectedNumbProjects = 1
        self.assertEqual(numProjects, expectedNumbProjects)

    def tearDown(self):
        """
        Delete test project from db. This might be unnecessary since this is only a test db.
        """
        self.testProject.delete()
