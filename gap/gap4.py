from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                r"\mathcal H":BLUE,
                "{h}":YELLOW,
                r"\chi":RED,
                r"_\mathbb P":GREEN,
                r"\sum":ORANGE,
                "Q":PINK
        }
        tit=TextMobject("Bounded Gaps between Primes \#1")
        eqn=TexMobject(r"\mathcal H=\{h_1,h_2,\dots,h_k\}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"Q(n)=(n+h_1)(n+h_2)\cdots(n+h_k)",
                tex_to_color_map=cmap)
        eqn3=TexMobject(r"\sum_{N<n\le2N}\left(\sum_{{h}\in\mathcal H}\chi_\mathbb P( n+{h})-1\right)\Bigg(\sum_{d|Q(n)}\lambda_d\Bigg)^2",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
