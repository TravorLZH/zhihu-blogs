from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={"{A}":RED,"Q":TEAL,"^A}":RED}
        tit=TextMobject(r"Analytic Number Theory \#18")
        eqn=TexMobject(r"\pi(x;q,a)=\sum_{\substack{p\le x\\p\equiv a(q)}}1",tex_to_color_map=cm)
        tit2=TextMobject(r"\textbf{Theorem (Bombieri-Vinogradov):}")
        eqn2=TexMobject(r"\forall{A}>0\wedge 1\le Q\le x^{1/2}(\log x)^{-{A}-4},",
                tex_to_color_map=cm)
        eqn3=TexMobject(r"\sum_{q\le Q}\max_{y\le x}\max_{(a,q)=1}\left|\pi(y;q,a)-{\operatorname{li}y\over\varphi(q)}\right|\ll_{A}{x\over(\log x)^A}",
                tex_to_color_map=cm)
        self.add(VGroup(tit,eqn,tit2,eqn2,eqn3).arrange(DOWN))
        self.wait()
