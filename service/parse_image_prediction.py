import json

from schema.base_class import Box, BaseItem, Resource
from schema.everdell_image import EverdellImage


def aggregate_resources(resources) -> dict:
    dictionary = {}
    for resource in resources:
        if resource in dictionary:
            dictionary[resource] = dictionary[resource] + 1
        else:
            dictionary[resource] = 1
    return dictionary


def parse_image_prediction(prediction):
    # prediction.show()  # display to screen
    prediction_json = json.loads(prediction.to_json())
    items: list[BaseItem] = []
    resources: list[Resource] = []
    # For each object in each picture parse to the proper class
    for object in prediction_json:
        box_json = object["box"]
        box = Box(
            x1=box_json["x1"], x2=box_json["x2"], y1=box_json["y1"], y2=box_json["y2"]
        )
        item = BaseItem(
            object["name"],
            object["class"],
            object["confidence"],
            box=box,
            segments=object["segments"],
        )
        if isinstance(item, Resource):
            resources.append(item)
        else:
            items.append(item)

    image = EverdellImage(items=None, resources=resources, prediction=prediction)
    image.items = [image.add_card(item) for item in items]
    card_names = [item.name for item in image.items]
    resources = [(resource.name) for resource in image.resources]
    resources_dict = aggregate_resources(resources)
    score, score_details = image.calculate_score()
    return card_names, resources_dict, score, score_details
