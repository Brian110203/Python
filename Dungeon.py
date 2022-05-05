class Dungeon:
    def __init__(self, name, description, fighter):
        self.name = name
        self.description = description
        self.fighter = fighter

    def is_completed(self):
        if self.fighter.is_alive():
            return False

        return True
