from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann Hypothesis \#8")
        fml=TexMobject(r"L({s},\chi)=\sum_{n=1}^\infty{\chi(n)\over n^s}",
                tex_to_color_map={
                    "{s}":YELLOW,
                    "^s":YELLOW,
                    r"\chi":RED,
                    "L":BLUE
                })
        fml2=TexMobject(r"\sum_{\substack{p\le x\\p\equiv a(q)}}1\sim{1\over\varphi(q)}\sum_{p\le x}1")
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
