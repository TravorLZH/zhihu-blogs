from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#11")
        fml0=TexMobject(r"\varphi(n)=\operatorname{card}\{m\in\mathbb Z:1\le m\le n,\gcd(m,n)=1\}",
                tex_to_color_map={
                    r"\varphi":ORANGE,
                    r"\operatorname{card}":TEAL
                })
        fml=TexMobject(r"\lim_{x\to\infty}{1\over\log x}\sum_{n\le x}{1\over\varphi(n)}={315\zeta(3)\over2\pi^4}",
                tex_to_color_map={
                    r"\lim":YELLOW,
                    r"\sum":GREEN,
                    r"\zeta":RED,
                    r"\pi":BLUE
                })
        self.add(VGroup(tit,fml0,fml).arrange(DOWN))
        self.wait()
