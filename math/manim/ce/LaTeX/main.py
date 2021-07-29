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

class Convolution(Scene):
    def construct(self):
        conv = Text('Convolution')
        eq1 = MathTex(r'(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau')
        VGroup(conv, eq1).arrange(DOWN)
        self.play(
            Write(conv),
            FadeInFrom(eq1, UP)
        )
        self.wait()

        corr = Text('Correlation')
        eq2 = MathTex(r'(f \star g)(\tau) = \int_{-\infty}^{\infty}'
                      r'\overline{f(t)} g(t + \tau) \, dt')
        VGroup(corr, eq2).arrange(DOWN)
        self.play(
            Transform(conv, corr),
            Transform(eq1, eq2)
        )
        self.wait()
