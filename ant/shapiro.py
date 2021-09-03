from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#3")
        fml=TexMobject(r"\sum_{p\le{x}}\log p" \
                r"\left\lfloor{x}\over p\right\rfloor" \
                r"={x}\log{x}+\mathcal O({x})",
                tex_to_color_map={
                    r"\sum":RED,
                    "p":BLUE,
                    r"\mathcal O":GREEN,
                    "{x}":YELLOW
                })
        fml2=TexMobject(r"\Rightarrow" \
                r"{Mx\over\log x}\le\pi(x)\le{Nx\over\log x}",
                tex_to_color_map={
                    "M":RED,"N":ORANGE,"x":YELLOW,
                    r"\pi":PINK
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
