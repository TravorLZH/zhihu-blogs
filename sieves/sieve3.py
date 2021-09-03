from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#3")
        fml0=TexMobject(r"\#\{p\le x:p+2\text{ prime}\}\ll{x(\log\log x)^2\over\log^2x}")
        fml=TexMobject(r"\sum_{\substack{p\le x\\p+2\text{ prime}}}\left[\frac1p+{1\over p+2}\right]=B_2+\mathcal O\left\{(\log\log x)^2\over\log x\right\}",
                tex_to_color_map={
                    r"B_2":YELLOW,
                    r"\sum":ORANGE})
        self.add(VGroup(tit,fml0,fml).arrange(DOWN))
        self.wait()
