from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        mp={
            r"\#\{p\le x:x-p=P_2\}":ORANGE,
            r"^{\frac13}":RED,
            r"^{1\over10}":RED,r"\frac1{10}":RED,
            "w":PINK,"_j":YELLOW,"{x}":GREEN,
            "{P}":BLUE,
            r"\prod":BLUE
        }
        tit=TextMobject("Goldbach's Problem \#10")
        eqn=TexMobject(r"\#\{p\le x:x-p=P_2\}\ge{P}_w({x},1,{x}^{1\over10})",
                tex_to_color_map=mp)
        eqn2=TexMobject(r"-\frac12\sum_{{x}^{1\over10}<p_j\le{x}^{\frac13}}{P}_{w_j}({x},p_j,{x}^{1\over10})-{\Omega\over2}+O({x}^{1-\frac1{10}})",
                tex_to_color_map=mp)
        eqn3=TexMobject(r"\ge0.084\prod_{\substack{p|x\\p>2}}{p-1\over p-2}\prod_{p>2}\left(1-{1\over(p-1)^2}\right){{x}\over\log^2{x}}",tex_to_color_map=mp)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
