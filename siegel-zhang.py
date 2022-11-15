from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={
            "D":YELLOW,
            r"\beta":RED,
            "{a}":BLUE,
            r"\pi":GREEN,
        }
        tit=TextMobject(r"Zhang's Bound and Primes in Arithmetic Progressions")
        eqn=TexMobject(r"L(1,\chi)\gg(\log D)^{-2022}",tex_to_color_map=cmap)
        eqn1=TexMobject(r"1-\beta\gg(\log D)^{-2024}",tex_to_color_map=cmap)
        eqn2=TexMobject(r"\pi(x;D,{a})={\pi(x)\over\varphi(D)}+O(xe^{-(\log x)^{1/4048}})",tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn1,eqn2).arrange(DOWN))
        self.wait()
