# manim scene

from manimlib.imports import *
import math

class HelloScene(GraphScene):
    CONFIG = {
        "x_min": -3.14,
        "x_max": 3.14,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: math.sin(x), WHITE)
        graph_label = self.get_graph_label(graph, label=r'\sin(x)')

        self.play(ShowCreation(graph), Write(graph_label))
