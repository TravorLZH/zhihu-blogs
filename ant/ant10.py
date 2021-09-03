from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#10")
        cs={r"\varphi":ORANGE,
                r"\sum":GREEN,
                r"\pi":BLUE,
                "{e}":RED,
                r"\varlimsup":YELLOW,
                r"\varliminf":YELLOW}
        fml0=TexMobject(r"\sum_{n\le x}\varphi(n)={3x^2\over\pi^2}+\mathcal O(x\log x)",tex_to_color_map=cs)
        fml=TexMobject(r"\varlimsup_{n\to\infty}{\varphi(n)\over n}=1",
                tex_to_color_map=cs)
        fml2=TexMobject(r"\varliminf_{n\to\infty}{\varphi(n)\log\log n\over n}={e}^{-\gamma}",tex_to_color_map=cs)
        self.add(VGroup(tit,fml0,fml,fml2).arrange(DOWN))
        self.wait()
