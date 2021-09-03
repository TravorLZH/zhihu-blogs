from manimlib.imports import *

class MobiusScene(Scene):
    def construct(self):
        dcv=TexMobject(r"(f*g)(n)=\sum_{d|n}f({d})g\left(n\over {d}\right)",
                tex_to_color_map={
                    "*":RED,r"\sum_{d|n}":BLUE,r"{d}":YELLOW
                })
        mi=TexMobject(r"{g}(n)=\sum_{d|n}{f}(d)," \
                r"{f}(n)=\sum_{d|n}\mu({d}){g}\left(n\over {d}\right)",
                tex_to_color_map={
                    r"\sum_{d|n}":PURPLE,
                    "{d}":YELLOW,
                    r"{f}":RED,
                    r"{g}":BLUE
                })
        gp=VGroup(dcv,mi).arrange(DOWN).scale(1.5)
        self.add(gp)
        self.wait()
