cards_base_score_dict = {
    "ladeninhaber-card": 1,
    "gasthause-card": 2,
    "kran-card": 1,
    "ehefrau-card": 2,
    "kloster-card": 1,
    "kapelle-card": 2,
    "gastwirt-card": 1,
    "holzschnitzer-card": 2,
    "doktor-card": 4,
    "bootskrote-card": 1,
    "universitat-card": 3,
    "post-card": 2,
    "friedhof-card": 0,
    "schloss-card": 4,
    "gemischtwarenladen-card": 1,
    "boot-aus-zweigen-card": 1,
    "totenfraberin-card": 1,
    "harzraffinerie-card": 1,
    "schulile-card": 1,
    "monsch-card": 0,
    "farn-card": 1,
    "lehrer-card": 2,
    "festplatz-card": 3,
    "ehemann-card": 2,
    "fegehornchen-card": 2,
    "lager-card": 2,
    "wanderin-card": 1,
    "farm-card": 1,
    "brieftaube-card": 0,
    "palast-card": 4,
    "ausguck-card": 2,
    "mine-card": 2,
    "hirtin-card": 1,
    "konig-card": 4,
    "waldlaufer-card": 1,
    "ruine-card": 0,
    "gericht-card": 2,
    "richterin-card": 2,
    "architekt-card": 2,
    "barde-card": 0,
    "immerbaum-card": 5,
    "hausierer-card": 1,
    "konigin-card": 4,
    "verlies-card": 0,
    "historiker-card": 1,
    "uhrenturm-card": 0,
    "theater-card": 3,
    "minemaulwurf-card": 1,
    "score-token-1": 1,
    "score-token-3": 3,
    "basic-event-city-monument": 3,
    "basic-event-expedition": 3,
    "basic-event-grand-tour": 3,
    "basic-event-harvest-festival": 3,
}


class Box:
    def __init__(self, x1: float, x2: float, y1: float, y2: float):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class BaseItem:
    base_score = 0

    def __init__(self, name: str, id: int, confidence: float, box: Box, segments: any):
        self.name = name
        self.id = id
        self.confidence = confidence
        self.box = box
        self.segments = segments
        try:
            self.base_score = cards_base_score_dict[self.name]
        except Exception as e:
            print("not found in dict: ", self.name, "error: ", e)
