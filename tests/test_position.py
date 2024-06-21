import pytest
from fuel_efficency.entities.position import Position

@pytest.mark.parametrize("pos1, pos2, expected", [
    (Position(1, 2), Position(2, 3), True),
    (Position(2, 3), Position(1, 2), False)
])
def test_position_comparisons_lt(pos1, pos2, expected) -> None:
    assert (pos1 < pos2) == expected

@pytest.mark.parametrize("pos1, pos2, expected", [
    (Position(1, 2), Position(2, 3), True),
    (Position(2, 3), Position(1, 2), False),
    (Position(1, 2), Position(1, 2), True)
])
def test_position_comparisons_le(pos1, pos2, expected) -> None:
    assert (pos1 <= pos2) == expected

@pytest.mark.parametrize("pos1, pos2, expected", [
    (Position(2, 3), Position(1, 2), True),
    (Position(1, 2), Position(2, 3), False)
])
def test_position_comparisons_gt(pos1, pos2, expected) -> None:
    assert (pos1 > pos2) == expected

@pytest.mark.parametrize("pos1, pos2, expected", [
    (Position(2, 3), Position(1, 2), True),
    (Position(1, 2), Position(2, 3), False),
    (Position(1, 2), Position(1, 2), True)
])
def test_position_comparisons_ge(pos1, pos2, expected) -> None:
    assert (pos1 >= pos2) == expected

@pytest.mark.parametrize("pos1, pos2, expected", [
    (Position(1, 2), Position(1, 2), True),
    (Position(1, 2), Position(2, 3), False)
])
def test_position_equality(pos1, pos2, expected) -> None:
    assert (pos1 == pos2) == expected

def test_position_hash() -> None:
    pos1 = Position(1, 2)
    pos2 = Position(1, 2)
    pos_set = {pos1, pos2}
    assert len(pos_set) == 1

def test_position_add_success() -> None:
    position1 = Position(x=10, y=20)
    position2 = Position(x=5, y=3)
    result = position1 + position2
    assert result.x == 15 and result.y == 23, "Addition should correctly add Position coordinates"

def test_position_add_invalid_type() -> None:
    position = Position(x=10, y=20)
    other = "not a position object"
    with pytest.raises(NotImplementedError) as excinfo:
        _ = position + other
    assert f"Cannot add Position and {type(other)}" in str(excinfo.value)

def test_position_sub_success() -> None:
    position1 = Position(x=10, y=20)
    position2 = Position(x=5, y=3)
    result = position1 - position2
    assert result.x == 5 and result.y == 17, "Subtraction should correctly subtract Position coordinates"

def test_position_sub_invalid_type() -> None:
    position = Position(x=10, y=20)
    other = "not a position object"
    with pytest.raises(NotImplementedError) as excinfo:
        _ = position - other
    assert f"Cannot subtract Position and {type(other)}" in str(excinfo.value)
