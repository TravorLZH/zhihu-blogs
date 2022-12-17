from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cmap=tex_to_color_map={
                r"\liminf":ORANGE,
                "p":BLUE
        }
        tit=TextMobject("Bounded Gaps between Primes \#7")
        tx=TextMobject(r"\textbf{Theorem (Maynard, 2015):}")
        eqn=TexMobject(
                r"\liminf_{n\to\infty}(p_{n+m}-p_n)\ll m^3e^{4m}",
                tex_to_color_map=cmap)
        eqn2=TexMobject(
                r"\liminf_{n\to\infty}(p_{n+1}-p_n)\le600",
                tex_to_color_map=cmap)
        self.add(VGroup(tit,tx,eqn,eqn2).arrange(DOWN))
        self.wait()
