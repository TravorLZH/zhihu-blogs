from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#7")
        cmap={
            r"s(h,k)":PINK,
            "{e}":GREEN,
            r"\sum":BLUE,"A_k(n)":RED
        }
        eqn=TexMobject(r"p(n)={1\over\pi\sqrt2}\sum_{k\ge1}A_k(n)\sqrt k{\mathrm d\over\mathrm dn}\left(\sinh(B \lambda_n /k)\over\lambda_n\right)",
            tex_to_color_map=cmap).scale(0.8)
        eqn2=TexMobject(r"\lambda_n=\sqrt{n-{1\over24}},\quad B=\pi\sqrt{\frac23}",
            tex_to_color_map=cmap).scale(0.8)
        eqn3=TexMobject(r"A_k(n)=\sum_{\substack{1\le h\le k\\(h,k)=1}}{e}^{i\pi s(h,k)-2\pi inh/k}",
            tex_to_color_map=cmap).scale(0.8)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
