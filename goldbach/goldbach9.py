from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        mp={
            r"\#\{p\le x:x-p=P_3\}":ORANGE,
            r"^{\frac13}":RED,
            r"^{1\over10}":RED,r"\frac1{10}":RED,
            "w":PINK,"_j":YELLOW,"{x}":GREEN,
            "{P}":BLUE
        }
        tit=TextMobject("Goldbach's Problem \#9")
        eqn=TexMobject(r"\#\{p\le x:x-p=P_3\}\ge{P}_w({x},1,{x}^{1\over10})",
                tex_to_color_map=mp)
        eqn2=TexMobject(r"-\frac12\sum_{{x}^{1\over10}<p_j\le{x}^{\frac13}}{P}_{w_j}({x},p_j,{x}^{1\over10})+O({x}^{1-\frac1{10}})",
                tex_to_color_map=mp)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
