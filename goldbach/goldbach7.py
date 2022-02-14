from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={r"\Omega":RED,r"\eta":GREEN,r"^\eta":GREEN,
        "{q}":TEAL,"z":YELLOW,r"\sum":PINK}
        tit=TextMobject("Goldbach's Problem \#7")
        eqn=TexMobject(r"{\eta}=\frac12-\varepsilon",tex_to_color_map=cm)
        eqn1=TexMobject(r"d\in\Omega(x,{q},z)\iff(d={q}m,m\le x^\eta/{q},m|P(z))",tex_to_color_map=cm)
        eqn2=TexMobject(r"R_0(x,{q},z)=\sum_{d\in\Omega(x,{q},z)}\max_{y\le x}\max_{(a,d)=1}\left|\pi(x;q,a)-{\operatorname{li}x\over\varphi(qd)}\right|",
                tex_to_color_map=cm)
        eqn3=TexMobject(r"C_y=e^{-\gamma}\prod_{\substack{p|y\\p>2}}{p-1\over p-2}\prod_{p>2}\left(1-{1\over(p-1)^2}\right)",
                tex_to_color_map={r"\gamma":ORANGE,r"\prod":BLUE})
        self.add(VGroup(tit,eqn,eqn1,eqn2,eqn3).arrange(DOWN))
        self.wait()
