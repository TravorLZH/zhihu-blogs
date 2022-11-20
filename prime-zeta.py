from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={
            r"\zeta":YELLOW,
            "P":BLUE
        }
        eqn=TexMobject(r"\zeta(s)=1^{-s}+2^{-s}+3^{-s}+4^{-s}+\dots=\sum_{n\ge1}n^{-s}",tex_to_color_map=cmap)
        eqn1=TexMobject(r"P(s)=2^{-s}+3^{-s}+5^{-s}+7^{-s}+\dots=\sum_pp^{-s}",tex_to_color_map=cmap)
        eqn2=TexMobject(r"\zeta(-1)=-{1\over12},\quad P(-1)=?",tex_to_color_map=cmap)
        self.add(VGroup(eqn,eqn1,eqn2).arrange(DOWN))
        self.wait()
