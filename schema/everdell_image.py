from schema.base_class import BaseItem, Resource
from functools import reduce


class EverdellImage:
    total_score: int

    def __init__(self, items: list[BaseItem],resources: list[Resource], prediction: any):
        self.items = items
        self.prediction = prediction
        self.resources = resources

    def calculate_score(self):
        self.total_score = 0
        explaination = []
        for item in self.items:
            print(f'{item.name}: {item.calculate_score(self.items,self.resources)} \n')
            explaination.append(
                f"{item.name}: {item.calculate_score(self.items,self.resources)}"
            )
            self.total_score += item.calculate_score(self.items,self.resources)
        return self.total_score, explaination
