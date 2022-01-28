from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#4")
        eqn=TexMobject(r"\Lambda(\alpha)={2e^{2\gamma}\alpha^2\over(\alpha-1)^2-2\left(\alpha\over2\right)^2\log{\alpha\over2}}\quad2\le\alpha\le4",
                tex_to_color_map={r"\Lambda":TEAL,r"\alpha":RED})
        eqn2=TexMobject(r"P_w({x},{x}^{1/5})\ge9.18{c_x{x}\over\log^2{x}}",
                tex_to_color_map={r"_w":PURPLE,"P":BLUE,
                    "{x}":YELLOW,"_x":YELLOW})
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
