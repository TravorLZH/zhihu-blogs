from manimlib.imports import *

class Ant2(Scene):
    def construct(self):
        t1=TextMobject("Home-made summation formula")
        eq1=TexMobject(r"\sum_{a\le n\le b}f(n)=\int_a^bf(x)\mathrm dx" \
                r"+\int_a^b\{x\}f'(x)\mathrm dx+\{a\}f({a})-\{b\}f({b})",
                tex_to_color_map={
                    r"\sum_{a\le n\le b}":PINK,
                    r"\int":YELLOW,
                    r"\mathrm dx":YELLOW,
                    "_a":RED,"^b":BLUE,
                    "{a}":RED,"{b}":BLUE,
                })
        t2=TextMobject("Dirichlet divisor problem")
        eq2=TexMobject(r"\sum_{n\le x}d(n)=x\ln x+(2\gamma-1)x" \
                r"+\mathcal O(x^\theta)",
                tex_to_color_map={
                    r"\sum_{n\le x}":PINK,
                    r"\gamma":RED,
                    r"\mathcal O":GREEN,
                    r"^\theta":YELLOW
                })
        gp=VGroup(t1,eq1,t2,eq2).arrange(DOWN).scale(0.9)
        self.add(gp)
        self.wait()
