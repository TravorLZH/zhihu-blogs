from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#2")
        fml=TexMobject(r"{1\over2\pi}\int_0^{2\pi}\log|f(R{e}^{it})|" \
                r"\mathrm dt=\log\left|f(0)\cdot{R\over z_1}" \
                r"\cdot{R\over z_2}\cdots{R\over z_m}\right|",
                tex_to_color_map={
                    r"\int_0^{2\pi}":RED,
                    r"\mathrm dt":RED,
                    r"\log":YELLOW,
                    "{e}":GREEN
                })
        fml2=TexMobject(r"\forall1\le{k}\le m:|z_k|<R\wedge f(z_k)=0",
                tex_to_color_map={
                    r"\forall":ORANGE,
                    r"{k}":PINK,r"_k":PINK,
                    r"\wedge":BLUE
                })
        gp=VGroup(tit,fml,fml2).arrange(DOWN)
        self.add(gp)
        self.wait()
