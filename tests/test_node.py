import pytest
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position
from fuel_efficency.entities.valley import Valley
from fuel_efficency.entities.plateau import Plateau
from fuel_efficency.entities.up_hill import UpHill
from fuel_efficency.entities.down_hill import DownHill

@pytest.mark.parametrize("node_cls, weight, position", [
    (Valley, 1.0, Position()),
    (Plateau, 1.0, Position()),
    (UpHill, 2.0, Position()),
    (DownHill, 0.5, Position())
])
def test_node_initialization(node_cls, weight, position) -> None:
    node = node_cls()
    assert node.weight == weight
    assert node.position == position

@pytest.mark.parametrize("node1, node2, expected", [
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=2.0, position=Position(2, 2)), True),
    (Valley(weight=2.0, position=Position(2, 2)), Valley(weight=1.0, position=Position(1, 1)), False)
])
def test_node_comparisons_lt(node1, node2, expected) -> None:
    assert (node1 < node2) == expected

@pytest.mark.parametrize("node1, node2, expected", [
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=2.0, position=Position(2, 2)), True),
    (Valley(weight=2.0, position=Position(2, 2)), Valley(weight=1.0, position=Position(1, 1)), False),
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=1.0, position=Position(1, 1)), True)
])
def test_node_comparisons_le(node1, node2, expected) -> None:
    assert (node1 <= node2) == expected

@pytest.mark.parametrize("node1, node2, expected", [
    (Valley(weight=2.0, position=Position(2, 2)), Valley(weight=1.0, position=Position(1, 1)), True),
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=2.0, position=Position(2, 2)), False)
])
def test_node_comparisons_gt(node1, node2, expected) -> None:
    assert (node1 > node2) == expected

@pytest.mark.parametrize("node1, node2, expected", [
    (Valley(weight=2.0, position=Position(2, 2)), Valley(weight=1.0, position=Position(1, 1)), True),
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=2.0, position=Position(2, 2)), False),
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=1.0, position=Position(1, 1)), True)
])
def test_node_comparisons_ge(node1, node2, expected) -> None:
    assert (node1 >= node2) == expected

@pytest.mark.parametrize("node1, node2, expected", [
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=1.0, position=Position(1, 1)), True),
    (Valley(weight=1.0, position=Position(1, 1)), Valley(weight=2.0, position=Position(2, 2)), False)
])
def test_node_equality(node1, node2, expected) -> None:
    assert (node1 == node2) == expected

def test_node_hash() -> None:
    node1 = Valley(weight=1.0, position=Position(1, 1))
    node2 = Valley(weight=1.0, position=Position(1, 1))
    node_set = {node1, node2}
    assert len(node_set) == 1

@pytest.mark.parametrize("node_cls", [Valley, Plateau, UpHill, DownHill])
def test_node_eq_error_raised(node_cls) -> None:
    node = node_cls()
    other = int()
    with pytest.raises(NotImplementedError) as excinfo:
        node == other
    assert "Missing `position` or `weight` attribute" in str(excinfo.value)

@pytest.mark.parametrize("node_cls", [Valley, Plateau, UpHill, DownHill])
def test_node_lt_error_raised(node_cls) -> None:
    node = node_cls()
    other = int()
    with pytest.raises(NotImplementedError) as excinfo:
        node < other
    assert "Missing `weight` attribute" in str(excinfo.value)
