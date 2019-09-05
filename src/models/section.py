from os import listdir
from models.topic import Topic

class Section:
    def __init__(self, basepath, name):
        self.name = name
        self.fqdn = '{}/{}'.format(basepath, name)
        self.topics = list()

        for file in listdir(self.fqdn):
            self.topics.append(Topic(self.fqdn, file))