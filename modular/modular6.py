from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Elliptic Modular Functions \#6")
        cmap={
            "F":RED,
            r"s(h,k)":PINK,
            r"\exp":GREEN,"{e}":GREEN,
            r"\sum":BLUE,r"\prod":ORANGE
        }
        eqn0=TexMobject(r"F(z)=1+\sum_{n\ge1}p(n){e}^{2\pi inz}=\prod_{m\ge1}(1-{e}^{2\pi imz})^{-1}",
            tex_to_color_map=cmap).scale(0.8)
        eqn=TexMobject(r"F\left(\frac hk+{iu\over k}\right)={e}^{\pi is(h,k)}u^{1/2}\exp\left[{\pi\over12k}\left(\frac1u-u\right)\right]F\left({h'\over k}+{iu^{-1}\over k}\right)",
            tex_to_color_map=cmap).scale(0.8)
        eqn2=TexMobject(r"s(h,k)=\sum_{1\le r<k}\frac rk\left({hr\over k}-\left\lfloor{hr\over k}\right\rfloor-\frac12\right),\quad hh'\equiv-1\pmod k",
            tex_to_color_map=cmap).scale(0.8)
        self.add(VGroup(tit,eqn0,eqn,eqn2).arrange(DOWN))
        self.wait()
