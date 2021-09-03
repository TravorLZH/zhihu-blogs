from manimlib.imports import *

class MellinScene(Scene):
    def construct(self):
        fml=TexMobject(r"\sum_{p^n\le x}",r"\frac1n","=",r"{1\over2\pi i}",
                r"\int_{a-i\infty}^{a+i\infty}",r"\ln",r"\zeta","(","s",
                ")","x^s",r"{\mathrm ds\over"," s}").scale(1.5)
        fml[0].set_color(ORANGE)
        fml[1].set_color(YELLOW);
        fml[3].set_color(BLUE)
        fml[4].set_color(PINK)
        fml[5].set_color(RED)
        fml[6].set_color(GREEN)
        fml[8].set_color(YELLOW)
        fml[11].set_color(PINK)
        fml[12].set_color(YELLOW)
        self.add(fml)
        self.wait()
