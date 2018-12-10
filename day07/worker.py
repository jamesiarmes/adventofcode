class Worker:
    def __init__(self, id):
        self.id = id
        self.step = None
        self.complete_at = 0

    def work_step(self, step, complete_at):
        step.start()
        self.step = step
        self.complete_at = complete_at

    def is_working(self, time):
        if self.step and self.complete_at > time:
            return True
        elif self.step:
            self.step.complete()

        return False
