from manimlib.imports import *

class TestScene(Scene):
    def construct(self):
        circ = Circle()
        text = TextMobject("Hello manim!")
        text.scale(2)

        tex = TexMobject(r"\sum_{k=1}^\infty {1 \over k^2} = {\pi^2 \over 6}")

        group = VGroup(text, tex)
        group.arrange(DOWN)

        #img = SVGMobject("animated-pi.svg")
        img = ImageMobject("SupportIcon.png")

        # self.play(text, rate_func=rush_into)

        self.add(img)
        self.wait()
        self.remove(img)
        self.play(ShowCreation(circ))
        self.wait()
        self.play(Transform(circ, text))
        self.wait()
        self.play(Write(tex))
        self.wait()


class TestScene2(Scene):
    def construct(self):
        tex = TexMobject(r'e^{i \pi} + 1 = 0')

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


class SurfaceTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        c=2
        a=1
        trr = ParametricSurface(
            lambda u, v : [
                (c + a * math.cos(TAU * v)) * math.cos(TAU * u),
                (c + a * math.cos(TAU * v)) * math.sin(TAU * u),
                a * np.sin(TAU * v)
            ],
            resolution=(6, 16)
        ).fade(0.3)

        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        self.add(axes)

        self.play(Write(trr))
        self.wait()
        self.move_camera(phi=30*DEGREES, theta=45*DEGREES)
        self.wait()


class SurfaceSphere(ThreeDScene):
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


class GraphAxes(GraphScene):
    def construct(self):
        ax = Axes(
            axis_config = {
                "color": BLUE
            },
            x_min=-4,
            x_max=4,
            y_min=-4,
            y_max=4,
        )
        f = ax.get_graph(lambda x: 1 if x > 0 else -1, discontinuities=[0])
        #f2 = FunctionGraph(lambda t: t*t)
        f2 = ParametricFunction(
            lambda t: [
                (1 + np.cos(TAU * t)) * np.cos(TAU * t),
                (1 + np.cos(TAU * t)) * np.sin(TAU * t),
                0
            ]
        )

        self.add(ax)
        self.wait()
        self.play(Write(f))
        self.wait()
        self.play(Write(f2))
        self.wait()


class Cardioid(GraphScene):
    def construct(self):
        ax = Axes(
            axis_config = {
                "color": BLUE
            },
            x_min=-4,
            x_max=4,
            y_min=-4,
            y_max=4,
        )
        r = lambda theta: 1 + np.cos(theta)
        f = ParametricFunction(
            lambda t: [
                r(TAU * t) * np.cos(TAU * t),
                r(TAU * t) * np.sin(TAU * t),
                0
            ]
        )

        self.add(ax)
        self.wait()
        self.play(Write(f))
        self.wait()


class NumberLineTest(Scene):
    def construct(self):
        n = NumberLine(
            x_min=-5,
            x_max=5,
            include_tip=True,
            include_numbers=True
        )

        self.add(n)
        self.wait()

