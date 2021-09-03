from manimlib.imports import *

class RSumEulerScene(Scene):
    def construct(self):
        fml=TexMobject(r"\varphi({n})=\sum_{m=1}^n\gcd({m},{n})" \
                r"\cos\left({2\pi {m}\over {n}}\right)",
                tex_to_color_map={
                    r"\varphi":ORANGE,
                    r"\sum_{m=1}^n":PINK,
                    r"{m}":PINK,
                    r"{n}":YELLOW,
                    r"\gcd":BLUE
                })
        fml2=TexMobject(r"\sum_{n=1}^\infty{\varphi({n})\over{n}^s}" \
                r"={\zeta(s-1)\over\zeta(s)}",
                tex_to_color_map={
                    r"\varphi":ORANGE,
                    r"\sum_{n=1}^\infty":YELLOW,
                    r"{n}":YELLOW,
                    r"{\zeta":GREEN,
                    r"\zeta":GREEN
                })
        gp=VGroup(fml,fml2).arrange(DOWN).scale(1.5)
        self.add(gp)
        self.wait()
