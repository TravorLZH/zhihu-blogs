from manimlib.imports import *

class FooScene(Scene):
    def construct(self):
        title=TextMobject(r"\scshape 2021 AIME II Problem 13",
                tex_to_color_map={"AIME":GREEN}).scale(1.5)
        nothing=TextMobject("k")
        problm=TextMobject(r"Find the least positive integer $n$\\for which $2^n+5^n-n$ is a multiple of 1000",
                tex_to_color_map={"least":YELLOW,"integer":BLUE,"multiple":RED})
        VGroup(title,nothing,problm).arrange(DOWN)
        self.add(title,problm)
        self.wait()
