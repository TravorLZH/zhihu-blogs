from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        tit=TextMobject("Goldbach's Problem \#6")
        eqn=TexMobject(r"{M}(x,y,z,m)\ge{M}(x,y,z)-{1\over m+1}\sum_{y<p_j\le z}|\mathcal M_j|",
                tex_to_color_map={"{M}":PINK,r"\mathcal M":PINK})
        eqn2=TexMobject(r"\phi(v,u,m)=\lambda(v)-{2\over m+1}\int_{u-1}^{v-1}\Lambda\left(vz\over z+1\right){z+1\over z^2}\mathrm dz",
                tex_to_color_map={r"\lambda":RED,r"\Lambda":TEAL,r"\int_{u-1}^{v-1}":ORANGE,r"\mathrm dz":ORANGE})
        self.add(VGroup(tit,eqn,eqn2).arrange(DOWN))
        self.wait()
