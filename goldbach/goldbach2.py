from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#2")
        eqn=TexMobject(r"{c}_x=2e^{-2\gamma}\prod_{\substack{p|x\\p>2}}{p-1\over p-2}\prod_{p>2}{p(p-2)\over(p-1)^2}",
                tex_to_color_map={"{c}":RED,r"\prod":ORANGE})
        eqn1=TexMobject(r"P_w(x,x^{1/10})\ge77{c_xx\over\log^2x}",
                tex_to_color_map={"P":BLUE,"c":RED,"^{1/10}":YELLOW,"_w":PINK})
        eqn2=TextMobject(r"$\Rightarrow$ Every large even integer is a sum of two products,")
        eqn3=TextMobject("each having at most 9 prime factors")
        self.add(VGroup(tit,eqn,eqn1,eqn2,eqn3).arrange(DOWN))
        self.wait()
