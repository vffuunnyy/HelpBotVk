class Trigger:
    triggers = {}

    def add(self, name, trigger):
        self.triggers[name] = trigger

    def call(self, name):
        return self.triggers[name]()

    def hasTrigger(self, name):
        if name in self.triggers:
            return True
        return False

    def handle(self, event):
        pass