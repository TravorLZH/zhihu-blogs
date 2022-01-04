from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={
                r"\mathcal A":RED,
                r"\mathcal P":BLUE,
                "z":YELLOW,
                r"\chi":ORANGE
        }
        tit=TextMobject(r"Sieves \#8 (Combinatorial Foundations)")
        fml=TexMobject(r"\forall v\in\{1,2\},pd|P(z),p<p^-(d)",tex_to_color_map=cm)
        fml2=TexMobject(r"(-1)^{v-1}\mu(d)[\chi_v(d)-\chi_v(pd)]\ge0",tex_to_color_map=cm)
        fml3=TexMobject(r"\Rightarrow S(\mathcal A,\mathcal P,z)\le\sum_{d|P(z)}\mu(d)\chi_1(d)|\mathcal A_d|",tex_to_color_map=cm)
        fml4=TexMobject(r"\Rightarrow S(\mathcal A,\mathcal P,z)\ge\sum_{d|P(z)}\mu(d)\chi_2(d)|\mathcal A_d|",tex_to_color_map=cm)
        self.add(VGroup(tit,fml,fml2,fml3,fml4).arrange(DOWN))
        self.wait()
