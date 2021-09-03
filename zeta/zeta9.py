from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cs={"q":TEAL,r"\chi":RED,r"\beta":ORANGE}
        tit=TextMobject(r"Riemann Hypothesis \#9")
        fml=TexMobject(r"3+4\cos\theta+\cos2\theta\ge0",
                tex_to_color_map={r"\theta":YELLOW})
        fml1=TexMobject(r"\Rightarrow\text{ Zero-free region for }L(s,\chi)",tex_to_color_map=cs)
        tit2=TextMobject("Landau-Siegel zeros")
        fml2=TexMobject(r"\forall\text{ real }\chi\text{ mod }q,\exists\text{ at most one }0<\beta_q<1",tex_to_color_map=cs)
        fml3=TexMobject(r"\text{s.t. }L(\beta_q,\chi)=0\wedge" \
                r"\lim_{q\to\infty}(1-\beta_q)\log q=0",
                tex_to_color_map=cs)
        self.add(VGroup(tit,fml,fml1,tit2,fml2,fml3).arrange(DOWN))
        self.wait()
