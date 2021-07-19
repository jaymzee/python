from manim import *

class ExampleText(Scene):
    def construct(self):
        text = Text(r'\LaTeX').scale(3)
        self.add(text)

class ExampleLaTeX(Scene):
    def construct(self):
        tex = Tex(r'\LaTeX').scale(3)
        self.add(tex)

class Math(Scene):
    def construct(self):
        tex = MathTex(r'\int \frac{1}{x} \, dx = \log x').scale(3)
        self.play(Write(tex))
        self.wait()
