import json

from schema.base_class import Box, BaseItem, Resource
from schema.everdell_image import EverdellImage


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

    image = EverdellImage(items=items, resources=resources, prediction=prediction)
    card_names = [item.name for item in image.items]
    card_names.append([resource.name for resource in image.resources])
    score, score_details = image.calculate_score()
    return card_names, score, score_details
