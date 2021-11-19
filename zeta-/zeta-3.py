from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        mp={r"N_0":ORANGE,r"T_0":YELLOW,r"\varepsilon":BLUE}
        tit=TextMobject(r"Critical line \#3")
        eqn=TexMobject(r"N_0(T)=\#\{0<t\le T:\zeta(1/2+it)=0\}",
                tex_to_color_map=mp)
        eqn2=TexMobject(r"\forall\varepsilon>0,\exists T_0=T_0(\varepsilon)\text{ s.t}",
                tex_to_color_map=mp)
        eqn3=TexMobject(r"\forall{T}>T_0,N_0({T})>{T}^{1/4-\varepsilon}",
                tex_to_color_map=mp)
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
