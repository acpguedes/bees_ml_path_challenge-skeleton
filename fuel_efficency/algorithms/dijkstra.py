import heapq
import math
from typing import List, Dict, Tuple
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position

class DijkstraStrategy(PathfindingStrategy):

    cardinal_directions = [Position(-1, -1), Position(-1, 0), Position(-1, 1), Position(0, -1), Position(0, 1), Position(1, -1), Position(1, 0), Position(1, 1)]

    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:
        queue: List[Tuple[float, Node]] = [(0, start)]
        distances: Dict[Node, float] = {start: 0}
        came_from: Dict[Node, Node] = {}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                return DijkstraStrategy.reconstruct_path(came_from, start, end)

            for neighbor in DijkstraStrategy.get_neighbors(grid, current_node):
                distance = current_distance + DijkstraStrategy.calculate_distance(current_node, neighbor)
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    came_from[neighbor] = current_node

        return []

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        neighbors = []
        for direction in DijkstraStrategy.cardinal_directions:
            new_position = node.position + direction
            if 0 <= new_position.x < len(grid) and 0 <= new_position.y < len(grid[0]):
                neighbors.append(grid[new_position.x][new_position.y])
        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        return math.sqrt((node1.position.x - node2.position.x) ** 2 + (node1.position.y - node2.position.y) ** 2)

    @staticmethod
    def reconstruct_path(came_from: Dict[Node, Node], start: Node, end: Node) -> List[Node]:
        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
