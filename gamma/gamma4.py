from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        eqn=TexMobject(r"s=\sigma+it")
        eqn2=TexMobject(r"\log\Gamma(s)=\left(s-\frac12\right)\log(it)-it+\frac12\log2\pi+\mathcal O_\sigma\left(1\over|t|\right)",
                tex_to_color_map={
                    r"\Gamma":RED,r"\mathcal O":GREEN
                })
        eqn3=TexMobject(r"\left|\zeta(s)\over\zeta(1-s)\right|\sim\left(|t|\over2\pi\right)^{1/2-\sigma}")
        self.add(VGroup(eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
