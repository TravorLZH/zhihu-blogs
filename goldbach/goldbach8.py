from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={r"\Omega":RED,r"\eta":GREEN,r"^\eta":GREEN,
        "{q}":TEAL,"z":YELLOW,r"\sum":PINK}
        mp={
                r"\Lambda":TEAL,
                r"\lambda":RED,
                r"\int_{\alpha-1}^{\beta-1}":BLUE,r"\mathrm du":BLUE
        }
        tit=TextMobject("Goldbach's Problem \#8")
        eqn=TexMobject(r"\lambda({\alpha})=\lambda({\beta})-\int_{\alpha-1}^{\beta-1}{\Lambda(u)\over u}\mathrm du",
                tex_to_color_map=mp)
        eqn2=TexMobject(r"\Lambda(\alpha)={2\alpha e^\gamma\over\alpha-1-\frac\alpha2\log\frac\alpha2+\delta(\alpha)}",
                tex_to_color_map={r"\Lambda":TEAL})
        eqn3=TexMobject(r"\delta(\alpha)=\int_1^{\frac\alpha4}\int_s^{\frac\alpha2-s}{\frac\alpha2-s-t\over st}\mathrm dt\mathrm ds",
                tex_to_color_map={
                    r"\int_1^{\frac\alpha4}":PINK,
                    r"\mathrm ds":PINK,
                    r"\int_s^{\frac\alpha2-s}":YELLOW,
                    r"\mathrm dt":YELLOW
                })
        self.add(VGroup(tit,eqn,eqn2,eqn3).arrange(DOWN))
        self.wait()
