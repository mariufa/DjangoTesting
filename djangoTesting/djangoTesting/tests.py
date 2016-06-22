from django.test import TestCase
import os
from

class DatabaseSecretsTests(TestCase):

    def setUp(self):
        self.dbInfo = {
            'dbName': 'testDb',
            'dbUser': 'testUser',
            'dbPassword': 'testPassword'
        }

        self.testFile = 'testFile.txt'
        self.setupTestFile()

    def setupTestFile(self):
        testFile = open(self.testFile, 'w')
        for key, value in self.dbInfo.items():
            self.writeLine(testFile, key, value)
        testFile.close()

    def writeLine(self, file, key, value):
        file.write(key + ':' + value + '\n')

    def test

    def tearDown(self):
        os.remove(self.testFile)
