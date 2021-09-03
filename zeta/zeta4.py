from manimlib.imports import *

class Zeta4(Scene):
    def construct(self):
        t1=TextMobject("Advanced home-made summation formula")
        fml=TexMobject(r"\sum_{a<n\le b}{r}(n)f(n)=f(b)R(b)-f(a)R(a)" \
                r"-\int_a^bR(t)f'(t)\mathrm dt",
                tex_to_color_map={
                    r"\sum_{a<n\le b}":PINK,
                    "f":BLUE,
                    "{r}":RED,
                    "R":RED,
                    r"\int_a^b":ORANGE,
                    r"\mathrm dt":ORANGE
                })
        t2=TextMobject("Prime Number Theorem")
        fml2=TexMobject(r"\pi({n})" \
                r"\sim\int_2^n{\mathrm dx\over\ln x}",
                tex_to_color_map={
                    r"\pi":BLUE,
                    "{n}":YELLOW,
                    r"\int_2^n":ORANGE,
                    r"\mathrm dx":ORANGE,
                })
        gp=VGroup(t1,fml,t2,fml2).arrange(DOWN)
        self.add(gp)
        self.wait()
