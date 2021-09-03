from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#9")
        fml=TexMobject(r"G(n,\chi)=\sum_{r\in\mathbb Z_q}\chi(r)e^{2\pi irn/{q}}",
                tex_to_color_map={
                    r"\chi":RED,
                    "G":GREEN,
                    "{q}":TEAL,
                    r"\mathbb Z_q":TEAL
                })
        fml2=TexMobject(r"\forall (n,q)=1,G(n,{\chi})={\overline\chi}(n)G(1,{\chi})",
                tex_to_color_map={
                    r"{\chi}":RED,
                    r"{\overline\chi}":ORANGE,
                    "G":GREEN,
                    "q":TEAL,
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
