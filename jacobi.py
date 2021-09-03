from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Jacobi's triple product identity")
        fml=TexMobject(r"\prod_{r=1}^\infty[(1-q^{2r})" \
                r"(1+q^{2r-1}z)(1+q^{2r-1}z^{-1})]" \
                r"=\sum_{k\in\mathbb Z}q^{k^2}z^k",
                tex_to_color_map={
                    r"\prod_{r=1}^\infty":RED,
                    r"\sum_{k\in":PINK,
                    r"\mathbb Z}":YELLOW,
                    "q":TEAL
                })
        tit2=TextMobject("Euler's pentagonal-number theorem")
        fml2=TexMobject(r"\prod_{r=1}^\infty(1-q^r)=" \
                r"\sum_{k\in\mathbb Z}(-1)^kq^{\frac12(3k^2+k)}",
                tex_to_color_map={
                    r"\prod_{r=1}^\infty":RED,
                    r"\sum_{k\in":PINK,
                    r"\mathbb Z}":YELLOW,
                    "q":TEAL
                })
        gp=VGroup(tit,fml,tit2,fml2).arrange(DOWN)
        self.add(gp)
        self.wait()

