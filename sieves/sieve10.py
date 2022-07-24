from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={
                "R":BLUE,
                r"\lambda":RED,
                "_d":YELLOW,
                "{d}":YELLOW,
                "^k":PURPLE
        }
        tit=TextMobject(r"Sieves \#10")
        fml=TexMobject(r"\Bigg(\sum_{{d}|n}\lambda_d\Bigg)^2\ge\sum_{{d}|n}\mu({d})",tex_to_color_map=cm)
        fml2=TexMobject(r"\lambda_d\sim\mu({d})\left(\log R/{d}\over\log R\right)^k",tex_to_color_map=cm)
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
