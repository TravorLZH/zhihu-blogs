from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Prime Gap \#3")
        eqn=TexMobject(r"\text{PNT + Sieve}\Rightarrow\exists\delta>0,s.t.",
                tex_to_color_map={r"\delta":RED})
        eqn2=TexMobject(r"\liminf_{n\to\infty}{p_{n+1}-p_n\over\log p_n}\le1-\delta",
                tex_to_color_map={r"\liminf_{n\to\infty}":BLUE,r"\log":GREEN,"p":YELLOW,r"\delta":RED})
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
