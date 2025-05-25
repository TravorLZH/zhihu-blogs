from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        mp={r"N_0":ORANGE,r"T":YELLOW,r"\varepsilon":BLUE}
        tit=TextMobject(r"Critical line \#4")
        tx=TextMobject(r"\textbf{Theorem (Hardy-Littlewood, 1921):}")
        eqn=TexMobject(r"N_0(T)>CT",
                tex_to_color_map=mp)
        self.add(VGroup(tit,tx,eqn).arrange(DOWN))
        self.wait()
