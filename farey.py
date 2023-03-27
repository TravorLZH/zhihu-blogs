from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Farey Fractions and the Circle Method")
        cmap={
                r"\frac aq":YELLOW,
                r"_{a/q}":YELLOW,
                r"\bigcup":BLUE,
                "I":RED,
                r"{1\over N+1}":ORANGE
        }
        eqn=TexMobject(r"I_{a/q}=\left[\frac aq-{1\over q(q+q_1)},\frac aq+{1\over q(q+q_2)}\right)",
                tex_to_color_map=cmap)
        eqn2=TexMobject(r"\left[{1\over N+1},1+{1\over N+1}\right)=\bigcup_{\substack{1\le a\le q\le N\\(a,q)=1}}I_{a/q}",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
