from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#6 (Arithmetic Large Sieve)")
        fml=TexMobject(r"S(\mathcal A,\mathcal P,z)\times\sum_{q\le z}\mu^2(q)\prod_{p|q}{b(p)\over p-b(p)}\le N+3z^2",
                tex_to_color_map={
                    "L":BLUE,r"\mathcal A":PINK,"z":YELLOW,
                    r"\mu":GREEN,r"\prod":ORANGE,
                    r"\sum":RED,"q":TEAL,r"\mathcal P":BLUE
                })
        fml2=TexMobject(r"\pi_2(x+y)-\pi_2(x)\le{(16+\varepsilon)y\over(\log y)^2}\prod_{p>2}\left(1-{1\over(p-1)^2}\right)",
                tex_to_color_map={
                    "y":YELLOW,r"\prod":ORANGE,
                    r"\pi_2":GREEN,r"\varepsilon":PINK
                })
        self.add(VGroup(tit,fml,fml2).arrange(DOWN))
        self.wait()
