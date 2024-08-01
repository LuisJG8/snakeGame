from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
ANGLES = [0, 90, 180, 270]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        bob = Turtle("square")
        bob.color("white")
        bob.penup()
        bob.goto(position)
        self.segments.append(bob)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != ANGLES[3]:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != ANGLES[1]:
            self.segments[0].setheading(270)

    def right(self):
        if self.head.heading() != ANGLES[2]:
            self.segments[0].setheading(0)

    def left(self):
        if self.head.heading() != ANGLES[0]:
            self.segments[0].setheading(180)