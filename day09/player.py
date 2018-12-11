class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0

    def __str__(self):
        return str(self.id)
