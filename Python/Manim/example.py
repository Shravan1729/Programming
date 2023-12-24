from manim import *

class example(Scene):
    def construct(self):
        axis = Axes(x_range=(-5,5),y_range=(0,10))
        Scene.add(axis)
        