from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject(r"Analytic Number Theory \#13")
        tit2=TextMobject("Schnirelman's Theorem")
        fml0=TexMobject(r"\{0\}\subset A\subseteq\mathbb N_0\text{ and }\inf_{N\ge1}{1\over {N}}|A\cap[1,{N}]|>0",
                tex_to_color_map={
                    "A":RED,
                    r"\inf":GREEN,
                    r"_{N\ge1}":YELLOW,
                    "{N}":YELLOW
                })
        fml=TexMobject(r"\Rightarrow\exists k>0\text{ such that}")
        fml1=TexMobject(r"\{a_1+a_2+\cdots+a_k:a_1,a_2,\dots,a_k\in A\}=\mathbb N_0")
        self.add(VGroup(tit,tit2,fml0,fml,fml1).arrange(DOWN))
        self.wait()
