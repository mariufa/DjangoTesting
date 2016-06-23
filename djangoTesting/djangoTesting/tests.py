from django.test import TestCase
import os
from . import dbSecrets

class DatabaseSecretsTests(TestCase):

    def setUp(self):
        self.dbInfo = {
            'dbName': 'testDb',
            'dbUser': 'testUser',
            'dbPassword': 'testPassword'
        }

        self.testFile = 'testFile.txt'
        self.setupTestFile()
        self.dbSecrets = dbSecrets()
        self.dbSecrets.loadSecrets()

    def setupTestFile(self):
        testFile = open(self.testFile, 'w')
        for key, value in self.dbInfo.items():
            self.writeLine(testFile, key, value)
        testFile.close()

    def writeLine(self, file, key, value):
        file.write(key + ':' + value + '\n')

    def testDbName(self):
        self.assertEqual(self.dbInfo['dbName'], self.dbSecrets.dbInfo['dbName'])

    def testDbUser(self):
        self.assertEqual(self.dbInfo['dbUser'], self.dbSecrets.dbInfo['dbUser'])

    def testDbPassword(self):
        self.assertEqual(self.dbInfo['dbPasword'], self.dbSecrets.dbInfo['dbPassword'])

    def tearDown(self):
        os.remove(self.testFile)
