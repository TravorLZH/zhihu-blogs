from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann Hypothesis \#10")
        cs={r"\chi":RED,r"^\beta":ORANGE,r"\beta}":ORANGE}
        fml=TexMobject(r"\sum_{n\le x}\chi(n)\Lambda(n)=-{x^\beta\over\beta}+\mathcal O\left\{x\exp\left(-c\sqrt{\log x}\right)\right\}",
                tex_to_color_map=cs)
        fml2=TexMobject(r"GRH\Rightarrow\pi(x;{q},{a})={\operatorname{li}(x)\over\varphi({q})}+\mathcal O(\sqrt x\log x)",
                tex_to_color_map={
                    "{q}":TEAL,"{a}":BLUE
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
