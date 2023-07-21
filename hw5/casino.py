import random

class Casino:

    def __init__(self, slot_numbers):
        self.slot_numbers = slot_numbers

    def play(self):
        win_slot = random.choice(self.slot_numbers)
        return win_slot