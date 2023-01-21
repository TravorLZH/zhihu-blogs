from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap={r"\phi":RED,r"\psi":YELLOW,"{f}":BLUE}
        eqn=TexMobject(r"\phi,\psi\uparrow\quad {f}\in C^n [x_0,+\infty)",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"{f}=O(\phi)\quad{f}^{(n)}=O(\psi)",
                tex_to_color_map=cmap)
        eqn3=TexMobject(r"\Rightarrow{f}^{(k)}=O(\phi^{1-\frac kn}\psi^{\frac kn})\quad\forall 0<k<n",
                tex_to_color_map=cmap)
        self.add(VGroup(eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
