from schema.base_class import BaseItem, Resource
from functools import reduce


class EverdellImage:
    total_score: int

    def __init__(
        self,
        prediction: any,
        items: list[BaseItem],
        resources: list[Resource],
    ):
        self.items = []
        [self.add_card(item) for item in items]
        self.prediction = prediction
        self.resources = resources

    def add_card(self, new_card):
        for i, existing_card in enumerate(self.items):
            if existing_card.box.overlaps(new_card.box):  
                print(f"Overlap detected between {existing_card.name} and {new_card.name}.")
                if new_card.confidence > existing_card.confidence:
                    print(f"Replacing card {existing_card.name} (confidence: {existing_card.confidence}) "
                          f"with new card (confidence: {new_card.confidence}).")
                    self.items[i] = new_card  
                    return

            if existing_card.name == new_card.name:
                print(f"Duplicate cards detected Name: {existing_card.name}")
                if new_card.confidence > existing_card.confidence:
                    print(f"Replacing card {existing_card.name} (confidence: {existing_card.confidence}) "
                          f"with new card (confidence: {new_card.confidence}).")
                    self.items[i] = new_card  
                    return

        self.items.append(new_card)

    def calculate_score(self):
        self.total_score = 0
        explaination = []
        for item in self.items:
            print(
                f"LOG: {item.name}: {item.calculate_score(self.items,self.resources)}"
            )
            explaination.append(
                f"{item.name}: {item.calculate_score(self.items,self.resources)}"
            )
            self.total_score += item.calculate_score(self.items,self.resources)
        return self.total_score, explaination
