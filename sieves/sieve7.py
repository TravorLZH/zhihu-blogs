from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={
                r"\sum_n":BLUE,
                r"\sum_{q\le Q}":TEAL,
                r"\mathop{\sum_\chi}\nolimits^*":RED,
                r"T(\chi)":YELLOW,
                r"{\chi}":RED,
                "{q}":TEAL,
                r"{n}":BLUE
        }
        tit=TextMobject(r"Sieves \#7 (Multiplicative Large Sieve)")
        fml=TexMobject(r"T(\chi)=\sum_na_{n}\chi({n})\text{ for }M<{n}\le M+N",
                tex_to_color_map=cm)
        fml2=TexMobject(r"\mathop{\sum_\chi}\nolimits^*\text{ sums over primitive }{\chi}\text{ mod }{q}",tex_to_color_map=cm)
        fml3=TexMobject(r"\Rightarrow\sum_{q\le Q}{{q}\over\varphi({q})}\mathop{\sum_\chi}\nolimits^*|T(\chi)|^2\ll(N+Q^2)\sum_n|a_{n}|^2",tex_to_color_map=cm)
        self.add(VGroup(tit,fml,fml2,fml3).arrange(DOWN))
        self.wait()
