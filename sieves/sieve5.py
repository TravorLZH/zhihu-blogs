from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#5 (The Large Sieve)")
        cm={r"\alpha":RED,r"\delta":YELLOW}
        fml0=TexMobject(r"\forall r\ne s," \
                r"\min_{n\in\mathbb Z}|\alpha_r-\alpha_s-n|\ge\delta",
                tex_to_color_map=cm)
        fml=TexMobject(r"S(\alpha)=\sum_{M<n\le M+N}a_ne^{2\pi in\alpha}",
                tex_to_color_map=cm)
        fml2=TexMobject(r"\Rightarrow\sum_{1\le r\le R}|S(\alpha_r)|^2\le\Delta\sum_{M<n\le M+N}|a_n|^2",tex_to_color_map=cm)
        fml3=TexMobject(r"\text{Theorem (Rényi): }\Delta=N+3\delta^{-1}",
                tex_to_color_map=cm)
        self.add(VGroup(tit,fml0,fml,fml3,fml2).arrange(DOWN))
        self.wait()
