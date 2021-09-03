from manimlib.imports import *

class GammaDefScene(Scene):
    def construct(self):
        fml=TexMobject(r"\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\mathrm dt",
                tex_to_color_map={
                    r"\Gamma":PURPLE,
                    r"s":YELLOW,
                    r"\int_0^\infty":RED,
                    r"\mathrm dt":RED
                }).scale(2)
        self.add(fml)
        self.wait()
