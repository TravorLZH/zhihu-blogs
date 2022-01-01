from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#1")
        eqn=TexMobject(r"\mathfrak S(N)=\prod_{\substack{p|N\\p>2}}{p-1\over p-2}\prod_{p>2}{p(p-2)\over(p-1)^2}",
                tex_to_color_map={r"\mathfrak S":ORANGE,r"\prod":BLUE})
        eqn1=TexMobject(r"{r}(N)=\#\{p\le N:N-p\text{ prime}\}",
                tex_to_color_map={"{r}":RED})
        eqn2=TexMobject(r"{r}(N)\sim{2N\over(\log N)^2}\mathfrak S(N)",
                tex_to_color_map={r"\mathfrak S":ORANGE,"{r}":RED})
        self.add(VGroup(tit,eqn,eqn1,eqn2).arrange(DOWN))
        self.wait()
