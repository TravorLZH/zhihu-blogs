from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Sieves \#4")
        fml=TexMobject(r"\left(\sum_{d|n}\lambda_d\right)^2\ge\begin{cases}1 & n=1\\ 0 & n>1\end{cases}").scale(0.8)
        fmls=TexMobject(r"S(\mathcal A,\mathcal P,z)\le{|\mathcal A|\over G(z)}+\sum_{k\le z^2}3^{\omega(k)}|{r}(k)|",
                tex_to_color_map={
                    r"\mathcal A":RED,
                    r"\mathcal P":BLUE,
                    "z":YELLOW,
                    r"G":GREEN,
                    r"\sum":ORANGE,
                    r"{r}":RED})
        fml1=TexMobject(r"\#\{x<p\le x+y:p+2\text{ prime}\}\ll{y\over(\log y)^2}",
                tex_to_color_map={
                    r"\log":GREEN
                })
        gp=VGroup(fml,fmls,fml1).arrange(DOWN).scale(0.7)
        self.add(VGroup(tit,gp).arrange(DOWN))
        self.wait()
