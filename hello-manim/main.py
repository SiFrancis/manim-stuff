from manim import *

class FirstMessage(Scene):
    def construct(self):
        txt = Text("STATUS: With testicles", font_size=120)
        self.play(Write(txt), run_time=2)
        self.play(txt.animate.to_edge(UP).scale(0.6))
        self.pause()
        grid = Axes(
            x_range = [-5 ,5 ,1],
            y_range = [-1, 5, 1],
            y_length=4,
        ).to_edge(DOWN).add_coordinates()
        
        f = grid.plot(lambda x: (1/5)*x**2, x_range=[-5, 5, 1], color=BLUE)
        
        self.play(Write(grid), run_time=2.5)
        self.play(Write(f))
        self.pause(duration=3)