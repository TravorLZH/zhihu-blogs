from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Karamata's Tauberian Theorem:")
        eqn=TexMobject(r"\sum_{n\ge0}|a_n|{x}^n\sim(1-{x})^{-{k}}\text{ as }{x}\to1^-",
                tex_to_color_map={"{k}":YELLOW,r"{x}":BLUE})
        eqn2=TexMobject(r"\Rightarrow\sum_{n\le y}|a_n|\sim{{y}^k\over\Gamma({k}+1)}\text{ as }{y}\to+\infty",
                tex_to_color_map={r"\Gamma":RED,r"_{n\le y}":GREEN,r"{y}":GREEN,r"^k":YELLOW,
                    "{k}":YELLOW})
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
