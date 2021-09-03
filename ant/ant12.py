from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#12")
        tit2=TextMobject("Twin Prime Conjecture")
        fml0=TexMobject(r"\pi_2(x)\sim{Kx\over\log^2x}",
                tex_to_color_map={
                    "K":RED,
                    r"\pi_2":GREEN
                })
        fml=TexMobject(r"K=2\prod_{p\ge3}\left[1-{1\over({p}-1)^2}\right]",
                tex_to_color_map={
                    "K":RED,
                    r"\prod":ORANGE,
                    r"_{p\ge3}":BLUE,
                    r"{p}":BLUE
                })
        self.add(VGroup(tit,tit2,fml0,fml).arrange(DOWN))
        self.wait()
