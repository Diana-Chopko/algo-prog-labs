import collections


class KnightSolution:
    """
    A class to solve the shortest path problem for a knight on a nxn chessboard.
    """
    def __init__(self, n):
        """
        Initialize the solver with the board size and possible knight moves.
        :param n: The size of the chessboard.
        """
        self.n = n
        self.direction = [
            (-1, -2), (-1, 2), (1, -2), (1, 2),
            (-2, -1), (-2, 1), (2, -1), (2, 1)
        ]

    def get_moves(self, current_posit):
        """
        Generate all valid next positions for a knight from the current position.
        :param current_posit: A tuple (x, y) representing the current coordinates.
        """
        curr_x, curr_y = current_posit
        for dx, dy in self.direction:
            next_x = curr_x + dx
            next_y = curr_y + dy

            if 0 <= next_x < self.n and 0 <= next_y < self.n:
                yield (next_x, next_y)

    def find_shortest_way(self, start_x, start_y, finish_x, finish_y):
        """
        Find the minimum number of knight moves required to reach the
        destination (BFS algorithm).
        :param start_x: The starting X coordinate.
        :param start_y: The starting Y coordinate.
        :param finish_x: The destination X coordinate.
        :param finish_y: The destination Y coordinate.
        :return: result
        """
        result = -1
        path_found = False

        if start_x == finish_x and start_y == finish_y:
            result = 0
            path_found = True

        memory = {(start_x, start_y): 0}
        queue = collections.deque([(start_x, start_y)])
        step = 0

        while len(queue) > 0 and not path_found:
            step += 1

            for _ in range(len(queue)):
                if path_found:
                    break

                current_posit = queue.popleft()
                for next_posit in self.get_moves(current_posit):
                    if next_posit not in memory:
                        memory[next_posit] = step
                        queue.append(next_posit)

                        next_x, next_y = next_posit
                        if next_x == finish_x and next_y == finish_y:
                            result = step
                            path_found = True
                            break
        return result


def run_file_test(input_filename, output_filename):
    """
    Read input data from a file, compute the shortest knight path, and write the result.
    :param input_filename: The path to the input text file.
    :param output_filename: The path to the output text file.
    :return: status_message
    """
    status_message = "Complete successfully, check out 'output.txt' "

    try:
        with open(input_filename, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        n = int(lines[0].split('#')[0].strip())

        start_parts = lines[1].split('#')[0].strip().split(',')
        start_x = int(start_parts[0].strip())
        start_y = int(start_parts[1].strip())

        dest_parts = lines[2].split('#')[0].strip().split(',')
        dest_x = int(dest_parts[0].strip())
        dest_y = int(dest_parts[1].strip())

        solver = KnightSolution(n)
        shortest_path = solver.find_shortest_way(start_x, start_y, dest_x, dest_y)

        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(str(shortest_path))

    except Exception as e:
        status_message = f"Error: {e}"

    return status_message


if __name__ == "__main__":
    result = run_file_test("input.txt", "output.txt")
    print(result)
