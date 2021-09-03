from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#9")
        eqn=TexMobject(r"\zeta\left(\frac12+i{t}\right)=\sum_{n\le x}n^{-1/2-i{t}}+\mathcal O(\log^{1/4}|{t}|)",
                tex_to_color_map={
                    r"\zeta":RED,
                    r"{t}":YELLOW
                })
        eqn2=TexMobject(r"x=|{t}|/2\pi\log^{1/2}|{t}|",
                tex_to_color_map={
                    r"{t}":YELLOW
                })
        self.add(VGroup(tit,eqn2,eqn).arrange(DOWN))
        self.wait()
