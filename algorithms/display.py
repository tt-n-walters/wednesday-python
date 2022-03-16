import arcade
import itertools


class Window(arcade.Window):
    def __init__(self, maze, rows=10, columns=10, size=40, offset=20):
        width = columns * size + offset * 2
        height = rows * size + offset * 2
        super().__init__(width, height, "Maze")
        self.maze = maze
        self.rows = rows
        self.columns = columns
        self.size = size
        self.offset = offset

        self.draws = 0
        self.generate_rate = None
        self.maze_position = None

        self.create_shapes()

    def create_shapes(self):
        self.shapes = arcade.ShapeElementList()
        for column, row in itertools.product(range(self.columns), range(self.rows)):
            cell = self.maze[row][column]
            x = column * self.size + self.offset
            y = row * self.size + self.offset
            if not cell["down"]:
                self.shapes.append(arcade.create_line(
                    x, y, x+self.size, y, arcade.color.WHITE))
            if not cell["right"]:
                self.shapes.append(arcade.create_line(
                    x+self.size, y, x+self.size, y+self.size, arcade.color.WHITE))
        points = (
            (self.offset, self.offset),
            (self.offset, self.height-self.offset),
            (self.width-self.offset, self.height-self.offset),
            (self.width-self.offset, self.offset)
        )
        if self.maze_position:
            x, y = self.maze_position
            self.shapes.append(arcade.create_rectangle_filled(
                (x + 0.5) * self.size + self.offset,
                (y + 0.5) * self.size + self.offset,
                self.size * 0.8,
                self.size * 0.8,
                arcade.color.LIME
            ))
        self.shapes.append(arcade.create_line_loop(points, arcade.color.WHITE))

    def on_draw(self):
        arcade.start_render()
        if self.generate_rate and self.draws == self.generate_rate:
            self.draws = 0
            r = self.generate()
            if not r is None:
                self.maze_position = r
            self.create_shapes()
        self.shapes.draw()
        self.draws += 1

    def run(self):
        arcade.run()
