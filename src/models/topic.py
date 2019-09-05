class Topic:
    def __init__(self, section, name):
        self.name = name.split('.')[0]
        self.fqdn = '{}/{}'.format(section, name)