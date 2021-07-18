from manim import *

class ExampleText(Scene):
    def construct(self):
        tex = Text(r'\LaTeX').scale(3)
        self.add(tex)

class ExampleLaTeX(Scene):
    def construct(self):
        tex = Tex(r'\LaTeX').scale(3)
        self.add(tex)
