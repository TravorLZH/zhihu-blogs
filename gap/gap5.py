from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                "y":BLUE,"g":GREEN,"h":PINK,
                r"\sum":ORANGE,r"\prod":ORANGE,
                r"\lambda":RED
        }
        tit=TextMobject("Bounded Gaps between Primes \#2")
        eqn=TexMobject(
                r"y_m=g(m)\sum_{\substack{n\\(n,m)=1}}g(n)\lambda_{nm}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"h(d)=\prod_{p|d}{g(p)\over1-g(p)}",
                tex_to_color_map=cmap)
        eqn3=TexMobject(
                r"\sum_{d_1,d_2}g([d_1,d_2])\lambda_{d_1}\lambda_{d_2}" \
                r"=\sum_m{y_m^2\over h(m)}",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
