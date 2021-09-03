from manimlib.imports import *

class FourierScene(Scene):
    def construct(self):
        sers=TexMobject(
            r"f(x)=\sum_{n\in\mathbb{Z}} c_n{e}^{2\pi inx\over T}",
            tex_to_color_map={
                r"x":YELLOW,
                r"\sum_{n\in\mathbb{Z}}":BLUE,
                r"{e}":RED,
                r"c_n":GREEN
            })
        trsfm=TexMobject(
            r"\mathcal{F}\{x(t)\}(k)=\int_{t\in\mathbb{R}}" \
            r"x(t){e}^{-2\pi ikt}dt",
            tex_to_color_map={
                r"\mathcal{F}":GREEN,
                r"\int_{t\in\mathbb{R}}":PINK,
                r"dt":PINK,
                r"k":YELLOW,
                r"{e}":RED
            })
        self.add(VGroup(sers,trsfm).arrange(DOWN).scale(1.5))
        self.wait()
