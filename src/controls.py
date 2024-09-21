
from dataclasses import dataclass


@dataclass
class Controls:
    left_key: int
    right_key: int
    up_key: int
    down_key: int
    fire: int
