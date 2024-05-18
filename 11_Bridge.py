from abc import ABC, abstractmethod

# 抽象化部分
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass


# 実装部分
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: int):
        pass

    @abstractmethod
    def render_square(self, width: int, height: int):
        pass


# 具体的な実装
class VectorRenderer(Renderer):
    def render_circle(self, radius: int):
        print("Render circle of radius={} as lines.".format(radius))

    def render_square(self, width: int, height: int):
        print("Render square of width={} height={} as lines.".format(width, height))

class RasterRenderer(Renderer):
    def render_circle(self, radius: int):
        print("Render circle of radius={} as pixcels.".format(radius))

    def render_square(self, width: int, height: int):
        print("Render square of width={} height={} as pixcels.".format(width, height))


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer: Renderer, width: int, height: int):
        super().__init__(renderer)
        self.width = width
        self.height = height

    def draw(self):
        self.renderer.render_square(self.width, self.height)


if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    circle = Circle(vector_renderer, 10)
    circle.draw()
    square = Square(vector_renderer, 20, 30)
    square.draw()

    raster_renderer = RasterRenderer()
    circle = Circle(raster_renderer, 10)
    circle.draw()
    square = Square(raster_renderer, 20, 30)
    square.draw()
