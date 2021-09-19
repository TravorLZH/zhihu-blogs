from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#11")
        lb=TextMobject(r"For primitive $\chi$ modulo $q$")
        eqn=TexMobject(
                r"\frac12\sum_{\substack{L(\rho,\chi)=0\\|\Im\rho|\le T}}1" \
                r"={T\over2\pi}\log{qT\over2\pi}-{T\over2\pi}+\mathcal O(\log qT)",
                tex_to_color_map={
                    r"\chi":RED,
                    r"\rho":BLUE,
                })
        self.add(VGroup(tit,lb,eqn).arrange(DOWN))
        self.wait()
