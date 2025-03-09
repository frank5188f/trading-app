import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random

kivy.require('1.11.1')

# 定义蛇的方块大小
BLOCK_SIZE = 20


class SnakeBlock(Widget):
    pass


class Snake(Widget):
    head_x = NumericProperty(0)
    head_y = NumericProperty(0)
    head_pos = ReferenceListProperty(head_x, head_y)

    def __init__(self, **kwargs):
        super(Snake, self).__init__(**kwargs)
        self.body = []
        self.direction = Vector(1, 0)
        self.add_block()

    def add_block(self):
        block = SnakeBlock()
        block.pos = self.head_pos
        self.body.append(block)
        self.add_widget(block)

    def move(self):
        new_head = self.head_pos + self.direction * BLOCK_SIZE
        self.head_pos = new_head
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].pos = self.body[i - 1].pos
        self.body[0].pos = self.head_pos


class Food(Widget):
    def __init__(self, **kwargs):
        super(Food, self).__init__(**kwargs)
        self.randomize()

    def randomize(self):
        max_x = int(self.parent.width / BLOCK_SIZE) - 1
        max_y = int(self.parent.height / BLOCK_SIZE) - 1
        self.pos = (random.randint(0, max_x) * BLOCK_SIZE, random.randint(0, max_y) * BLOCK_SIZE)


class SnakeGame(Widget):
    snake = None
    food = None

    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self.snake = Snake()
        self.food = Food()
        self.add_widget(self.snake)
        self.add_widget(self.food)
        Clock.schedule_interval(self.update, 1.0 / 5.0)

    def update(self, dt):
        self.snake.move()
        if self.snake.head_pos == self.food.pos:
            self.snake.add_block()
            self.food.randomize()

    def on_touch_down(self, touch):
        if touch.x > self.width / 2:
            if self.snake.direction != Vector(-1, 0):
                self.snake.direction = Vector(1, 0)
        elif touch.x < self.width / 2:
            if self.snake.direction != Vector(1, 0):
                self.snake.direction = Vector(-1, 0)
        if touch.y > self.height / 2:
            if self.snake.direction != Vector(0, -1):
                self.snake.direction = Vector(0, 1)
        elif touch.y < self.height / 2:
            if self.snake.direction != Vector(0, 1):
                self.snake.direction = Vector(0, -1)


class SnakeApp(App):
    def build(self):
        return SnakeGame()


if __name__ == '__main__':
    SnakeApp().run()
