from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#6")
        fml=TexMobject(r"\lim_{x\to\infty}{1\over\log x}\prod_{p\le x}{1\over1-p^{-1}}={e}^\gamma",
                tex_to_color_map={
                    r"\lim_{x\to\infty}":PINK,
                    r"\prod":ORANGE,
                    r"{e}":RED,
                    r"^\gamma":YELLOW,
                    r"\log":GREEN
                })
        fml2=TexMobject(r"\varliminf_{x\to\infty}{\pi(x)\log x\over x}\le1\le\varlimsup_{x\to\infty}{\pi(x)\log x\over x}",
                tex_to_color_map={
                    r"\varliminf_{x\to\infty}":PINK,
                    r"\varlimsup_{x\to\infty}":PINK,
                    r"\pi":BLUE,
                    r"\log":GREEN
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
