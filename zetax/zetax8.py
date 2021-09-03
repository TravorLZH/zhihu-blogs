from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#8")
        eqn0=TextMobject(r"For all $\Re(s)>1$, we have")
        eqn=TexMobject(r"\zeta(s,{a})=\sum_{n=0}^\infty{1\over(n+{a})^s}",
                tex_to_color_map={
                    r"\zeta":PINK,
                    "{a}":RED,
                    r"\sum_{n=0}^\infty":ORANGE
                })
        eqn2=TexMobject(r"\zeta(1-s,{a})={\Gamma(s)\over(2\pi)^s}\left[e^{-i\pi s/2}\sum_{n=1}^\infty{e^{2\pi ina}\over n^s}+e^{i\pi s/2}\sum_{n=1}^\infty{e^{-2\pi ina}\over n^s}\right]",
                tex_to_color_map={
                    r"\zeta":PINK,
                    "a}":RED,
                    r"\sum_{n=1}^\infty":BLUE
                })
        self.add(VGroup(tit,VGroup(eqn0,eqn,eqn2).scale(0.8).arrange(DOWN)).arrange(DOWN))
        self.wait()
