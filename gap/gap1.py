from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Prime Gap \#1")
        eqn=TexMobject(r"p_n\sim n\log n",tex_to_color_map={r"\log":GREEN,"p":YELLOW})
        eqn2=TexMobject(r"\liminf_{n\to\infty}{p_{n+1}-p_n\over\log p_n}\le1",
                tex_to_color_map={r"\liminf_{n\to\infty}":BLUE,r"\log":GREEN,"p":YELLOW})
        eqn3=TexMobject(r"\limsup_{n\to\infty}{{p}_{n+1}-{p}_n\over\log{p}_n}\ge1",
                tex_to_color_map={r"\limsup_{n\to\infty}":RED,r"\log":GREEN,"{p}":YELLOW})
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
