from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                "M":ORANGE,
                "_k":PINK,
                "I":BLUE,
                "J":RED,
                "F":YELLOW,
                r"\sum":GREEN
        }
        tit=TextMobject("Bounded Gaps between Primes \#6")
        eqn=TexMobject(r"w_n=\sum_{\substack{d_1,\dots,d_k\\d_i|(n+h_i)\forall i}}\lambda_{d_1,\dots,d_k}",tex_to_color_map=
                {r"\sum":GREEN,"w":RED,r"\lambda":ORANGE})
        eqn2=TexMobject(
                r"M_k=\sup_F{\sum_mJ^{(m)}_k(F)\over I_k(F)}",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
