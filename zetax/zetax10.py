from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#10")
        eqn=TexMobject(r"{L'\over L}(s,\chi)-\sum_{|t-\Im\rho|\le1}{1\over s-\rho}\ll\log q+\log(|t|+2)",
                tex_to_color_map={
                    r"\chi":RED,
                    "q":TEAL
                })
        lb=TextMobject(r"For primitive $\chi$ modulo $q>1$ and $-1\le\sigma\le2$",
                tex_to_color_map={
                    r"$\chi$":RED,
                    "$q>1$":TEAL
                })
        self.add(VGroup(tit,eqn,lb).arrange(DOWN))
        self.wait()
