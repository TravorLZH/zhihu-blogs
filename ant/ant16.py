from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#16")
        eqn=TexMobject(r"\sum_{\substack{n\le z\\(n,q)=1}}\frac1n>{\varphi({q})\over{q}}\log z",tex_to_color_map={"{q}":TEAL})
        tit2=TextMobject(r"Brun-Titchmarsh Inequality")
        eqn2=TexMobject(r"\pi(x+y;{q},{a})-\pi(x;{q},{a})\le{(2+\varepsilon)y\over\varphi({q})\log y/q}",
                tex_to_color_map={
                    "q}":TEAL,r"\varepsilon":PINK,
                    "{a}":RED,"y":BLUE
                })
        self.add(VGroup(tit,eqn,tit2,eqn2).arrange(DOWN))
        self.wait()
