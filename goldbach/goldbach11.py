from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#11")
        eqn=TexMobject(r"S(\alpha,N)=\sum_{p\le N}e(p\alpha)\log p",
                tex_to_color_map={
                    "S":BLUE,r"\alpha":ORANGE
                })
        eqn2=TexMobject(r"{v}(n)=\sum_{p_1+p_2=n}\log p_1\log p_2=\int_0^1S^2(\alpha,N)e(-n\alpha)\mathrm d\alpha",
                tex_to_color_map={
                    r"\int_0^1":ORANGE,r"\mathrm d":ORANGE,
                    r"\alpha":ORANGE,"S":BLUE,"{v}":PINK
                })
        eqn3=TexMobject(r"\sum_{\substack{n\le x\\2|n}}[{v}(n)-2n\mathfrak S(n)]^2\ll{x\over\log^Ax}",
                tex_to_color_map={
                    r"\sum":RED,
                    "{v}":PINK,r"\mathfrak S":YELLOW
                })
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
