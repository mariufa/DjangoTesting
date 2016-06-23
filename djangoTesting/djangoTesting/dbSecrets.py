
class DbSecrets():

    def __init__(self, filename):
        self.filename = filename
        self.dbInfo = {
            'dbName': '',
            'dbUser': '',
            'dbPassword': ''
        }

    def loadSecrets(self):
        secretFile = open(self.filename, 'r')
        for line in secretFile:
            line = line.strip().split(':')
            key = line[0]
            value = line[1]
            self.dbInfo[key] = value
        secretFile.close()
