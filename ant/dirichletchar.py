from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#4")
        fml=TexMobject(r"{1\over\varphi(k)}" \
                r"\sum_{r=1}^{\varphi(k)}\overline\chi_r({h})" \
                r"\chi_r(n)=[n\equiv{h}\pmod{k}]",
                tex_to_color_map={
                    r"\sum_{r=1}^{\varphi(k)}":RED,
                    r"\chi":BLUE,
                    r"\pmod{k}":ORANGE,
                    r"{h}":YELLOW
                })
        self.add(VGroup(tit,fml).arrange(DOWN))
        self.wait()
