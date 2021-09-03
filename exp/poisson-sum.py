from manimlib.imports import *

class PoissonScene(Scene):
    def construct(self):
        fml=TexMobject(
            r"\sum_{n\in\mathbb{Z}}{s}(t+{n}T)=\sum_{k\in\mathbb{Z}}" \
            r"{1\over T}\cdot\hat s\left({k}\over T\right)" \
            r"e^{2\pi i{{k}\over T}t}",
            tex_to_color_map={
                r"\hat s":ORANGE,
                r"T":GREEN,
                r"{k}":PINK,
                r"{n}":BLUE,
                r"{s}":YELLOW,
                r"\sum_{n\in\mathbb{Z}}":BLUE,
                r"\sum_{k\in\mathbb{Z}}":PINK
            })
        self.add(VGroup(TextMobject("Poisson summation formula"),fml) \
            .arrange(DOWN).scale(1.5))
        self.wait()
