from typing import List
from pydantic import BaseModel


class PredictionRes(BaseModel):
    card_names: List[str]
    score: int
    score_details: List[str]
