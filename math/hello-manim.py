from manimlib.imports import *

class TestScene(Scene):
    def construct(self):
        circ = Circle()
        t = TextMobject("Hello manim!")
        t.scale(2)

        tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )

        group = VGroup(t, tex)
        group.arrange(DOWN)

        self.play(ShowCreation(circ))
        self.play(Write(t))
        self.play(Write(tex))
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()


class SurfaceExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.move_camera(phi=70 * DEGREES, theta=-30 * DEGREES)
        sphere = Sphere(radius=3)

        self.play(ShowCreation(sphere), ShowCreation(axes))
        self.wait()
        

class Graph2dFunc(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x**2, WHITE)
        graph_label = self.get_graph_label(graph, label='x^{2}')

        graph2 = self.get_graph(lambda x: x**3, WHITE)
        graph_label2 = self.get_graph_label(graph2, label='x^{3}')

        graph3 = self.get_graph(lambda x: max(x, 0), WHITE)
        graph_label3 = self.get_graph_label(graph3, label='max(x, 0)')

        # Display graph
        self.play(ShowCreation(graph), Write(graph_label))
        self.wait(1)
        self.play(ReplacementTransform(graph, graph2), 
                  ReplacementTransform(graph_label, graph_label2))
        self.wait(1)
        self.play(ReplacementTransform(graph2, graph3), 
                  ReplacementTransform(graph_label2, graph_label3))
        self.wait(1)