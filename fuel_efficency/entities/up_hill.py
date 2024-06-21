from dataclasses import dataclass, field

from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


@dataclass(slots=True, frozen=True)
class UpHill(Node):
    weight: float = field(default=2.0)
    position: Position = field(default_factory=Position)
