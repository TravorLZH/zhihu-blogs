from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#4")
        cmap={
                "F":RED,r"\exp":GREEN,r"\sum_{n\ge1}":BLUE,r"\prod_{k\ge1}":ORANGE
        }
        eqn=TexMobject(r"F(z)=1+\sum_{n\ge1}p(n)e^{2\pi inz}=\prod_{k\ge1}{1\over1-e^{2\pi ikz}}",
            tex_to_color_map=cmap)
        eqn2=TexMobject(r"F(z)=\left(\frac zi\right)^{1/2}\exp\left[{2\pi i\over24}\left(z+\frac1z\right)\right]F\left(-\frac1z\right)",
            tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
