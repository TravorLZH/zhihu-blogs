from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Critical line \#1")
        fml=TexMobject(r"\lim_{\alpha\to\pi/4^-}\int_0^\infty{\Xi(t)t^{2n}\over t^2+1/4}\cosh(\alpha t)\mathrm dt={(-1)^n\pi{\cos}(\pi/8)\over2^{2n}}",
                tex_to_color_map={
                    r"\alpha":RED,
                    r"{\Xi":GREEN,
                    r"\cosh":ORANGE,
                    r"{\cos}":BLUE
                })
        fml2=TexMobject(r"\Rightarrow N_0(T)=\sum_{\substack{\zeta(1/2+i\eta)=0\\0<\eta\le T}}1\to+\infty\quad(T\to+\infty)",
                tex_to_color_map={"T":YELLOW})
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
