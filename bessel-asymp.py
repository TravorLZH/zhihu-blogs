from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Asymptotics for Bessel functions of the 1st kind")
        eqn=TexMobject(r"J_m(z)=\sum_{r\ge0}{(-1)^r\over{r}!\Gamma({m}+{r}+1)}\left(z\over2\right)^{m+2{r}}",
                tex_to_color_map={r"\sum":ORANGE,
                    r"_{r\ge0}":PINK,
                    "^r":PINK,"{r}":PINK,
                    "_m":BLUE,"^{m":BLUE,
                    "{m}":BLUE,"z":YELLOW,
                    r"\Gamma":RED,"J":GREEN})
        eqn2=TexMobject(r"J_m(z)\sim\sqrt{2\over\pi z}\cos\left(z-{\pi{m}\over2}-\frac\pi4\right),\quad|z|\to\infty",
                tex_to_color_map={"_m":BLUE,"{m}":BLUE,"z":YELLOW,"J":GREEN})
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
