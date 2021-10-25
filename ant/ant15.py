from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={r"\prod":ORANGE,r"\log":GREEN,"r(N)":BLUE,"A":RED}
        tit=TextMobject(r"Analytic Number Theory \#15")
        eqn=TexMobject(r"r(N)=\#\{p\le N:N-p\text{ prime}\}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"\forall 2|N,r(N)\sim{AN\over(\log N)^2}\prod_{\substack{{p}|N\\ {p}>2}}{{p}-1\over {p}-2}",tex_to_color_map=cmap)
        eqn3=TexMobject(r"\Rightarrow A=2\prod_{{p}>2}\left(1-{1\over({p}-1)^2}\right)",tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
