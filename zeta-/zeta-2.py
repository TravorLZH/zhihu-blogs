from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Critical line \#2")
        fml=TexMobject(r"N(\sigma,T)=\{\rho:\Re(\rho)\ge\sigma,0<\Im(\rho)\le T\}")
        fml2=TexMobject(r"\forall\sigma>1/2,\lim_{T\to\infty}{N(\sigma,T)\over N(T)}=0",tex_to_color_map={r"\sigma":YELLOW})
        fml3=TexMobject(r"\Rightarrow\text{Almost all nontrivial zeros lie near }\Re(s)=1/2")
        self.add(VGroup(tit,fml,fml2,fml3).arrange(DOWN))
        self.wait()
