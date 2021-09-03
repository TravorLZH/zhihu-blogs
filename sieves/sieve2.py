from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#2")
        fml0=TexMobject(r"S(x,y;P)={\varphi(P)\over P}y+\mathcal O(2^{\omega(P)})",
                tex_to_color_map={
                    "P":BLUE,
                    r"\varphi":GREEN,
                    r"^{\omega":ORANGE
                })
        fml=TexMobject(r"\sum_{\substack{x<p\le x+y\\p\equiv a(q)}}1\ll{y\over\varphi(q)\log\log y/q}",
                tex_to_color_map={
                    r"\varphi":GREEN
                })
        self.add(VGroup(tit,fml0,fml).arrange(DOWN))
        self.wait()
