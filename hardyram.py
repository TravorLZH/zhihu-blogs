from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Hardy-Ramanujan Theorem:")
        eqn0=TexMobject(r"\omega(n)=\#\{p|n:p\text{ prime}\}",
                tex_to_color_map={r"\omega":YELLOW})
        eqn=TexMobject(r"\sum_{n\le x}(\omega(n)-\log\log n)^2=O(x\log\log x)",
                tex_to_color_map={r"\sum":ORANGE,r"\omega":YELLOW})
        eqn2=TexMobject(r"\Rightarrow\forall\varepsilon>0,\forall 1\le n\le x,",
                tex_to_color_map={r"\Rightarrow":GREEN,r"\varepsilon":BLUE})
        eqn3=TexMobject(r"(1-\varepsilon)\log\log n<\omega(n)<(1+\varepsilon)\log\log n",
                tex_to_color_map={r"\varepsilon":BLUE,r"\omega":YELLOW})
        eqn4=TextMobject("holds with $o(x)$ exceptions.")
        self.add(VGroup(tit,eqn0,eqn,eqn2,eqn3,eqn4).arrange(DOWN))
        self.wait()
