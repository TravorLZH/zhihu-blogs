from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={r"\varphi":YELLOW,r"\sigma":RED,r"M":ORANGE,r"\delta":BLUE}
        tit=TextMobject("Phragmén-Lindelöf Theorems")
        eqn=TexMobject(r"|\varphi(a+it)|\le M,|\varphi(b+it)|\le M",
                tex_to_color_map=cm)
        eqn2=TexMobject(r"\forall a\le\sigma\le b,\forall\delta>0,\varphi(\sigma+it)\ll_\delta e^{\delta t}\text{ as }t\to+\infty",
                tex_to_color_map=cm)
        eqn3=TexMobject(r"\Rightarrow|\varphi(\sigma+it)|\le M\text{ for }a\le\sigma\le b,t\ge0",
                tex_to_color_map=cm)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
