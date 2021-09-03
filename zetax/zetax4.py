from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#4")
        fml=TexMobject(r"{1\over2\pi}\Delta_\gamma\arg[{f}(z)]={1\over2\pi{i}}\oint_\gamma{f'\over f}(z)\mathrm dz",
                tex_to_color_map={
                    r"\arg":YELLOW,
                    r"_\gamma":GREEN,
                    r"\oint":RED,
                    r"\mathrm dz":RED,
                    r"f'\over f":ORANGE,
                    "{f}":ORANGE,
                    r"\pi":PINK,
                    r"{i}":BLUE
                })
        self.add(VGroup(tit,fml).arrange(DOWN))
        self.wait()
