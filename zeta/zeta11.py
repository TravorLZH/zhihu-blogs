from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann Hypothesis \#11")
        t1=TextMobject("Siegel's theorem");
        fml=TexMobject(r"L(1,\chi)\gg_\varepsilon q^{-\varepsilon}",
                tex_to_color_map={r"\chi":RED,"q":TEAL})
        t2=TextMobject("Siegel-Walfisz theorem");
        fml2=TexMobject(r"\pi(x;{q},a)={\operatorname{li}(x)\over\varphi({q})}+\mathcal O_A\left\{x(\log x)^{-A}\right\}",
                tex_to_color_map={"{q}":TEAL})
        self.add(VGroup(tit,t1,fml,t2,fml2).arrange(DOWN))
        self.wait()
