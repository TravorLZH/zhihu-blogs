from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#5")
        eqn=TexMobject(r"P_w(x,y,z)\ge P_w(x,t,z)-\sum_{t<{p_i}\le y}P_{w_i}\left({x\over{p_i}},z\right)",
                tex_to_color_map={
                    r"_w":PURPLE,r"_{w":PURPLE,r"_i}":YELLOW,
                    "{p":BLUE
                })
        eqn2=TexMobject(r"\lambda(5)-\int_3^4\Lambda\left(5u\over u+1\right){u+1\over u^2}\mathrm du>1.04",
                tex_to_color_map={
                    r"\int_3^4":ORANGE,r"\mathrm du":ORANGE,
                    r"\Lambda":TEAL,
                    r"\lambda":RED
                })
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
