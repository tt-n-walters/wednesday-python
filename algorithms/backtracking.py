import random


class Vector(tuple):
    def __new__(cls, x, y):
        return type("tuple", cls, [x, y])

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(x={}, y={})".format(self.x, self.y)

    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)


    def __mul__(self, other):
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
        else:
            x = self.x * other
            y = self.y * other
        return Vector(x, y)
    



directions = {
    "up": Vector(0, 1),
    "down": Vector(0, -1),
    "left": Vector(-1, 0),
    "right": Vector(1, 0)
}
flipped = {v: d for d, v in directions.items()}

print(flipped)

rows = 15
columns = 15

start = Vector(columns // 2, rows // 2)
print(start)
end = Vector(9, 9)

maze = []
for i in range(rows):
    row = []
    for j in range(columns):
        # print("Creating cell", j, "in row", i)
        cell = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        row.append(cell)
    maze.append(row)


# Find neighbours around the current cell
# Randomly pick one
# Remove the walls
# Backtracking

current = start
stack = [start]

def generate():
    global current

    if stack:
        up =    current + directions["up"]
        down =  current + directions["down"]
        left =  current + directions["left"]
        right = current + directions["right"]

        neighbours = []
        if up.y < rows and not any(maze[up.y][up.x].values()):
            neighbours.append(up)
        if 0 <= down.y and not any(maze[down.y][down.x].values()):
            neighbours.append(down)
        if 0 <= left.x and not any(maze[left.y][left.x].values()):
            neighbours.append(left)
        if right.x < columns and not any(maze[right.y][right.x].values()):
            neighbours.append(right)

        if neighbours:
            next_position = random.choice(neighbours)

            direction_vector = next_position - current
            direction_string = flipped[direction_vector]
            next_direction = flipped[direction_vector * -1]

            maze[current.y][current.x][direction_string] = True     # Remove wall in current cell
            maze[next.y][next.x][next_direction] = True             # Remove opposite wall in next
            
            stack.append(current)
            current = next

        else:
            current = stack.pop()
            
        return current.x, current.y

from display import Window

window = Window(maze, rows, columns, 25)
window.generate = generate
window.generate_rate = 1
window.run()
