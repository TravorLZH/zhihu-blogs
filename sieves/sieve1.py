from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#1")
        fml0=TexMobject(r"\mathcal S(\mathcal A,\mathcal P)=\mathcal A\setminus\bigcup_{p\in\mathcal P}\mathcal A_p",
                tex_to_color_map={
                    r"\mathcal A":RED,
                    r"\mathcal P":BLUE,
                    "_p":YELLOW
                })
        fml=TexMobject(r"S(x,y;P)=\#\{x<n\le x+y:(n,P)=1\}")
        self.add(VGroup(tit,fml0,fml).arrange(DOWN))
        self.wait()
