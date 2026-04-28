from constants import ASTEROID_SCORE


class Score:
    def __init__(self):
        self.current_score = 0

    def get_score(self):
        return self.current_score

    def add_score(self):
        self.current_score += ASTEROID_SCORE
