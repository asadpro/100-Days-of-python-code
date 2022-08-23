from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# By pressing the downward key while snake moving upward it isn't allowed in official python so to mitigate this problem we need constant angles.

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    # Snake body longivity track record.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_name in range(
            len(self.segments) - 1, 0, -1
        ):  # This line of code will take the position of every chunk of the snake

            x_cord = self.segments[seg_name - 1].xcor()
            y_cord = self.segments[seg_name - 1].ycor()

            self.segments[seg_name].goto(
                x=x_cord, y=y_cord
            )  # Here seg_name will pick snake segment and will push it to the place of onward segment in parallel with it.

        self.segments[0].forward(
            MOVE_DISTANCE
        )  # We will move forward only the first chunk of the snake

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
