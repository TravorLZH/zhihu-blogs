from manimlib.imports import *

def func(x):
    return 1/x

class DigammaScene(GraphScene):
    CONFIG={
        "x_min":0,
        "x_max":5,
        "y_min":0,
        "y_max":5,
        "x_tick_frequency":1,
        "y_tick_frequency":1,
        "graph_origin":(-5,-3,0)
    }
    def construct(self):
        self.setup_axes(animate=False)
        gf=self.get_graph(func,x_min=0.05,color=RED)
        rect=self.get_riemann_rectangles(gf,x_min=1,x_max=5,dx=1)
        self.add(gf,rect)
        self.bring_to_front(gf)
        fml=TexMobject(r"\gamma","=",r"\lim_{n\to\infty}",r"\left[",
            r"\sum_{k=1}^n",r"{1\over k}","-",r"\ln","(n)",r"\right]")
        fml[0].set_color(ORANGE)
        fml[2].set_color(PINK)
        fml[4].set_color(BLUE)
        fml[7].set_color(GREEN)
        fml.scale(1.5)
        fml.move_to((2,1,0))
        self.add(fml)
        self.wait()
