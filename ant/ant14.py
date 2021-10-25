from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#14")
        tit2=TextMobject(r"\textbf{Theorem (Schnirelman-Goldbach):}",
                tex_to_color_map={
                    "Schnirelman":GREEN,
                    "Goldbach":RED
                })
        tit3=TextMobject("a) A positive proportion of integers")
        tit4=TextMobject("satisfies the Goldbach conjecture.",
                tex_to_color_map={"Goldbach":RED})
        tit5=TextMobject("b) Every integer greater than one is")
        tit6=TextMobject("a sum of a bounded number of primes.",
                tex_to_color_map={"bounded":YELLOW,"primes":BLUE})
        self.add(VGroup(tit,tit2,tit3,tit4,tit5,tit6).arrange(DOWN).scale(0.8))
        self.wait()
