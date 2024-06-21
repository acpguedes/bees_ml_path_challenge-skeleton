from dataclasses import dataclass, field
from typing import Any
from fuel_efficency.entities.position import Position

@dataclass(slots=True, frozen=True)
class Node:
    weight: float = field(default=0.0)
    position: Position = field(default_factory=Position)

    def __init__(self, *args, **kwargs):
        if type(self) is Node:
            raise TypeError("Node class cannot be instantiated directly")
        super().__init__(*args, **kwargs)

    def __hash__(self) -> int:
        return hash((self.weight, self.position))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `position` or `weight` attribute")
        return (self.weight, self.position) == (other.weight, self.position)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `weight` attribute")
        return (self.weight, self.position) < (other.weight, self.position)

    def __le__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `weight` attribute")
        return (self.weight, self.position) <= (other.weight, self.position)

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `weight` attribute")
        return (self.weight, self.position) > (other.weight, self.position)

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `weight` attribute")
        return (self.weight, self.position) >= (other.weight, self.position)
