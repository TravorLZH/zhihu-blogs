from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#3")
        fml=TexMobject(r"\sum_\rho{1\over\left|{\rho}-\frac12\right|" \
                r"^{1+\varepsilon}}<\infty",
                tex_to_color_map={
                    r"\sum":ORANGE,
                    r"_\rho":BLUE,
                    r"{\rho}":BLUE,
                })
        fml2=TexMobject(r"\xi(s)=\xi(0)\prod_\rho\left(1-{s\over\rho}\right)",
                tex_to_color_map={
                    r"\xi":RED,
                    r"\prod":ORANGE,
                    r"_\rho":BLUE,
                    r"\rho}":BLUE
                })
        gp=VGroup(tit,fml,fml2).arrange(DOWN)
        self.add(gp)
        self.wait()
