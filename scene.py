from math import *
from manim import *

#manim -pqk scene.py 
#manim -pqk --format=png scene.py 

# Colors
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#C02020'
GREEN = '#70FF70'
BLUE = '#8080FF'
PURE_RED = '#FF0000'
PURE_GREEN = '#00FF00'
PURE_BLUE = '#0000FF'

class Part2Turn1(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-1000, 1000, 100), y_range=(-100, 1000, 100),
            x_length=24, y_length=13.6
        ).add_coordinates([-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000],[100,200,300,400,500,600,700,800,900,1000]).set_opacity(0.25).scale(0.5).shift(0.25*DOWN)
        self.add(axes)
        axes_labels = VGroup(
            MathTex(r"x").set_opacity(0.25).move_to(axes.c2p(1100,0)),
            MathTex(r"y").set_opacity(0.25).move_to(axes.c2p(0,1050))
        )
        self.add(axes_labels)


        t = Variable(var=0, label=MathTex(r"t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(t)
        
        r = always_redraw(lambda :
            ArrowTriangleFilledTip(color=RED).move_to(axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value()))).rotate(0.4759*t.value.get_value()-0.5*PI).set_z_index(3)
        )
        trace = TracedPath(lambda : axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())), stroke_color=RED, stroke_width=6, stroke_opacity=1, z_index=6)
        self.add(r, trace)

        v = always_redraw(lambda : Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(2))
        self.add(v)

        a = always_redraw(lambda : Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(1))
        self.add(a)

        key = VGroup(
            Text("KEY", color=WHITE).to_edge(RIGHT),
            MathTex(r"\vec{r}_1(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
            MathTex(r"\vec{v}_1(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
            MathTex(r"\vec{a}_1(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
        ).to_corner(UR)
        self.add(key)

        self.play(t.tracker.animate.set_value(4.66), rate_func=linear, run_time=4.66)
        self.wait(0.05)

class Part2Turn2(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-1000, 1000, 100), y_range=(-100, 1000, 100),
            x_length=24, y_length=13.6
        ).add_coordinates([-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000],[100,200,300,400,500,600,700,800,900,1000]).set_opacity(0.25).scale(0.5).shift(0.25*DOWN)
        self.add(axes)
        axes_labels = VGroup(
            MathTex(r"x").set_opacity(0.25).move_to(axes.c2p(1100,0)),
            MathTex(r"y").set_opacity(0.25).move_to(axes.c2p(0,1050))
        )
        self.add(axes_labels)


        t = Variable(var=0, label=MathTex(r"t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(t)
        
        r = always_redraw(lambda : 
            ArrowTriangleFilledTip(color=RED).move_to(axes.c2p(522.47*cos(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value()))).rotate(0.4211*t.value.get_value()-0.5*PI).set_z_index(3)
        )
        trace = TracedPath(lambda : axes.c2p(522.47*cos(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value())), stroke_color=RED, stroke_width=6, stroke_opacity=1, z_index=6)
        self.add(r, trace)

        v = always_redraw(lambda : Arrow(
            start=axes.c2p(522.47*cos(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value())),
            end=axes.c2p(522.47*cos(0.4211*t.value.get_value())-220.0121*sin(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value())+220.0121*cos(0.4211*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(2))
        self.add(v)

        a = always_redraw(lambda : Arrow(
            start=axes.c2p(522.47*cos(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value())),
            end=axes.c2p(522.47*cos(0.4211*t.value.get_value())-92.6471*cos(0.4211*t.value.get_value()) , 522.47*sin(0.4211*t.value.get_value())-92.6471*sin(0.4211*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(1))
        self.add(a)

        key = VGroup(
            Text("KEY", color=WHITE).to_edge(RIGHT),
            MathTex(r"\vec{r}_2(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
            MathTex(r"\vec{v}_2(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
            MathTex(r"\vec{a}_2(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
        ).to_corner(UR)
        self.add(key)

        self.play(t.tracker.animate.set_value(4.44), rate_func=linear, run_time=4.44)
        self.wait(0.05)

class Part2Turn3(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-1000, 1000, 100), y_range=(-100, 1000, 100),
            x_length=24, y_length=13.6
        ).add_coordinates([-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000],[100,200,300,400,500,600,700,800,900,1000]).set_opacity(0.25).scale(0.5).shift(0.25*DOWN)
        self.add(axes)
        axes_labels = VGroup(
            MathTex(r"x").set_opacity(0.25).move_to(axes.c2p(1100,0)),
            MathTex(r"y").set_opacity(0.25).move_to(axes.c2p(0,1050))
        )
        self.add(axes_labels)


        t = Variable(var=0, label=MathTex(r"t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(t)
        
        r = always_redraw(lambda : 
            ArrowTriangleFilledTip(color=RED).move_to(axes.c2p(733.89*cos(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value()))).rotate(0.3797*t.value.get_value()-0.5*PI).set_z_index(3)
        )
        trace = TracedPath(lambda : axes.c2p(733.89*cos(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value())), stroke_color=RED, stroke_width=6, stroke_opacity=1, z_index=6)
        self.add(r, trace)

        v = always_redraw(lambda : Arrow(
            start=axes.c2p(733.89*cos(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value())),
            end=axes.c2p(733.89*cos(0.3797*t.value.get_value())-278.6580*sin(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value())+278.6580*cos(0.3797*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(2))
        self.add(v)

        a = always_redraw(lambda : Arrow(
            start=axes.c2p(733.89*cos(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value())),
            end=axes.c2p(733.89*cos(0.3797*t.value.get_value())-105.8065*cos(0.3797*t.value.get_value()) , 733.89*sin(0.3797*t.value.get_value())-105.8065*sin(0.3797*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(1))
        self.add(a)

        key = VGroup(
            Text("KEY", color=WHITE).to_edge(RIGHT),
            MathTex(r"\vec{r}_3(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
            MathTex(r"\vec{v}_3(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
            MathTex(r"\vec{a}_3(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
        ).to_corner(UR)
        self.add(key)

        self.play(t.tracker.animate.set_value(1.50), rate_func=linear, run_time=1.50)
        self.wait(0.05)

class Part2Sec3(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-1000, 1000, 100), y_range=(-100, 1000, 100),
            x_length=24, y_length=13.6
        ).add_coordinates([-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000],[100,200,300,400,500,600,700,800,900,1000]).set_opacity(0.25).scale(0.5).shift(0.25*DOWN)
        self.add(axes)
        axes_labels = VGroup(
            MathTex(r"x").set_opacity(0.25).move_to(axes.c2p(1100,0)),
            MathTex(r"y").set_opacity(0.25).move_to(axes.c2p(0,1050))
        )
        self.add(axes_labels)


        t = Variable(var=0, label=MathTex(r"t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(t)
        
        r = always_redraw(lambda : 
            ArrowTriangleFilledTip(color=RED).move_to(axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value()))).rotate(0.4759*t.value.get_value()-0.5*PI).set_z_index(6)
        )
        trace = TracedPath(lambda : axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())), stroke_color=RED, stroke_width=6, stroke_opacity=1, z_index=6)
        self.add(r, trace)

        v = always_redraw(lambda : Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(5))
        self.add(v)

        a = always_redraw(lambda : Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(4))
        self.add(a)

        key = VGroup(
            Text("KEY", color=WHITE).to_edge(RIGHT),
            MathTex(r"\vec{r}_1(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
            MathTex(r"\vec{v}_1(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
            MathTex(r"\vec{a}_1(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
        ).to_corner(UR)
        self.add(key)

        v0 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v0)

        a0 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a0)

        self.play(t.tracker.animate.set_value(1.00), rate_func=linear, run_time=1)
        v1 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v1)

        a1 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a1)
        
        self.play(t.tracker.animate.set_value(2.00), rate_func=linear, run_time=1)
        v2 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v2)

        a2 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a2)

        self.play(t.tracker.animate.set_value(3.00), rate_func=linear, run_time=1)
        v3 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v3)

        a3 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a3)

        self.play(t.tracker.animate.set_value(4.00), rate_func=linear, run_time=1)
        v4 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v4)

        a4 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a4)

        self.play(t.tracker.animate.set_value(4.66), rate_func=linear, run_time=0.66)
        v5 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-212.6559*sin(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())+212.6559*cos(0.4759*t.value.get_value())),
            color=GREEN,
            buff=0
        ).set_z_index(3)
        self.add(v5)

        a5 = Arrow(
            start=axes.c2p(446.85*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())),
            end=axes.c2p(446.85*cos(0.4759*t.value.get_value())-101.2029*cos(0.4759*t.value.get_value()) , 446.85*sin(0.4759*t.value.get_value())-101.2029*sin(0.4759*t.value.get_value())),
            color=BLUE,
            buff=0
        ).set_z_index(2)
        self.add(a5)

        self.wait(0.05)

class Part3Sec0(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        l1 = Line([-5,-3,0],[5,-3,0], color=GREEN, z_index=2)
        l2 = Line([-5,-3,0],[5,2,0], color=GREEN, z_index=2)
        angle = Angle(l1,l2,radius=1.5)
        angleLabel = MathTex(r"\theta").next_to(angle, RIGHT)
        car = RoundedRectangle(color=RED, fill_color=RED, fill_opacity=0.5, z_index=1).rotate(np.arctan2(5,10)).move_to([0,0.65,0])
        mass = MathTex(r"m").set_z_index(4).scale(2).rotate(np.arctan2(5,10)).move_to([0,0.65,0])
        hBrace = BraceBetweenPoints([5.25,-3,0], [5.25,0.65,0], direction=RIGHT)
        hLabel = MathTex(r"h").move_to([6,-1,0])
        dash = DashedLine([0.75,0.65,0], [5.25,0.65,0], dash_length=0.5, dashed_ratio=0.6).set_z_index(2)
        diagramLabel = MathTex(r"\text{Front View}").move_to([0,-3.5,0])
        self.add(
            l1,
            l2,
            angle,
            angleLabel,
            car,
            mass,
            hBrace,
            hLabel,
            dash,
            diagramLabel
        )

        circle = Circle(radius=1, color=GREEN).move_to([-5.5,2.5,0])
        car2 = RoundedRectangle(height=0.3, width=0.2, corner_radius=0.02, color=RED, fill_color=RED, fill_opacity=0.5, z_index=2).move_to([-4.5,2.5,0])
        diagramLabel2 = MathTex(r"\text{Top View}").move_to([-5.5,1,0])
        rBrace = BraceBetweenPoints([-4.5,2.5,0], [-4.5,3.5,0], direction=RIGHT)
        rLabel = MathTex(r"R").move_to([-3.75,3,0])
        arrow = ArcBetweenPoints([-4.5,2.5,0],[-5.5,3.5,0], radius=1, stroke_width=5)
        tip = ArrowTriangleFilledTip(color=WHITE).move_to([-5.5,3.5,0])
        w = MathTex(r"\omega").move_to([-5.5,3.15,0])
        self.add(
            circle,
            car2,
            diagramLabel2,
            rLabel,
            rBrace,
            arrow,
            tip,
            w
        )

class Part3Sec1(Scene):
    def construct(self):
        self.camera.background_color = '#101020'

        R=2
        w=0.75
        wt = Variable(var=0, label=MathTex(r"\omega t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(wt)
        self.add(Dot(z_index=5))
        self.add(DashedVMobject( Circle(radius=R, color=WHITE, z_index=1).set_opacity(0.25) ))

        r = always_redraw(lambda : Arrow(
            ORIGIN,
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            color=RED,
            buff=0
        ).set_z_index(4))
        v = always_redraw(lambda : Arrow(
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0])+np.array([-w*R*sin(wt.value.get_value()),w*R*cos(wt.value.get_value()),0]),
            color=GREEN,
            buff=0
        ).set_z_index(3))
        a = always_redraw(lambda : Arrow(
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0])+np.array([-w*w*R*cos(wt.value.get_value()),-w*w*R*sin(wt.value.get_value()),0]),
            color=BLUE,
            buff=0
        ).set_z_index(2))
        self.add(r,v)

        key = VGroup(
                Text("KEY", color=WHITE).to_edge(RIGHT),
                MathTex(r"\vec{r}(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
                MathTex(r"\vec{v}(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
                #MathTex(r"\vec{a}(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
            ).to_corner(UR)
        self.add(key)

        self.play(wt.tracker.animate.set_value(6.28), rate_func=linear, run_time=6.28)

class Part3Sec3(Scene):
    def construct(self):
        self.camera.background_color = '#101020'

        R=2
        w=0.75
        wt = Variable(var=0, label=MathTex(r"\omega t"), num_decimal_places=2).scale(1.5).to_corner(UL)
        self.add(wt)
        self.add(Dot(z_index=5))
        self.add(DashedVMobject( Circle(radius=R, color=WHITE, z_index=1).set_opacity(0.25) ))

        r = always_redraw(lambda : Arrow(
            ORIGIN,
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            color=RED,
            buff=0
        ).set_z_index(4))
        v = always_redraw(lambda : Arrow(
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0])+np.array([-w*R*sin(wt.value.get_value()),w*R*cos(wt.value.get_value()),0]),
            color=GREEN,
            buff=0
        ).set_z_index(3))
        a = always_redraw(lambda : Arrow(
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0]),
            np.array([R*cos(wt.value.get_value()),R*sin(wt.value.get_value()),0])+np.array([-w*w*R*cos(wt.value.get_value()),-w*w*R*sin(wt.value.get_value()),0]),
            color=BLUE,
            buff=0,
            stroke_width=10,
            max_stroke_width_to_length_ratio=10
        ).set_z_index(2))
        self.add(r,v,a)

        key = VGroup(
                Text("KEY", color=WHITE).to_edge(RIGHT),
                MathTex(r"\vec{r}(t)", color=RED).to_edge(RIGHT).shift(0.75*DOWN),
                MathTex(r"\vec{v}(t)", color=GREEN).to_edge(RIGHT).shift(1.5*DOWN),
                MathTex(r"\vec{a}(t)", color=BLUE).to_edge(RIGHT).shift(2.25*DOWN)
            ).to_corner(UR)
        self.add(key)

        self.play(wt.tracker.animate.set_value(6.28), rate_func=linear, run_time=6.28)

class Part3Sec5(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        l1 = Line([-5,-3,0],[5,-3,0], color=GREEN, z_index=2)
        l2 = Line([-5,-3,0],[5,2,0], color=GREEN, z_index=2)
        angle = Angle(l1,l2,radius=1.5)
        angleLabel = MathTex(r"\theta").next_to(angle, RIGHT)
        car = RoundedRectangle(color=RED, fill_color=RED, fill_opacity=0.5, z_index=1).rotate(np.arctan2(5,10)).move_to([0,0.65,0])
        mass = MathTex(r"m").set_z_index(4).scale(2).rotate(np.arctan2(5,10)).move_to([0,0.65,0])
        gravityArrow = Arrow([0,0.2,0],[0,-2.25,0],buff=0,color=BLUE).set_z_index(2)
        gravity = MathTex(r"mg", color=BLUE).move_to([0,-2.7,0])
        normalArrow = Arrow([0,1.2,0],[-1,3.2,0],buff=0,color=BLUE).set_z_index(2)
        normal = MathTex(r"\vec{N}", color=BLUE).move_to([-1.3,3.5,0])
        frictionArrow = Arrow([-0.75,0.5,0],[-2.75,-0.5,0],buff=0,color=BLUE).set_z_index(2)
        friction = MathTex(r"\vec{f}", color=BLUE).move_to([-3.25,-0.75,0])
        self.add(
            l1,
            l2,
            angle,
            angleLabel,
            car,
            mass,
            gravityArrow,
            gravity,
            normalArrow,
            normal,
            frictionArrow,
            friction
        )

class Part3Sec5II(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-4,4,1), y_range=(-2,2,1),
            x_length=16, y_length=8
        ).set_opacity(0.25)
        self.add(axes)

        self.add(Dot(color=RED, z_index=5, radius=0.1))
        g = Arrow(ORIGIN, [0,-2,0], buff=0, color=BLUE)
        f = Arrow(ORIGIN, [-2,-1,0], buff=0, color=BLUE)
        N = Arrow(ORIGIN, [-1,2,0], buff=0, color=BLUE)
        g.target = Arrow(ORIGIN, [0,-2,0], buff=0, color=GREEN)
        f.target = Arrow(ORIGIN, [0,-1,0], buff=0, color=GREEN)
        N.target =Arrow(ORIGIN, [0,2,0], buff=0, color=GREEN)

        self.add(g,f,N)
        self.play(MoveToTarget(g), MoveToTarget(f), MoveToTarget(N), run_time=2)

class Part3Sec6(Scene):
    def construct(self):
        self.camera.background_color = '#101020'
        axes = NumberPlane(
            x_range=(-4,4,1), y_range=(-2,2,1),
            x_length=16, y_length=8
        ).set_opacity(0.25)
        self.add(axes)

        self.add(Dot(color=RED, z_index=5, radius=0.1))
        g = Arrow(ORIGIN, [0,-2,0], buff=0, color=BLUE)
        f = Arrow(ORIGIN, [-2,-1,0], buff=0, color=BLUE)
        N = Arrow(ORIGIN, [-1,2,0], buff=0, color=BLUE)
        g.target = Arrow(ORIGIN, [0,0,0], buff=0, color=GREEN)
        f.target = Arrow(ORIGIN, [-2,0,0], buff=0, color=GREEN)
        N.target =Arrow(ORIGIN, [-1,0,0], buff=0, color=GREEN)

        self.add(g,f,N)
        self.play(MoveToTarget(g), MoveToTarget(f), MoveToTarget(N), run_time=2)


