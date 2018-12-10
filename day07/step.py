class Step:
    STATUS_WAITING = 'waiting'
    STATUS_STARTED = 'started'
    STATUS_COMPLETE = 'complete'

    def __init__(self, id):
        self.id = id
        self.dependencies = []
        self.status = self.STATUS_WAITING

    def __str__(self):
        return self.id

    def complete(self):
        self.status = self.STATUS_COMPLETE

    def start(self):
        self.status = self.STATUS_STARTED

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def is_ready(self):
        for step in self.dependencies:
            if step.status != self.STATUS_COMPLETE:
                return False

        return True


