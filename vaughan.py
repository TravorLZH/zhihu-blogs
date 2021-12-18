from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={"F":RED,"G":BLUE,r"\zeta":PINK,"U":YELLOW,"V":TEAL}
        tit=TextMobject("Vaughan's Identity")
        eqn=TexMobject(r"F(s)=\sum_{n\le U}{\Lambda(n)\over n^s},\quad"
                +r" G(s)=\sum_{n\le V}{\mu(n)\over n^s}",
                tex_to_color_map=cm)
        eqn2=TexMobject(r"-{\zeta'\over\zeta}(s)&="
                +r"F-\zeta(s)F(s)G(s)-\zeta'(s)G(s)"
                +r"\\&+\left({-\zeta'\over\zeta}(s)-F(s)\right)"
                +r"(1-\zeta(s)G(s))",
                tex_to_color_map=cm)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
