from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Prime Gap \#2")
        eqn=TexMobject(r"\zeta(\rho)=0\Rightarrow\Re(\rho)\le\Theta",
                tex_to_color_map={r"\zeta":PINK,r"\rho":BLUE})
        eqn2=TexMobject(r"\Rightarrow p_{n+1}-p_n=O(p_n^\Theta\log p_n)",
                tex_to_color_map={"p":YELLOW})
        eqn3=TexMobject(r"RH \Rightarrow p_{n+1}-p_n=O(p_n^{1/2}\log p_n)",
                tex_to_color_map={"p":YELLOW})
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
