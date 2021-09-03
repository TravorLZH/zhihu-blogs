from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann Hypothesis \#5")
        fml=TexMobject(r"\Pi_0(x)=\operatorname{li}(x)-\sum_\rho\operatorname{li}(x^\rho)-\log2+\int_x^\infty{\mathrm dt\over t(t^2-1)\log t}",
                tex_to_color_map={
                    r"\Pi_0":PINK,
                    r"\operatorname{li}":YELLOW,
                    r"_\rho":BLUE,
                    r"^\rho":BLUE,
                    r"\int_x^\infty":RED,
                    r"\mathrm dt":RED
                })
        fml2=TexMobject(r"\pi(x)\approx\sum_{n\le\log_2x}{\mu(n)\operatorname{li}(x^{1/n})\over n}",
                tex_to_color_map={
                    r"\pi":ORANGE,
                    r"\operatorname{li}":YELLOW,
                    r"\mu":GREEN
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
