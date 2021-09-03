from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#5")
        fml=TexMobject(r"\sum_{\scriptstyle p\le x" \
                r"\atop\scriptstyle p\equiv h\text{ (mod }k)}" \
                r"{\log{p}\over{p}}={\log x\over\varphi(k)}+\mathcal O(1)",
                tex_to_color_map={
                    r"\sum":RED,
                    #r"\sum_{\scriptstyle p\le x\atop\scriptstyle p\equiv h\pmod k}":RED,
                    r"\varphi":YELLOW,
                    r"\mathcal O":GREEN
                })
        self.add(VGroup(tit,fml).arrange(DOWN))
        self.wait()
