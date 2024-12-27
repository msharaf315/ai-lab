from schema.base_class import BaseItem
from functools import reduce


class EverdellImage:
    total_score: int

    def __init__(self, items: list[BaseItem], prediction: any):
        self.items = items
        self.prediction = prediction

    def calculate_score(self):
        self.total_score = 0
        for item in self.items:
            self.total_score += item.base_score
        return self.total_score
