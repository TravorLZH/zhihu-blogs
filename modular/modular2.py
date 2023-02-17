from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#2")
        cmap={
            r"\tau":YELLOW,
            r"J":RED,
            r"\mathbb H":ORANGE,
            r"\mathbb Z":GREEN,
            r"\wp":PINK,
        }
        eqn=TexMobject(r"(\wp')^2=4\wp^3-g_2\wp-g_3",
            tex_to_color_map=cmap)
        eqn2=TexMobject(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z),\quad\tau\in\mathbb H",
            tex_to_color_map=cmap)
        eqn3=TexMobject(r"\Rightarrow J\left(a\tau+b\over c\tau+d\right)=J(\tau)",
            tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
