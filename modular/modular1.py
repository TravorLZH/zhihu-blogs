from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#1")
        cmap={
            r"\int":BLUE,
            r"\mathrm du":BLUE,
            "k":RED,
            "{w}":PURPLE,
            "_0":YELLOW,"{z}":YELLOW,
            "{K}":GREEN,"{K'}":ORANGE
        }
        eqn=TexMobject(r"F(z;k)=\int_0^z{\mathrm du\over\sqrt{1-k^2u^2}\sqrt{1-u^2}}",tex_to_color_map=cmap)
        eqn2=TexMobject(r"{w}=F({z};k),{z}=\operatorname{sn}({w};k)",
                tex_to_color_map=cmap)
        eqn3=TexMobject(r"{K}=F(1;k)\Rightarrow\operatorname{sn}({w})=\operatorname{sn}({w}+4{K};k)",
                tex_to_color_map=cmap)
        eqn4=TexMobject(r"{K'}=F(1;\sqrt{1-k^2})\Rightarrow\operatorname{sn}({w})=\operatorname{sn}({w}+2i{K'};k)",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3,eqn4).arrange(DOWN))
        self.wait()
