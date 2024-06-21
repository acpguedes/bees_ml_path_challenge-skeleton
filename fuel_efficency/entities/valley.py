from dataclasses import dataclass, field
from typing import Any
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position

@dataclass(slots=True, frozen=True)
class Valley(Node):
    weight: float = field(default=1.0)
    position: Position = field(default_factory=Position)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `position` or `weight` attribute")
        return (self.weight, self.position) == (other.weight, other.position)
