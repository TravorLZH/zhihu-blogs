from manimlib.imports import *

class FuncsScene(Scene):
    def construct(self):
        fc=TexMobject(r"\Gamma(z)",r"\Gamma(1-z)","={\pi\over\sin(\pi z)}")
        fc[0].set_color(RED)
        fc[1].set_color(YELLOW)
        fc2=TexMobject(r"\zeta(s)","=",r"\sum_{k=1}^\infty",r"{1\over k^s}")
        fc2[0].set_color(ORANGE)
        fc2[2].set_color(GREEN)
        fc3=TexMobject(r"\sum_{n=1}^\infty",r"n^{-n}","=",
            r"\int_0^1","x^{-x}",r"\mathrm{d}x")
        fc3[0].set_color(BLUE)
        fc3[3].set_color(ORANGE)
        fc3[5].set_color(ORANGE)
        fc4=TexMobject(r"\iint\limits",r"_{[0,1]\times[0,1]}",r"{1\over1-xy}",
            r"\mathrm{d}x\mathrm{d}y")
        fc4[0].set_color(PINK)
        fc4[1].set_color(BLUE)
        fc4[3].set_color(PINK)
        gp=VGroup(VGroup(fc,fc2).arrange(RIGHT),
            VGroup(fc3,fc4).arrange(RIGHT)).arrange(DOWN)
        self.add(gp)
        self.wait()
