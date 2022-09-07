from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                r"\theta":GREEN,
                r"\int_0^1":ORANGE,
                r"\mathrm dx":ORANGE,
                "P":BLUE
        }
        tit=TextMobject("Bounded Gaps between Primes \#4")
        eqn=TexMobject(
                r"\lambda_d=\mu(d)P\left(\log R/d\over\log R\right)",
                tex_to_color_map=cmap)
        eqn2=TexMobject(
                r"\int_0^1x^{k-2}[P^{(k-1)}(1-x)]^2\mathrm dx",
                tex_to_color_map=cmap)
        eqn3=TexMobject(
                r">{2\over\theta k(k-1)}\int_0^1x^{k-1}[P^{(k)}(1-x)]^2\mathrm dx",tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
