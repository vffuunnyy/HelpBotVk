class Command:
    def __init__(self):
        self.commands = {}

    def add(self, foo, isAdmin=False):
        name = foo.__name__
        self.commands[name] = {"isAdmin": isAdmin, "call": foo}

        return foo

    def call(self, name, args):
        return self.commands[name]["call"](args)

    def hasCommand(self, name):
        if name in self.commands:
            return True
        return False

    def handle(self, event):
        pass
