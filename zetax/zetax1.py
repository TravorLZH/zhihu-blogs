from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#1")
        fml=TexMobject(
                r"\xi\left(\frac12+i{t}\right)" \
                r"=4\int_1^\infty{\mathrm d\over\mathrm dx}" \
                r"\left[\psi'(x)x^{3/2}\right]x^{-1/4}" \
                r"\cos\left(\frac12{t}\log x\right)\mathrm{d}x",
                tex_to_color_map={
                    r"\xi":BLUE,
                    r"\int_1^\infty":RED,
                    r"\mathrm{d}x":RED,
                    r"\cos":GREEN,
                    r"{t}":YELLOW,
                    r"\psi":ORANGE
                })
        gp=VGroup(tit,fml).arrange(DOWN)
        self.add(gp)
        self.wait()
