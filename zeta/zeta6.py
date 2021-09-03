from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann Hypothesis \#6")
        fml=TexMobject(r"N({T})={T\over2\pi}\log{T\over2\pi}-{T\over2\pi}+\mathcal O(\log{T})",
                tex_to_color_map={
                    r"{T":YELLOW,
                    r"N":ORANGE,
                    r"\log":GREEN,
                })
        self.add(VGroup(tit,fml).arrange(DOWN))
        self.wait()
