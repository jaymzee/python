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


class SurfaceExample3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        c=1
        a=1
        trr = ParametricSurface(
            lambda u, v : np.array([
                 (c + a * math.cos(TAU * v)) * math.cos(TAU * u),
                 (c + a * math.cos(TAU * v)) * math.sin(TAU * u),
                 a * np.sin(TAU * v)
             ]),
            resolution=(6, 32)).fade(0.7) #Resolution of the surfaces

        self.set_camera_orientation(phi=60 * DEGREES,theta=-45*DEGREES)
        self.add(axes)

        self.play(Write(trr))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.1)


class SurfaceExample2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.move_camera(phi=70 * DEGREES, theta=-30 * DEGREES)
        surface = ParametricSurface(lambda u, v: [u, v, u+v], resolution=(32, 32)).fade(0.9)

        self.play(ShowCreation(surface), ShowCreation(axes))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)


class SurfaceExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.move_camera(phi=70 * DEGREES, theta=-30 * DEGREES)
        sphere = Sphere(radius=3)

        self.play(ShowCreation(sphere), ShowCreation(axes))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        

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

