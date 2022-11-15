from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={
            "D":YELLOW,
            r"\beta":RED
        }
        tit=TextMobject(r"Siegel Zeros and $L(1,\chi)$")
        eqn=TexMobject(r"1-\beta\gg(\log D)^{-2}L(1,\chi)",tex_to_color_map=cmap)
        eqn2=TexMobject(r"L(1,\chi)\gg(1-\beta)D^{-\frac12(1-\beta)}",tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
