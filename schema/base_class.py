cards_base_score_dict = {
    "narr-card": {"score": -2, "card_type": "unique critter"},
    "ladeninhaber-card": {"score": 1, "card_type": "unique critter"},
    "gasthaus-card": {"score": 2, "card_type": "common construction"},
    "kran-card": {"score": 1, "card_type": "unique construction"},
    "ehefrau-card": {"score": 2, "card_type": "common critter"},
    "kloster-card": {"score": 1, "card_type": "unique construction"},
    "kapelle-card": {"score": 2, "card_type": "unique construction"},
    "gastwirt-card": {"score": 1, "card_type": "unique critter"},
    "holzschnitzer-card": {"score": 2, "card_type": "common critter"},
    "doktor-card": {"score": 4, "card_type": "unique critter"},
    "bootskrote-card": {"score": 1, "card_type": "common critter"},
    "universitat-card": {"score": 3, "card_type": "unique construction"},
    "post-card": {"score": 2, "card_type": "common construction"},
    "friedhof-card": {"score": 0, "card_type": "unique construction"},
    "schloss-card": {"score": 4, "card_type": "unique construction"},
    "gemischtwarenladen-card": {"score": 1, "card_type": "unique construction"},
    "boot-aus-zweigen-card": {"score": 1, "card_type": "common construction"},
    "totengraberin-card": {"score": 1, "card_type": "unique critter"},
    "harzraffinerie-card": {"score": 1, "card_type": "common construction"},
    "schule-card": {"score": 1, "card_type": "unique constrcution"},
    "monch-card": {"score": 0, "card_type": "unique critter"},
    "lehrer-card": {"score": 2, "card_type": "common critter"},
    "festplatz-card": {"score": 3, "card_type": "unique construction"},
    "ehemann-card": {"score": 2, "card_type": "common critter"},
    "fegehornchen-card": {"score": 2, "card_type": "common critter"},
    "lager-card": {"score": 2, "card_type": "common construction"},
    "wanderin-card": {"score": 1, "card_type": "common critter"},
    "farm-card": {"score": 1, "card_type": "common construction"},
    "brieftaube-card": {"score": 0, "card_type": "common critter"},
    "palast-card": {"score": 4, "card_type": "unique construction"},
    "ausguck-card": {"score": 2, "card_type": "unique construction"},
    "mine-card": {"score": 2, "card_type": "common construction"},
    "hirtin-card": {"score": 1, "card_type": "unique critter"},
    "konig-card": {"score": 4, "card_type": "unique critter"},
    "waldlaufer-card": {"score": 1, "card_type": "unique critter"},
    "ruine-card": {"score": 0, "card_type": "common construction"},
    "gericht-card": {"score": 2, "card_type": "unique construction"},
    "richterin-card": {"score": 2, "card_type": "unique critter"},
    "architekt-card": {"score": 2, "card_type": "unique critter"},
    "barde-card": {"score": 0, "card_type": "unique critter"},
    "immerbaum-card": {"score": 5, "card_type": "unique construction"},
    "haustierer-card": {"score": 1, "card_type": "common critter"},
    "konigin-card": {"score": 4, "card_type": "unique critter"},
    "verlies-card": {"score": 0, "card_type": "unique construction"},
    "historiker-card": {"score": 1, "card_type": "unique critter"},
    "uhrenturm-card": {"score": 0, "card_type": "unique construction"},
    "theater-card": {"score": 3, "card_type": "unique construction"},
    "minenmaulwurf-card": {"score": 1, "card_type": "common critter"},
    "meinenmaulwurf-card": {"score": 1, "card_type": "common critter"},
    "score-token-1": {"score": 1, "card_type": "token"},
    "score-token-3": {"score": 3, "card_type": "token"},
    "basic-event-city-monument": {"score": 3, "card_type": "basic-event"},
    "basic-event-expedition": {"score": 3, "card_type": "basic-event"},
    "basic-event-grand-tour": {"score": 3, "card_type": "basic-event"},
    "basic-event-harvest-festival": {"score": 3, "card_type": "basic-event"},
    "special-event-card": {"score": 1, "card_type": "special-event"},
}


class Box:
    def __init__(self, x1: float, x2: float, y1: float, y2: float):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def overlaps(self, other_box):
        return not (
            self.x2 < other_box.x1
            or self.x1 > other_box.x2
            or self.y2 < other_box.y1
            or self.y1 > other_box.y2
        )


class BaseItem:
    base_score = 0
    prosperty_card = False

    def __new__(cls, name: str, id: int, confidence: float, box, segments):
        if name == "architekt-card":
            instance = super().__new__(Architect)
            instance.prosperity_card = True
            return instance
        if name == "konig-card":
            instance = super().__new__(King)
            instance.prosperity_card = True
            return instance
        if name == "ehefrau-card":
            instance = super().__new__(Wife)
            instance.prosperity_card = True
            return instance
        if name == "schloss-card":
            instance = super().__new__(Castle)
            instance.prosperity_card = True
            return instance
        if name == "immerbaum-card":
            instance = super().__new__(Evertree)
            instance.prosperity_card = True
            return instance
        if name == "palast-card":
            instance = super().__new__(Palace)
            instance.prosperity_card = True
            return instance
        if name == "schule-card":
            instance = super().__new__(School)
            instance.prosperity_card = True
            return instance
        if name == "theater-card":
            instance = super().__new__(Theater)
            instance.prosperity_card = True
            return instance
        if "journey" in name:
            instance = super().__new__(Journey)
            return instance

        if name not in cards_base_score_dict:
            print(f"Creating Resource instance for: {name}")
            return super().__new__(Resource)

        print(f"Creating BaseItem instance for: {name}")
        return super().__new__(cls)

    def __init__(self, name: str, id: int, confidence: float, box: Box, segments: any):
        self.name = name
        self.id = id
        self.confidence = confidence
        self.box = box
        self.segments = segments
        try:
            self.base_score = cards_base_score_dict[name]["score"]
            self.card_type = cards_base_score_dict[name]["card_type"]
        except Exception as e:
            print("not found in dict: ", self.name, "error: ", e)

    def calculate_score(self, items, resources=None):
        return self.base_score


class Resource(BaseItem):
    def __init__(self, name, id, confidence, box, segments):
        self.name = name
        self.id = id
        self.confidence = confidence
        self.box = box
        self.segments = segments
        self.used = False
        print(f"${self.name} init and used = ${self.used}")


class Architect(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=[]):
        prosperity_score = self.base_score

        for resource in resources:
            if (
                resource.name == "stone"
                or resource.name == "resin"
                and resource.used == False
            ):
                prosperity_score = min(self.base_score + 6, prosperity_score + 1)
                print(
                    f"Architect: prosperty_score = {prosperity_score} + 1 because of {resource.name} not used "
                )
                resource.used = True
        return prosperity_score


class King(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.card_type == "basic-event":
                print(
                    f"King: prosperty_score = {Prosperity_score} + 1 because of {item.name}"
                )
                Prosperity_score += 1
            elif item.card_type == "special-event":
                print(
                    f"King: prosperty_score = {Prosperity_score} + 2 because of {item.name}"
                )
                Prosperity_score += 2
        return Prosperity_score


class Wife(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.name == "ehemann-card":
                print(
                    f"Wife: prosperty_score = {Prosperity_score} + 3 because of {item.name}"
                )
                Prosperity_score += 3
        return Prosperity_score


class Castle(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.card_type == "common construction":
                print(
                    f"Castle: prosperty_score = {Prosperity_score} + 1 because of {item.name} which is common construction"
                )
                Prosperity_score += 1
        return Prosperity_score


class Evertree(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.prosperty_card == True and item.name != "immerbaum-card":
                print(
                    f"Evertree: prosperty_score = {Prosperity_score} + 1 because of {item.name} which is prosperty card"
                )
                Prosperity_score += 1
        return Prosperity_score


class Palace(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.card_type == "unique construction":
                print(
                    f"Palace: prosperty_score = {Prosperity_score} + 1 because of {item.name} which is unique construction"
                )
                Prosperity_score += 1
        return Prosperity_score


class School(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.card_type == "common critter":
                print(
                    f"School: prosperty_score = {Prosperity_score} + 1 because of {item.name} which is common critter"
                )
                Prosperity_score += 1
        return Prosperity_score


class Theater(BaseItem):
    prosperty_card = True

    def calculate_score(self, items, resources=None):
        Prosperity_score = self.base_score
        for item in items:
            if item.card_type == "unique critter":
                print(
                    f"Theater: prosperty_score = {Prosperity_score} + 1 because of {item.name} which is unique critter"
                )
                Prosperity_score += 1
        return Prosperity_score


class Journey(BaseItem):

    def calculate_score(self, items, resources):
        score = self.base_score
        curr_location = int(self.name.split("-")[1])  # from journey-2 returns 2
        for resource in resources:
            if "worker" in resource.name and self.box.overlaps(
                resource.box
            ):  # should be modified to diffrentiate between workers
                print(
                    f"Worker: score = {curr_location} because of overlapping with {self.name}"
                )
                score += curr_location
        return score
