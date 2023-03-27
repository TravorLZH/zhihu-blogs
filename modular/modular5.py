from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#5")
        cmap={
            r"\exp":GREEN,
            "{n}":YELLOW,
        }
        eqn=TexMobject(r"p({n})\sim{1\over4{n}\sqrt3}\exp\left(\pi\sqrt{2{n}\over3}\right)",tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn).arrange(DOWN))
        self.wait()
