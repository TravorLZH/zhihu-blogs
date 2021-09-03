from manimlib.imports import *

class BMTScene(Scene):
    def construct(self):
        tit=TextMobject("2020 ","BMT"," Algebra round ",r"\#10")
        tit[0].set_color(RED)
        tit[1].set_color_by_gradient(RED,YELLOW)
        tit[2].set_color_by_gradient(GREEN,BLUE)
        tit[3].set_color(BLUE)
        fml=TexMobject(r"\sum_{k=1}^\infty" \
                r"\cos^{-1}\left(2^{2k+1}-3\cdot2^{k+1}+5" \
                r"\over\sqrt{(2^{2k}-2^{k+2}+5)(2^{2k+2}-2^{k+3}+5)}\right)" \
                r"={\pi\over2}",
                tex_to_color_map={
                    r"\sum_{k=1}^\infty":PINK,
                    r"\cos^{-1}":GREEN,
                    r"\pi":BLUE,
                })
        gp=VGroup(tit,fml).arrange(DOWN)
        self.add(gp)
        self.wait()
