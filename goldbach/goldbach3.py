from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#3")
        mp={
                "{c}":ORANGE,
                r"\Lambda":TEAL,
                r"\lambda":RED,
                r"{\alpha}":YELLOW,
                r"{\beta}":PINK,
                r"\int":BLUE,r"\mathrm du":BLUE,"{u}":BLUE,
                # Somehow we need to reverse it to make them look right
                r"_{\alpha":PINK,
                r"^{\beta":YELLOW
        }
        eqn=TexMobject(r"P_w(x,x^{1/{\alpha}})\le\Lambda({\alpha}){{c}x\over\log^2x}+\mathcal O\left({c}x\over\log^3x\right)",tex_to_color_map=mp)
        eqn1=TexMobject(r"P_w(x,x^{1/{\alpha}})\ge\lambda({\alpha}){{c}x\over\log^2x}+\mathcal O\left({c}x\over\log^3x\right)",tex_to_color_map=mp)
        eqn2=TexMobject(r"\lambda({\alpha})=\lambda({\beta})-2\int_{\alpha-1}^{\beta-1}\Lambda({u}){{u}+1\over{u}^2}\mathrm du",tex_to_color_map=mp)
        self.add(VGroup(tit,eqn,eqn1,eqn2).arrange(DOWN))
        self.wait()
