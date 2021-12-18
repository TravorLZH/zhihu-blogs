from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        cm={r"\vartheta":BLUE,"H":RED,"Q":TEAL}
        tit=TextMobject(r"Analytic Number Theory \#17")
        eqn=TexMobject(r"\vartheta(x;q,a)=\sum_{\substack{p\le x\\p\equiv a(q)}}\log p",tex_to_color_map=cm)
        tit2=TextMobject(r"\textbf{Theorem (Barban-Davenport-Halberstam):}")
        eqn2=TexMobject(r"\forall H>0\wedge x(\log x)^{-H}\le Q\le x,",
                tex_to_color_map=cm)
        eqn3=TexMobject(r"\sum_{q\le Q}\sum_{\substack{a\le q\\(a,q)=1}}\left(\vartheta(x;q,a)-{x\over\varphi(q)}\right)^2\ll_HQx\log x",
                tex_to_color_map=cm)
        self.add(VGroup(tit,eqn,tit2,eqn2,eqn3).arrange(DOWN))
        self.wait()
