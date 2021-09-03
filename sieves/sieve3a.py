from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#3.1")
        fml=TexMobject(r"\sum_{\substack{d|n\\\omega(d)\le\ell}}\mu(d)=(-1)^\ell\binom{\omega(n)-1}{\ell}",
                tex_to_color_map={r"\mu":YELLOW,"d":RED})
        fml1=TexMobject(r"\#\{x<p\le x+y:p+2\text{ prime}\}\ll{y(\log\log y)^2\over(\log y)^2}",
                tex_to_color_map={
                    r"\log":GREEN
                })
        self.add(VGroup(tit,fml,fml1).arrange(DOWN))
        self.wait()
