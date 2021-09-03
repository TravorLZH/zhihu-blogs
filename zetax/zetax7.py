from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#7")
        eqn=TexMobject(r"\int_1^\infty{A(x)-x\over x^2}\mathrm dx\text{ converges}\Rightarrow\lim_{x\to\infty}{A(x)\over x}=1",
                tex_to_color_map={
                    "A":RED,
                    r"\int_1^\infty":PINK,
                    r"\mathrm dx":PINK,
                    r"\lim":ORANGE,
                })
        eqn2=TexMobject(r"\lim_{s\to1}\left[-\frac1s{\zeta'\over\zeta}(s)-{1\over s-1}\right]=\int_1^\infty{\psi(x)-x\over x^2}\mathrm dx\text{ converges}",
                tex_to_color_map={
                    r"\psi":GREEN,
                    r"\int_1^\infty":PINK,
                    r"\mathrm dx":PINK
                })
        self.add(VGroup(tit,eqn2,eqn).arrange(DOWN))
        self.wait()
