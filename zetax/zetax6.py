from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Riemann hypothesis companion \#6")
        eqn=TexMobject(r"\forall|t|\ge2,\zeta(\sigma+it)=" \
        r"\begin{cases}" \
        r"\mathcal O(|t|^{1/2}\log|t|) & \sigma=0 \\" \
        r"\mathcal O_{a,b}(|t|^{1/2-\sigma}) & a\le\sigma\le b<0 \\" \
        r"\mathcal O_\delta(|t|^{1-\delta}) & 0<\delta<1,\sigma\ge\delta" \
        r"\end{cases}",
        tex_to_color_map={
            r"\zeta":PINK,
        })
        self.add(VGroup(tit,eqn).arrange(DOWN))
        self.wait()
