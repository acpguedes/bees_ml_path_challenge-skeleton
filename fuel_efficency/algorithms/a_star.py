import heapq
import math
from typing import List, Dict, Tuple
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position

class AStarStrategy(PathfindingStrategy):

    allowed_directions = [Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:
        open_set: List[Tuple[float, Node]] = [(0, start)]
        came_from: Dict[Node, Node] = {}
        g_score: Dict[Node, float] = {start: 0}
        f_score: Dict[Node, float] = {start: AStarStrategy.heuristic(start.position, end.position)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == end:
                return AStarStrategy.reconstruct_path(came_from, start, end)

            for neighbor in AStarStrategy.get_neighbors(grid, current):
                tentative_g_score = g_score[current] + AStarStrategy.calculate_distance(current, neighbor)

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + AStarStrategy.heuristic(neighbor.position, end.position)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        neighbors = []
        for direction in AStarStrategy.allowed_directions:
            new_position = node.position + direction
            if 0 <= new_position.x < len(grid) and 0 <= new_position.y < len(grid[0]):
                neighbors.append(grid[new_position.x][new_position.y])
        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        return node2.weight

    @staticmethod
    def heuristic(pos1: Position, pos2: Position) -> float:
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)

    @staticmethod
    def reconstruct_path(came_from: Dict[Node, Node], start: Node, end: Node) -> List[Node]:
        path = []
        current = end
        while current != start:
            path.append(current)
