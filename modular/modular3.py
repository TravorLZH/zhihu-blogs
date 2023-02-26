from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#3")
        cmap={
            "{f}":RED,"z":YELLOW,"M":ORANGE
        }
        eqn=TexMobject(r"{f}\left(az+b\over cz+d\right)=(cz+d)^kf(z)",
            tex_to_color_map=cmap)
        eqn2=TexMobject(r"\dim M_k=\begin{cases}\lfloor k/12\rfloor & k\equiv2\pmod{12} \\\lfloor k/12\rfloor+1 & k\not\equiv2\pmod{12}\end{cases}",
            tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
