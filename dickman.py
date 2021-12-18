from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Dickman's $\rho$ function and smooth numbers")
        eqn=TexMobject(r"\Psi(x,y)=\#\{n\le x:p|n\Rightarrow p\le y\}",
                tex_to_color_map={r"\Psi":RED})
        eqn2=TexMobject(r"\rho(u)=\lim_{x\to\infty}{\Psi(x,x^{1/u})\over x",
                tex_to_color_map={
                    r"\Psi":RED,"u":TEAL,r"\rho":PINK
                })
        eqn3=TexMobject(r"u\rho'(u)+\rho(u-1)=0",
                tex_to_color_map={
                    "u":TEAL,r"\rho":PINK
                })
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
