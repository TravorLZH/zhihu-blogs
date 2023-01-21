from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={"{D}":YELLOW,r"\mathbb C":BLUE,r"{\partial D}":RED}
        eqn=TexMobject(r"f\text{ analytic in }{D}\text{ \& injective on }{\partial D}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"\Rightarrow f\text{ injective in }{D},",
                tex_to_color_map=cmap)
        eqn3=TexMobject(r"\Rightarrow\partial[f({D})]=f({\partial D}),",
                tex_to_color_map=cmap)
        eqn4=TexMobject(r"\Rightarrow f'(z)\ne0\forall z\in{D},",
                tex_to_color_map=cmap)
        eqn5=TexMobject(r"\Rightarrow f^{-1}\text{ analytic in }f({D}).",
                tex_to_color_map=cmap)
        self.add(VGroup(eqn,eqn2,eqn3,eqn4,eqn5).arrange(DOWN))
        self.wait()
