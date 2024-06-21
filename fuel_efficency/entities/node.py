from dataclasses import dataclass, field

from typing import Protocol
from fuel_efficency.entities.position import Position


@dataclass(slots=True, frozen=True)
class Node(Protocol):
    weight: float = field(default=0.0)
    position: Position = field(default_factory=Position)

    def __eq__(self, other) -> bool:
        return (self.weight, self.position) == (other.weight, other.position)

    def __hash__(self) -> int:
        return hash((self.weight, self.position))

    def __lt__(self, other) -> bool:
        return (self.weight, self.position) < (other.weight, other.position)

    def __le__(self, other) -> bool:
        return (self.weight, self.position) <= (other.weight, other.position)

    def __gt__(self, other) -> bool:
        return (self.weight, self.position) > (other.weight, other.position)

    def __ge__(self, other) -> bool:
        return (self.weight, self.position) >= (other.weight, other.position)
