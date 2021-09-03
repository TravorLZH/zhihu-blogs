from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        eqn=TexMobject(r"{1\over m^n}={(-1)^{n-1}\over(n-1)!}\int_0^1x^{m-1}\ln^{n-1}x\mathrm dx",
                tex_to_color_map={r"\int_0^1":ORANGE,r"\mathrm dx":ORANGE,r"\ln":GREEN})
        eqn2=TexMobject(r"\sum_{n=0}^\infty{(-1)^n\over(2n+1)^3}={\pi^3\over32}",
                tex_to_color_map={
                    r"\sum_{n=0}^\infty":RED,
                    r"\pi":BLUE
                })
        self.add(VGroup(eqn,eqn2).arrange(DOWN))
        self.wait()
