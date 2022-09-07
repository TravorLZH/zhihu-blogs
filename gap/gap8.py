from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                r"\liminf":ORANGE,
                "p":BLUE
        }
        tit=TextMobject("Bounded Gaps between Primes \#5")
        tx=TextMobject(r"\textbf{Theorem (Zhang, 2014):}")
        eqn=TexMobject(
                r"\liminf_{n\to\infty}(p_{n+1}-p_n)<7\times10^7",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,tx,eqn).arrange(DOWN))
        self.wait()
