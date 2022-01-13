from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={
                "z":YELLOW,
                "^u":BLUE,
                "{u}":BLUE,
                "y":PINK,
                r"\beta":RED
        }
        tit=TextMobject(r"Sieves \#9 (Brun's Complicated Sieve)")
        fml=TexMobject(r"\mathcal D_v=\{d|P(z):\omega((d,P_{z_n,z}))\le2b+2n-v-1,1\le n\le r\}",tex_to_color_map={r"\mathcal D":GREEN})
        fml2=TexMobject(r"{V(w)\over V(z)}\le\left(\log z\over\log w\right)^\kappa\left(1+{M\over\log w}\right)",tex_to_color_map=cm)
        fml3=TexMobject(r"P(x,y,z)=\sum_{\substack{x-y<n\le x\\p|n\Rightarrow p>z}}1",
                tex_to_color_map=cm)
        fml4=TexMobject(r"\forall {u}\beta\ge4.052,P(x,x^u,x^{1/\beta})\ge0.00825\beta{x^u\over\log x}",tex_to_color_map=cm)
        self.add(VGroup(tit,fml,fml2,fml3,fml4).arrange(DOWN))
        self.wait()
