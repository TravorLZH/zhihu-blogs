from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                r"\prod":ORANGE,
                "{k}":YELLOW,
                r"\ell":RED,
                r"\theta":GREEN
        }
        tit=TextMobject("Bounded Gaps between Primes \#3")
        eqn=TexMobject(
                r"H=\prod_p\left(1-{\nu_p\over p}\right)" \
                r"\left(1-\frac1p\right)^{-{k}}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(
                r"{{k}(2\ell+1)\over(2\ell+{k}+1)(\ell+1)}\theta>1",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
