from manim import*
import numpy as np


class ReusableEllipse(Ellipse):
    """Reusable ellipse highlight with configurable styles"""
    def __init__(self, mobject, color=BLUE, fill_opacity=0.3, 
                 stroke_width=2, **kwargs):
        super().__init__(
            width=mobject.width + 0.2,
            height=mobject.height + 0.2,
            color=color,
            fill_opacity=fill_opacity,
            **kwargs
        )
        self.move_to(mobject)
        self.set_stroke(color=color, width=stroke_width)
        
    def highlight_at_position(self, position):
        """Position a copy at new location"""
        copy = self.copy()
        copy.move_to(position)
        return copy
    

class ReusableRectangles(SurroundingRectangle):
    """Reusable rectangle with configurable styles"""
    def __init__(self, mobject, color=RED, buff=0.1, 
                 fill_opacity=0.3, stroke_width=2, **kwargs):
        super().__init__(mobject, color=color, buff=buff, 
                         fill_opacity=fill_opacity, **kwargs)
        self.set_stroke(color=color, width=stroke_width)
        self.original_color = color
        
    def create_prime_version(self):
        """Create derivative version with prime symbol"""
        prime = MathTex("'", color=self.color).scale(1.5)
        prime.move_to(self.get_corner(UR) + UP * 0.2 + RIGHT * 0.2)
        Group1_PrimeRect=VGroup(self.copy(), prime)
        return Group1_PrimeRect
        
    def highlight_at_position(self, position, color=None):
        """Position a copy at new location"""
        copy = self.copy()
        if color:
            copy.set_color(color)
            copy.set_stroke(color=color)
        copy.move_to(position)
        return copy


class Rational2(Scene,ReusableRectangles,ReusableEllipse):
    def construct(self):
# Create texts objects
        text1 = Text("Proper Rational Function", gradient=[TEAL_A,TEAL_E],sheen_factor=-0.75).scale(0.75).shift([0,3,0])
        integral1 = MathTex(
                r"\int",       # 0: integral symbol
                r"{",          # 1: opening brace
                r"1",          # 2: numerator
                r"\over",      # 3: fraction line
                r"(x+1)",     # 4: base expression as single mobject
                r"^2",         # 5: exponent as single mobject (^2 together)
                r"}",          # 6: closing brace
                r"\,",         # 7: small space
                r"dx",         # 8: differential
            color=TEAL_A,
            sheen_factor=-0.25).next_to(text1[0], DOWN, buff=0.8).scale(1.15)
        self.play(Write(text1,run_time=1),Write(integral1,run_time=0.75))

#Boxing:
        indices_denominator1=[4,5]
        denominator1 = VGroup(*[integral1[i] for i in indices_denominator1])
        """
                        Explanation:Let’s say:
                        integral1 = [mobj0, mobj1, mobj2, mobj3, mobj4, mobj5, mobj6, mobj7]
                        Then this part:
                        [integral1[i] for i in indices_denominator1]
                        Means:
                        [integral1[4], integral1[5], integral1[6]]
                        → [mobj4, mobj5, mobj6]
                        That list [mobj4, mobj5, mobj6] gets unpacked with * like this:
                        VGroup(mobj4, mobj5, mobj6)
        """

                                # ====== USING REUSABLE RECTANGLES ======
        box1=ReusableRectangles(mobject=denominator1)
        self.play(Create(box1))
        self.wait(1.5)

                                # ====== COPY AND MOVE THE BOX ======
        # Create a copy of the box and move it to the side
        box1_copy=box1.highlight_at_position(box1.get_center())
        self.play(box1_copy.animate.shift([3.5,0,0]))
        self.wait(0.75)

        isEqualTo=Text("=",color=RED).next_to(box1_copy,RIGHT)
        self.play(Write(isEqualTo))
        self.wait(0.075)
# copy of denominator 
        denominator1_copy=denominator1.copy()
        self.play(denominator1_copy.animate.next_to(isEqualTo,RIGHT))
        self.wait(0.075)
                # ====== CREATE PRIME VERSION (DERIVATIVE) ======
        rect_Prime=box1_copy.create_prime_version()
        rect_Prime.set_color(BLUE_C)
        rect_Prime.next_to(box1_copy,DOWN)
        self.play(DrawBorderThenFill(rect_Prime)) # Displaying the rectangle and prime symbol
           # ====== SHOW DERIVATIVE EXPRESSION ======
        isEqualTo2 =isEqualTo.copy().set_color(BLUE_C)
        isEqualTo2.next_to(rect_Prime, RIGHT)
        self.play(Write(isEqualTo2))

        
        exp1 = MathTex(
    "2",        # 0: coefficient
    "(",        # 1: opening parenthesis
    "x",        # 2: x
    "+",        # 3: plus
    "1",        # 4: first constant
    ")",        # 5: closing parenthesis
    "(",        # 6: second opening parenthesis
    "1",        # 7: second constant
    ")"         # 8: second closing parenthesis
)

        exp1.next_to(isEqualTo2,RIGHT)
        self.play(Write(exp1),run_time=1.5)
        self.wait() 
        
# making a cross 
        cross1=Cross(mobject=exp1,color=PURE_RED,stroke_width=3.5)
        self.play(Create(cross1),run_time=1.5)



#==============================#==============================#==============================#==============================


                  #=======| DOING CORRECT WAY |=======
# ++++++++++++ Removing stuff ++++++++++++
        group1_removal=VGroup(box1,box1_copy,rect_Prime,isEqualTo,isEqualTo2,denominator1_copy,exp1,cross1)
        self.play(FadeOut(group1_removal))
# ++++++++++++| Boxing denominator |++++++++++++
        #compreshension list 
        indices_denominator2=[4]
        denominator2=VGroup(*[integral1[i] for i in indices_denominator2])
        #Red box
        box2=ReusableRectangles(denominator2)
        self.play(DrawBorderThenFill(box2))
        self.wait()
        #Red box copy
        box2_copy=box2.highlight_at_position(box2.get_center())
        self.play(box2_copy.animate.shift([4,0,0]))
        self.wait()
        #is equalto1
        isEqualTo.next_to(box2_copy,RIGHT)
        self.play(Write(isEqualTo))
        self.wait()
        #repeating denominator2
        denominator2_copy=denominator2.copy()
        self.play(denominator2_copy.animate.next_to(isEqualTo,RIGHT))
        
        #Rectprime2
        rect_Prime2=box2_copy.create_prime_version()
        rect_Prime2.set_color(BLUE_C).next_to(box2_copy,DOWN)
        self.play(DrawBorderThenFill(rect_Prime2))
        self.wait()
        #isequalto2 copy 
        isEqualTo2.next_to(rect_Prime2,RIGHT)
        self.play(Write(isEqualTo2))
        self.wait()
        #derivative 
        exp2=MathTex(r"1")
        exp2.next_to(isEqualTo2,RIGHT)
        self.play(Write(exp2))
        #ellipsing 
        ellipso1=ReusableEllipse(mobject=exp2)
        self.play(DrawBorderThenFill(ellipso1))
        self.wait()
        ellipso1_copy=ReusableEllipse(mobject=integral1[2])
        self.play(DrawBorderThenFill(ellipso1_copy))
        self.wait()
        #animating integration
        dot1_ellipso1=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso1.next_to(ellipso1_copy,UP,buff=0)
        self.play(Write(dot1_ellipso1))
        self.wait()
        background_colour1=BackgroundRectangle(integral1[2],color=PURPLE_A)
        background_colour2=BackgroundRectangle(integral1[0],color=PURPLE_A)
        background_colour3=BackgroundRectangle(integral1[8],color=PURPLE_A)
        self.play(Create(background_colour1,run_time=0.5),
                  Create(background_colour2,run_time=1.5),
                  Create(background_colour3),run_time=2.5)
        self.wait()
        arc1=ArcBetweenPoints(start=integral1[0].get_top(),
                              end=dot1_ellipso1.get_center(), 
                              angle=-PI/2 )
        arc2=ArcBetweenPoints(start=dot1_ellipso1.get_center(),
                              end=integral1[8].get_top(),
                              angle=-PI/2 )
        self.play(Write(arc1),
                  Write(arc2))
        self.wait()
        #Integral removal using list comprehension 
        indices_removal1=[0,1,3,6,7,8,2]
        removal1_integral1=VGroup(*[integral1[i] for i in indices_removal1])
        group5_removing1=VGroup(ellipso1_copy,
                                dot1_ellipso1,
                                arc1,
                                arc2,
                                removal1_integral1,
                                background_colour1,
                                background_colour2,
                                background_colour3,
                                box2)
        self.play(Uncreate(group5_removing1))
        self.wait()

        exp3 = MathTex(r"\frac{(x+1)^3}{3}")
        exp3.move_to(denominator1.get_center())

        self.play(ReplacementTransform(denominator1,exp3))

        self.wait()


#For one box that is worng

class Rational3_1(Scene,ReusableEllipse,ReusableRectangles):
    def construct(self):
# |=========|Create title=========
        text1 = Text("Proper Rational Function", gradient=[TEAL_A,TEAL_E],sheen_factor=-0.75).scale(0.75).shift([0,3,0])
        
# |=========|Create the integral|=========|
        integral1 =  MathTex(
                r"\int",       # 0: integral symbol
                r"{",          # 1: opening brace
                r"2x",         # 2: 2x term (single mobject)
                r"+",          # 3: plus sign
                r"5",          # 4: constant 5
                r"\over",      # 5: fraction line
                r"x",          # 6: base x
                r"^2",         # 7: exponent as single mobject (^2)
                r"}",          # 8: closing brace
                r"\,",         # 9: small space
                r"dx",         # 10: differential
            color=TEAL_A,
            sheen_factor=-0.25).next_to(text1[0], DOWN, buff=0.8).scale(1.15)
        self.play(Write(text1,run_time=1),Write(integral1,run_time=0.75))
        
#|=========| Box the denominator (x^2)|=========|
        #list comprehension:
        denominator_indices1=[6,7]
        denominator1 = VGroup(*[integral1[i] for i in denominator_indices1])
        box1 = ReusableRectangles(denominator1)
        self.play(Create(box1))
        self.wait(2)

# ====== COPY AND MOVE THE BOX ======
        box1_copy = box1.highlight_at_position(box1.get_center())
        self.play(box1_copy.animate.shift([4,0,0]))
        self.wait(0.5)
        
        # Add equals sign
        equals = Text("=", color=RED).next_to(box1_copy, RIGHT)
        self.play(Write(equals))
        
        # Add denominator copy
        denominator_copy = denominator1.copy()
        self.play(denominator_copy.animate.next_to(equals, RIGHT))
        self.wait(0.5)
        
# ====== CREATE PRIME VERSION ======
        prime_group = box1.create_prime_version()
        prime_group.set_color(BLUE)
        prime_group.next_to(box1_copy, DOWN)
        self.play(DrawBorderThenFill(prime_group))
        self.wait(1)
        
# ====== SHOW DERIVATIVE ======
        equals_deriv = equals.copy().set_color(BLUE).next_to(prime_group, RIGHT)
        self.play(Write(equals_deriv))
        
        # Derivative of x^2 is 2x
        derivative_exp = MathTex(r"2x").next_to(equals_deriv, RIGHT)
        self.play(Write(derivative_exp))
        self.wait(1)
        
        # Highlight derivative with ellipse
        deriv_ellipse = ReusableEllipse(derivative_exp, color=BLUE, fill_opacity=0.3)
        self.play(DrawBorderThenFill(deriv_ellipse))
        self.wait(1)
        
 # ====== COMPARE TO NUMERATOR ======
        # Create ellipse around numerator's 2x
        numerator_2x = integral1[2]  # The "2x" term
        num_ellipse = ReusableEllipse(numerator_2x, color=BLUE_C, fill_opacity=0.3)
        self.play(Transform(deriv_ellipse, num_ellipse))
        self.wait(1)
        
        # Show they are the same
        arrow1 = Arrow(derivative_exp.get_bottom(), num_ellipse.get_right(), sheen_factor=0.75, buff=0.2).set_color_by_gradient(BLUE_A,RED_E)
        self.play(GrowArrow(arrow1))
        same_text = Text("Same!", gradient=[BLUE_C,RED_E], sheen_factor=0.5).next_to(num_ellipse, LEFT)
        self.play(Write(same_text))
        self.wait(1)
        
# ====== PLACE CROSS OVER 2x ======
        # Create cross
        cross = Cross(numerator_2x, color=PURE_RED, stroke_width=6)
        
        # Create red circle around the term
        circle = Circle(color=RED, radius=0.5).move_to(numerator_2x.get_center())
        circle.stretch_to_fit_width(numerator_2x.width * 1.5)
        circle.stretch_to_fit_height(numerator_2x.height * 1.5)
        
        # Animate cross and circle
        self.play(Create(circle), Create(cross))
        self.wait(1)
        
        # Flash the cross
        self.play(Flash(cross, color=RED, line_length=0.3, flash_radius=0.7))
        self.wait(2)
        

class Rational3_2(Scene):

    def construct(self):
        # |=========|Create title=========
        text1 = Text("Proper Rational Function", gradient=[TEAL_A,TEAL_E],sheen_factor=-0.75).scale(0.75).shift([0,3,0])
        
        # |=========|Create the integral|=========|
        integral1 = MathTex(
            r"\int",       # 0
            r"{",          # 1
            r"2x",         # 2
            r"+",          # 3
            r"5",          # 4
            r"\over",      # 5
            r"x",          # 6
            r"^2",         # 7
            r"}",          # 8
            r"\,",         # 9
            r"dx",         # 10
            color=TEAL_A,
            sheen_factor=-0.25).next_to(text1[0], DOWN, buff=0.8).scale(1.15)
        self.play(Write(text1), Write(integral1))
        self.wait(0.5)
        
        # ====== SPLITTING THE FRACTION ======
        split_fraction = MathTex(
            r"\int",            # 0
            r"\left(",          # 1
            "{",                # 2
            "2",                # 3
            "x",                # 4
            r"\over",           # 5
            "x",                # 6
            "^2",               # 7
            "}",                # 8
            "+",                # 9
            "{",                # 10
            "5",                # 11
            r"\over",           # 12
            "x",                # 13
            "^2",               # 14
            "}",                # 15
            r"\right)",         # 16
            "dx",               # 17
            color=TEAL_A,
            sheen_factor=-0.25
        ).next_to(text1[0], DOWN, buff=0.8).scale(1.15)
        
        self.play(ReplacementTransform(integral1, split_fraction))
        self.wait(1)
        
        # ====== VISUAL CANCELLATION OF x IN FIRST TERM ======
        # Create copies of the x's to cancel
        x_num = split_fraction[4].copy()
        x_den = split_fraction[6].copy()
        
        # Create crossed versions
        cross_num = Cross(x_num, color=RED, stroke_width=6)
        cross_den = Cross(x_den, color=RED, stroke_width=6)
        
        # Create explosion effects
        explosion_num = VGroup(
            *[Line(ORIGIN, 0.3*RIGHT).rotate(i*PI/4, about_point=ORIGIN)
            for i in range(8)]
        ).move_to(x_num).set_color([YELLOW, ORANGE, RED])
        
        explosion_den = explosion_num.copy().move_to(x_den)
        
        # Create simplified fraction
        simplified_first = MathTex(
                "{",         # 0: opening brace
                "2",         # 1: numerator
                r"\over",    # 2: fraction bar
                "x",         # 3: denominator
                "}"          # 4: closing brace
                ).move_to(VGroup(split_fraction[3], split_fraction[4], split_fraction[5], 
                   split_fraction[6], split_fraction[7]))
        
        
        self.play(
            Flash(x_num, color=RED, line_length=0.2, flash_radius=0.3),
            Flash(x_den, color=RED, line_length=0.2, flash_radius=0.3),
            run_time=1
        )
        self.play(
            Create(cross_num),
            Create(cross_den)
        )
        self.play(
            x_num.animate.scale(1.5).set_color(RED),
            x_den.animate.scale(1.5).set_color(RED),
            run_time=0.5
        )
        self.play(
            FadeIn(explosion_num),
            FadeIn(explosion_den),
            FadeOut(x_num),
            FadeOut(x_den),
            FadeOut(cross_num),
            FadeOut(cross_den),
            run_time=1
        )
        self.play(
            FadeOut(explosion_num),
            FadeOut(explosion_den),
        )
        # Fixed indexing for simplified_first components
        self.play(
            FadeOut(split_fraction[4]),  # Remove numerator x
            FadeOut(split_fraction[7]),  # Remove exponent
            split_fraction[3].animate.move_to(simplified_first[1].get_center()),  # Move 2 to numerator position
            split_fraction[6].animate.move_to(simplified_first[3].get_center()),  # Move denominator x to denominator position
            split_fraction[5].animate.move_to(simplified_first[2].get_center())   # Move fraction bar
        )
        self.wait(1)
        
# ====== DISTRIBUTING THE INTEGRAL SIGN ======
        # Create copies of the integral sign and dx
        integral_sign_1stTerm=split_fraction[0]
        integral_sign_2ndTerm = split_fraction[0].copy()
        dx_sign_1stTerm = split_fraction[17].copy()
        dx_sign_2ndTerm = split_fraction[17]
        
        first_term_indices=[3,5,6]
        first_term1=VGroup(*[split_fraction[i] for i in first_term_indices])
        second_term1_indices=[10,11,12,13,14,15]
        second_term1=VGroup(*[split_fraction[i] for i in second_term1_indices])

        self.play(FadeOut(split_fraction[1]),  # Left parenthesis
                  FadeOut(split_fraction[16]),  # Right parenthesis
                  second_term1.animate.shift(RIGHT*0.35),
                  first_term1.animate.shift(LEFT*0.45)
        )
        self.wait()
        self.play(integral_sign_1stTerm.animate.next_to(first_term1, LEFT, buff=0.1),
                  integral_sign_2ndTerm.animate.next_to(second_term1, LEFT, buff=0.1),
                  dx_sign_1stTerm.animate.next_to(first_term1,RIGHT, buff=0.1),
                  dx_sign_2ndTerm.animate.next_to(second_term1,RIGHT, buff=0.1))
    
#|=========|Grouping first and second term correctly|=========|
        compile_1st_term=VGroup(integral_sign_1stTerm,dx_sign_1stTerm,first_term1)
        compile_2nd_term=VGroup(integral_sign_2ndTerm,dx_sign_2ndTerm,second_term1)


#|=========|Factoring out constant coefficients |=========|
        factor_First_term=MathTex(r"1").next_to(compile_1st_term,LEFT,buff=0.1)
        self.play(compile_2nd_term.animate.shift(RIGHT*0.35),
                  Write(factor_First_term))
        self.wait()
        
        factor_Second_term=MathTex(r"1").next_to(compile_2nd_term,LEFT,buff=0.1)
        self.play(Write(factor_Second_term))
        self.wait()
        self.play(CyclicReplace(split_fraction[3],factor_First_term),
                  CyclicReplace(split_fraction[11],factor_Second_term))



#|=========|boxing and simple|=========|
        box1=ReusableRectangles(mobject=split_fraction[6])
        box2=ReusableRectangles(mobject=split_fraction[13:15])
        self.play(Create(box1),Create(box2))

        box1_copy=box1.highlight_at_position(box1.get_center())
        box2_copy=box2.highlight_at_position(box2.get_center())
        self.play(
        box1_copy.animate.next_to(integral_sign_1stTerm,DOWN,buff=0.4),
        box2_copy.animate.next_to(second_term1,DOWN,buff=0.4))
        self.wait()

        #=
        isEqualTo=Text("=",color=RED).next_to(box1_copy,RIGHT)
        isEqualTo2=Text("=",color=RED).next_to(box2_copy,RIGHT)
        self.play(Write(isEqualTo),Write(isEqualTo2))
        self.wait(0.075)

# copy of denominators
        denominator1=split_fraction[6]
        denominator1_copy=denominator1.copy()
        denominator2=split_fraction[13:15]
        denominator2_copy=denominator2.copy()
        self.play(denominator1_copy.animate.next_to(isEqualTo,RIGHT),
                  denominator2_copy.animate.next_to(isEqualTo2,RIGHT))
        self.wait(0.075)
# ====== CREATE PRIME VERSION ======
        #rect primes:
        prime_group1 = box1.create_prime_version()
        prime_group1.set_color(BLUE_C)
        prime_group1.next_to(box1_copy, DOWN)

        prime_group2 = box2.create_prime_version()
        prime_group2.set_color(BLUE_C)
        prime_group2.next_to(box2_copy, DOWN)
        self.play(DrawBorderThenFill(prime_group1),DrawBorderThenFill(prime_group2))
        self.wait(1)

        #creating = signs 
        isEqualTo_copy=isEqualTo.copy().set_color(BLUE_C)
        isEqualTo2_copy=isEqualTo2.copy().set_color(BLUE_C)

        #placements 
        isEqualTo_copy.next_to(prime_group1,RIGHT)
        isEqualTo2_copy.next_to(prime_group2,RIGHT)

        self.play(Write(isEqualTo_copy),Write(isEqualTo2_copy))
        self.wait(1)

        
# ====== SHOW DERIVATIVE ======
        
        # Derivative of x^2 is 2x
        derivative_exp1=MathTex(r"1")
        derivative_exp2= MathTex(r"2x")
        
        #positioning:
        derivative_exp1.next_to(isEqualTo_copy,RIGHT)
        derivative_exp2.next_to(isEqualTo2_copy, RIGHT)
        #displaying

        self.play(Write(derivative_exp1),Write(derivative_exp2))
        self.wait(1)

        # making a cross 
        cross_derivative_exp2=Cross(mobject=derivative_exp2,color=PURE_RED,stroke_width=3.5)
        self.play(Create(cross_derivative_exp2),run_time=1.5)
        self.wait(1)

        #removing stuff:
        group1_removal=VGroup(cross_derivative_exp2,
                              denominator2_copy,
                              derivative_exp2,
                              box2,
                              box2_copy,
                              prime_group2,
                              isEqualTo2,
                              isEqualTo2_copy)
        self.play(FadeOut(group1_removal))
        self.wait(1)

        #Recreating stuff:
            #denominator
        denominator3=split_fraction[13]
        denominator3_copy=denominator3.copy()
            #Box
        box3=ReusableRectangles(mobject=denominator3)
        self.play(DrawBorderThenFill(box3))
        self.wait(1)
        box3_copy=box3.highlight_at_position(box3.get_center())
        self.play(box3_copy.animate.next_to(second_term1,DOWN))
        self.wait(1)
            #=
        isEqualTo2.next_to(box3_copy,RIGHT)
        self.play(Write(isEqualTo2))
        self.wait(1)
        self.play(denominator3_copy.animate.next_to(isEqualTo2,RIGHT))
            #creating prime version 
        prime_group3 = box3.create_prime_version()
        prime_group3.set_color(BLUE_C)
        prime_group3.next_to(box3_copy, DOWN)
        self.play(DrawBorderThenFill(prime_group3))
        self.wait(1)

        #creating = signs 
        #Already done 

        #placements 
        isEqualTo2_copy.next_to(prime_group3,RIGHT)
        self.play(Write(isEqualTo2_copy))
        self.wait(1)
        #Differentiating:
        derivative_exp3=MathTex(r"1")
        derivative_exp3.next_to(isEqualTo2_copy,RIGHT)
        self.play(Write(derivative_exp3))
        self.wait(1)

        
#|=========|ellipsing|=========|
        ellipso1=ReusableEllipse(mobject=derivative_exp1)
        ellipso2=ReusableEllipse(mobject=derivative_exp3)
        self.play(SpiralIn(ellipso1),SpiralIn(ellipso2))
        self.wait()
        ellipso1_copy=ReusableEllipse(mobject=factor_First_term)
        ellipso2_copy=ReusableEllipse(mobject=factor_Second_term)
        self.play(DrawBorderThenFill(ellipso1_copy),
                  DrawBorderThenFill(ellipso2_copy))
        self.wait()


                #animating integration
        dot1_ellipso1=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso1.next_to(ellipso1_copy,UP,buff=0)
        dot1_ellipso2=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso2.next_to(ellipso2_copy,UP,buff=0)
        self.play(Write(dot1_ellipso1),Write(dot1_ellipso2))
        self.wait()


                #Creating a list for background_colours:
        background_colour=[
        BackgroundRectangle(factor_First_term,color=PURPLE_A),
        BackgroundRectangle(integral_sign_1stTerm,color=PURPLE_A),
        BackgroundRectangle(dx_sign_1stTerm,color=PURPLE_A),
        BackgroundRectangle(factor_Second_term,color=PURPLE_A),
        BackgroundRectangle(integral_sign_2ndTerm,color=PURPLE_A),
        BackgroundRectangle(dx_sign_2ndTerm,color=PURPLE_A)]
                #list comprehension
        animations1_background_colour=[GrowFromCenter(i) for i in background_colour]
        self.play(AnimationGroup(*animations1_background_colour,lag_ratio=0.1))
        self.wait()


                #Creating a list for
        arcs_terms=[ArcBetweenPoints(start=integral_sign_1stTerm.get_top(),
                 end=dot1_ellipso1.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso1.get_center(),
                 end=dx_sign_1stTerm.get_top(),
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=integral_sign_2ndTerm.get_top(),
                 end=dot1_ellipso2.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso2.get_center(),
                 end=dx_sign_2ndTerm.get_top(),
                 angle=-PI/2 )]
        #List comprehension:
        animations2_arcs=[GrowFromCenter(i) for i in arcs_terms]
        self.play(AnimationGroup(*animations2_arcs,lag_ratio=0.1))
        self.wait()


        
        # ====== INTEGRATION STEP ======
        # Create group of elements to remove for first term
        remove_group1 = VGroup(
            ellipso1, ellipso1_copy, dot1_ellipso1,
            background_colour[0], background_colour[1], background_colour[2],
            arcs_terms[0], arcs_terms[1],
            factor_First_term, integral_sign_1stTerm, dx_sign_1stTerm,box1
        )
        
        # Create group of elements to remove for second term
        remove_group2 = VGroup(
            ellipso2, ellipso2_copy, dot1_ellipso2,
            background_colour[3], background_colour[4], background_colour[5],
            arcs_terms[2], arcs_terms[3],
            factor_Second_term, integral_sign_2ndTerm, dx_sign_2ndTerm,box3
        )
        
        # Animate removal with shrinking effect
        self.play(
            remove_group1.animate.scale(0.1).set_opacity(0),
            remove_group2.animate.scale(0.1).set_opacity(0),
            run_time=1.5
        )
        self.remove(remove_group1, remove_group2)
        self.wait(1)
        
        # ====== SHOW INTEGRATION RESULTS ======
        # Create solutions
        solution1_final = MathTex("2",     # 0: coefficient
                            
                    
                            r"\ln",  # 1: logarithm
                            "|",     # 2: absolute value start
                            "x",     # 3: the variable
                            "|"      # 4: absolute value end
        ).move_to(compile_1st_term.get_center())
        solution2 = MathTex(
    "{",      # 0: opening brace
    "5",      # 1: numerator
    r"\over", # 2: fraction line
    "x",      # 3: denominator base
    "^2",     # 4: exponent
    "}"       # 5: closing brace
).move_to(compile_2nd_term.get_center())

        self.play(compile_1st_term.animate.shift(UP*0.3),
            ReplacementTransform(compile_1st_term,solution1_final,path_arc=PI/2,run_time=1.5))
        self.wait()
        self.play(split_fraction[9].animate.next_to(solution1_final,RIGHT,buff=0.1))
        self.wait()
        self.play(
            ReplacementTransform(compile_2nd_term,solution2,path_arc=PI/2,run_time=1.5))
        self.wait()
        self.play(
            solution2.animate.next_to(split_fraction[9],RIGHT,buff=0.1))
        self.wait()
        solution2_simple = MathTex(
    "5",       # 0: coefficient
    "x",       # 1: base
    "^{-2}"    # 2: negative exponent
).move_to(solution2.get_center())
        solution2_simple_working= MathTex(
    r"{",        # 0: open brace
    "5",         # 1: coefficient
    "x",         # 2: base
    "^{-2+1}",   # 3: exponent
    r"\over",    # 4: fraction bar
    "-2",        # 5: denominator first term
    "+",         # 6: plus sign
    "1",         # 7: denominator second term
    "}"          # 8: close brace
).move_to(solution2_simple.get_center())
        solution2_final= MathTex(
    "{",         # 0: open brace
    "-",
    "5",        # 1: numerator
    r"\over",    # 2: fraction bar
    "x",         # 3: denominator
    "}"          # 4: close brace
).move_to(solution2_simple_working.get_center())
        self.play(TransformMatchingTex(solution2,solution2_simple,path_arc=PI/2,run_time=1.5))
        self.wait()
        self.play(TransformMatchingTex(solution2_simple,solution2_simple_working,path_arc=PI/2,run_time=1.5))
        self.wait()
        self.play(TransformMatchingTex(solution2_simple_working,solution2_final,path_arc=PI/2,run_time=1.5))
        text2=MathTex(r"+C")
        text2.next_to(solution2_final,RIGHT,buff=0.1)
        self.play(Write(text2))
        self.wait()
        
# get boxes for 2 terms
class Rational4_1(Scene):
    def construct(self):
        # |=========|Create title=========
        text1 = Text("Proper Rational Function", gradient=[TEAL_A,TEAL_E],sheen_factor=-0.75).scale(0.75).shift([0,3,0])
        self.play(Write(text1))
        
        # |=========|Create the integral|=========|
        integral1 = MathTex(
    "{",                  # 0: open fraction
    r"\text{numerator}",  # 1: numerator
    r"\over",             # 2
    "(",                  # 3
    "x",                  # 4
    "+",                  # 5
    "p",                  # 6
    ")",                  # 7
    "(",                  # 8
    "x",                  # 9
    "+",                  # 10
    "q",                  # 11
    ")",                  # 12
    "}",                  # 13: close fraction
    "=",                  # 14
    "{",                  # 15: start A/(x+p)
    "A",                  # 16
    r"\over",             # 17
    "x",                  # 18
    "+",                  # 19
    "p",                  # 20
    "}",                  # 21: end A/(x+p)
    "+",                  # 22
    "{",                  # 23: start B/(x+q)
    "B",                  # 24
    r"\over",             # 25
    "x",                  # 26
    "+",                  # 27
    "q",                  # 28
    "}",                  # 29: end B/(x+q)
    color=TEAL_A,
    sheen_factor=-0.25
).next_to(text1, DOWN, buff=0.6).scale(0.75)
        
        self.play(Write(integral1))
        self.wait()
        
        integral1_repeated = MathTex(
    "{",                    # 0
    r"\text{numerator}",    # 1
    r"\over",               # 2
    "(",                    # 3
    "x",                    # 4
    "+",                    # 5
    "p",                    # 6
    ")",                    # 7
    "(",                    # 8
    "x",                    # 9
    "+",                    # 10
    "p",                    # 11
    ")",                    # 12
    "}",                    # 13
    "=",                    # 14
    "{",                    # 15
    "A",                    # 16
    r"\over",               # 17
    "x",                    # 18
    "+",                    # 19
    "p",                    # 20
    "}",                    # 21
    "+",                    # 22
    "{",                    # 23
    "B",                    # 24
    r"\over",               # 25
    "(",                    # 26
    "x",                    # 27
    "+",                    # 28
    "p",                    # 29
    ")",                    # 30
    "(",                    # 31
    "x",                    # 32
    "+",                    # 33
    "p",                    # 34
    ")",                    # 35
    "}",                    # 36
    color=TEAL_A,
    sheen_factor=-0.25
).next_to(integral1, DOWN, buff=0.6).scale(0.75)
        self.play(Write(integral1_repeated))
        self.wait()

        integral2 = MathTex(
    "{",                    # 0
    r"\text{numerator}",    # 1
    r"\over",               # 2
    "(",                    # 3
    "x",                    # 4
    "^2",                   # 5
    "+",                    # 6
    "p",                    # 7
    ")",                    # 8
    "(",                    # 9
    "x",                    # 10
    "^2",                   # 11
    "+",                    # 12
    "q",                    # 13
    ")",                    # 14
    "}",                    # 15
    "=",                    # 16
    "{",                    # 17
    "A",                    # 18
    "x",                    # 19
    "+",                    # 20
    "B",                    # 21
    r"\over",               # 22
    "x",                    # 23
    "^2",                   # 24
    "+",                    # 25
    "p",                    # 26
    "}",                    # 27
    "+",                    # 28
    "{",                    # 29
    "C",                    # 30
    "x",                    # 31
    "+",                    # 32
    "D",                    # 33
    r"\over",               # 34
    "x",                    # 35
    "^2",                   # 36
    "+",                    # 37
    "q",                    # 38
    "}",                    # 39
    color=TEAL_A,
    sheen_factor=-0.25
).scale(0.75).next_to(integral1_repeated, DOWN, buff=0.6)
        self.play(Write(integral2))
        self.wait()
        integral2_repeated = MathTex(
    "{",                    # 0
    r"\text{numerator}",    # 1
    r"\over",               # 2
    "(",                    # 3
    "x",                    # 4
    "^2",                   # 5
    "+",                    # 6
    "p",                    # 7
    ")",                    # 8
    "(",                    # 9
    "x",                    # 10
    "^2",                   # 11
    "+",                    # 12
    "p",                    # 13
    ")",                    # 14
    "}",                    # 15
    "=",                    # 16
    "{",                    # 17
    "A",                    # 18
    "x",                    # 19
    "+",                    # 20
    "B",                    # 21
    r"\over",               # 22
    "x",                    # 23
    "^2",                   # 24
    "+",                    # 25
    "p",                    # 26
    "}",                    # 27
    "+",                    # 28
    "{",                    # 29
    "C",                    # 30
    "x",                    # 31
    "+",                    # 32
    "D",                    # 33
    r"\over",               # 34
    "(",                    # 35
    "x",                    # 36
    "^2",                   # 37
    "+",                    # 38
    "p",                    # 39
    ")",                    # 40
    "(",                    # 41
    "x",                    # 42
    "^2",                   # 43
    "+",                    # 44
    "p",                    # 45
    ")",                    # 46
    "}",                    # 47
    color=TEAL_A,
    sheen_factor=-0.25
).next_to(integral2, DOWN, buff=0.6).scale(0.75)
        self.play(Write(integral2_repeated))
        self.wait()


        integral1_repeated_simp_secondTerm = MathTex(
    "{",                    # 0
    r"\text{numerator}",    # 1
    r"\over",               # 2
    r"(x + p)^2",           # 3
    "}",                    # 4
    "=",                    # 5
    "{",                    # 6
    "A",                    # 7
    r"\over",               # 8
    "x + p",                # 9
    "}",                    # 10
    "+",                    # 11
    "{",                    # 12
    "B",                    # 13
    r"\over",               # 14
    r"(x + p)^2",           # 15
    "}",                    # 16
).next_to(integral1, DOWN, buff=0.6).scale(0.75)


        integral2_repeated_simp_secondTerm= MathTex(
    "{",                    # 0
    r"\text{numerator}",    # 1
    r"\over",               # 2
    "(",                    # 3
    "x",                    # 4
    "^2",                   # 5
    "+",                    # 6
    "p",                    # 7
    ")",                    # 8
    "^2",                   # 9   <- ADDED: the outer square
    "}",                    # 10
    "=",                    # 11
    "{",                    # 12
    "A",                    # 13
    "x",                    # 14
    "+",                    # 15
    "B",                    # 16
    r"\over",               # 17
    "x",                    # 18
    "^2",                   # 19
    "+",                    # 20
    "p",                    # 21
    "}",                    # 22
    "+",                    # 23
    "{",                    # 24
    "C",                    # 25
    "x",                    # 26
    "+",                    # 27
    "D",                    # 28
    r"\over",               # 29
    "(",                    # 30
    "x",                    # 31
    "^2",                   # 32
    "+",                    # 33
    "p",                    # 34
    ")",                    # 35
    "^2",                   # 36 <- outer exponent again
    "}",                    # 37
    color=TEAL_A,
    sheen_factor=-0.25
).next_to(integral2, DOWN, buff=0.6).scale(0.75)

        #list comprehension:
        # denominator_integral1_indices_LHS=list(range(26,36))
        # denominator_integral1_LHS=VGroup(*[integral1_repeated[i]for i in denominator_integral1_indices_LHS])

        self.play(TransformMatchingTex(integral1_repeated,integral1_repeated_simp_secondTerm))
        self.play(TransformMatchingTex(integral2_repeated,integral2_repeated_simp_secondTerm))
        self.wait()

        
        denominator1 = VGroup(*integral1[3:13])  # from '(' to ')'
        brace1 = Brace(denominator1, direction=DOWN, buff=0.05)
        denominator2 = VGroup(*integral2[3:15])  # adjust indices based on the full quadratic
        brace2 = Brace(denominator2, direction=DOWN, buff=0.05)

        self.play(GrowFromCenter(brace1), GrowFromCenter(brace2))
        self.wait()
        # Labels under the braces
        text2 = Text("Linear Factors").scale(0.5).next_to(brace1, DOWN, buff=0.1)
        text3 = Text("Quadratic Factors").scale(0.5).next_to(brace2, DOWN, buff=0.1)
        self.play(FadeIn(text2), FadeIn(text3))
        self.wait()

        self.play(
            Circumscribe(text2, shape=Rectangle,color=BLUE_A, stroke_width=2))
        self.wait()
        self.play(
            Circumscribe(text3, shape=Rectangle,color=BLUE_E, stroke_width=2),
        )
        self.wait()

        self.remove(integral1,integral1_repeated_simp_secondTerm,integral2,integral2_repeated_simp_secondTerm,brace1,brace2,text2,text1)


        self.play(text3.animate.move_to(ORIGIN).shift([0,3,0]).scale(2.3).shift(RIGHT*1.5))
        self.wait()
        text4=Text("Reducible").scale(1.15).next_to(text3, LEFT, buff=0.15)
        self.play(Write(text4))
        self.wait()


        integral3 = MathTex(
            r"\int",             # 0
            "{",                 # 1
            "1",                 # 2   numerator
            r"\over",            # 3
            "1",                 # 4   coefficient of x^2
            "x",                 # 5
            "^",                 # 6
            "2",                 # 7
            "-",                 # 8
            "7",                 # 9
            "x",                 # 10
            "+",                 # 11
            "12",                # 12
            "}",                 # 13
            "dx",                # 14
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(text4[1], DOWN, buff=0.9)

        self.play(Write(integral3))
        self.wait()

        underline1=Underline(mobject=text4,buff=0.1)
        underline1.set_stroke(PURE_BLUE).set_color_by_gradient(WHITE,BLUE_E).sheen_factor=-0.75
        self.play(Create(underline1))
        self.wait()

        discriminant1 = MathTex(
            "D",         # 0
            "=",         # 1
            "b",         # 2
            "^2",        # 3
            "-",         # 4
            "4",         # 5
            "a",         # 6
            "c",         # 7
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(integral3,RIGHT,buff=2.2)
        self.play(Write(discriminant1))
        self.wait()

        #copying determinant letters
        a_copy=discriminant1[6].copy().move_to(discriminant1[6].get_center()).set_color(BLUE_C) 
        b_copy=discriminant1[2].copy().move_to(discriminant1[2].get_center()) .set_color(TEAL_C) 
        c_copy=discriminant1[7].copy().move_to(discriminant1[7].get_center()) .set_color(MAROON_C) 

        #generating targets 

        for i in (a_copy,b_copy,c_copy):
            i.generate_target()
        a_copy.target.next_to(integral3[4],DOWN,buff=0.2)
        b_copy.target.next_to(integral3[9],DOWN,buff=0.2)
        c_copy.target.next_to(integral3[12],DOWN,buff=0.2)

        #Moving to target 
        self.play(MoveToTarget(a_copy),MoveToTarget(b_copy),MoveToTarget(c_copy))
        self.wait()

        #animating:
        # self.play(a_copy.animate.next_to(integral3[4],DOWN,buff=0.2),
        #           b_copy.animate.next_to(integral3[7],DOWN,buff=0.2),
        #           c_copy.animate.next_to(integral3[10],DOWN,buff=0.2)
        #           )
        # self.wait()
        # self.wait()
#Labeling coefficients for my convenience:
        coeff_a=integral3[4]
        coff_b=integral3[8:10]
        coff_c=integral3[12]

        self.play(
            coeff_a.animate.set_color(a_copy.get_color()),
            coff_b.animate.set_color(b_copy.get_color()),
            coff_c.animate.set_color(c_copy.get_color()),
        )
        self.wait()


        discriminant_sub = MathTex(
            "D",        # 0
            "=",        # 1
            "(",        # 2
            "-",        # 3  # negative sign separated
            "7",        # 4
            ")",        # 5
            "^2",       # 6  # keep exponent together
            "-",        # 7
            "4",        # 8
            "(",        # 9
            "1",        # 10
            ")",        # 11
            "(",        # 12
            "12",       # 13
            ")",        # 14
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(discriminant1, DOWN)
        
    
        discriminant_sub[10].set_color(coeff_a.get_color())
        discriminant_sub[3:5].set_color(coff_b.get_color())
        discriminant_sub[13].set_color(coff_c.get_color())
        
    
        
    
        integral3_denom= MathTex(
            "(",      # 0
            "x",      # 1
            "^2",     # 2
            "-",      # 3
            "7",      # 4
            "x",      # 5
            "+",      # 6
            "12",     # 7
            ")",      # 8
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).move_to(integral3[4:11].get_center())
        self.add(integral3_denom)
        self.play(TransformMatchingTex(integral3_denom,discriminant_sub))
        self.wait()

        discriminant_solved= MathTex(
            "D",   # 0
            "=",   # 1
            "1",   # 2
            color=TEAL_A,
            sheen_factor=-0.25
            ).scale(0.75).next_to(discriminant_sub, DOWN)
        discriminant_sub_copy=discriminant_sub.copy().move_to(discriminant_sub.get_center())
        
        self.play(TransformMatchingTex(discriminant_sub_copy,discriminant_solved))
        self.wait()

#removing everything from the screen after factorizing it, and placing it in the denominator  
# Factored form
        factored_form_integral = MathTex(
            r"\int",     # 0
            "{",         # 1
            "1",         # 2 numerator
            r"\over",    # 3
            "(",         # 4
            "x",         # 5
            "-",         # 6
            "3",         # 7
            ")",         # 8
            "(",         # 9
            "x",         # 10
            "-",         # 11
            "4",         # 12
            ")",         # 13
            "}",         # 14
            "dx",        # 15
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).move_to(integral3.get_center())

# Animation
        self.play(TransformMatchingTex(integral3,factored_form_integral))
        group1_removal=VGroup(discriminant1,
        discriminant_sub,
        discriminant_solved,
        a_copy,b_copy,c_copy)
        self.play(FadeOut(group1_removal))
        
        self.wait()

        # -------------------------
# -------------------------
# Partial fractions & solve A, B (fixed)
# -------------------------

        partial_fraction_form = MathTex(
            "{", "1", r"\over", "(", "x", "-", "3", ")", "(", "x", "-", "4", ")", "}", "=",
            "{", "A", r"\over", "x", "-", "3", "}", "+",
            "{", "B", r"\over", "x", "-", "4", "}",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).move_to(factored_form_integral.get_center() + DOWN*1.2)

        self.play(Write(partial_fraction_form))
        self.wait()

        equation_to_find = MathTex(
            "1", "=", "A", "(", "x", "-", "4", ")", "+", "B", "(", "x", "-", "3", ")",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).next_to(partial_fraction_form, DOWN, buff=0.6)

        self.play(Write(equation_to_find))
        self.wait()

        sub_for_A = MathTex(
            "x", "=", "3", r"\Rightarrow",
            "1", "=", "A", "(", "3", "-", "4", ")", "+", "B", "(", "3", "-", "3", ")",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.7).next_to(equation_to_find, DOWN, buff=0.4)
        underline2_sub_for_A=Underline(sub_for_A[:3])
        self.play(Write(sub_for_A),Create(underline2_sub_for_A))
        self.wait()

        # Fade the B*(3-3) term (indices 14..17 are "(" "3" "-" "3" ")" -> use 14:18)
        group2_removal=VGroup(*sub_for_A[13:])
        self.play(FadeToColor(group2_removal, GREY))
        self.wait()
        zero1=MathTex("0", color=TEAL_A).scale(0.7).next_to(sub_for_A[12], RIGHT, buff=0.1)
        self.play(ShrinkToCenter(group2_removal),
        GrowFromCenter(zero1))
        self.wait()

        step_A = MathTex("1", "=", "-", "A").scale(0.75).next_to(factored_form_integral, RIGHT, buff=2.5)
        self.play(ReplacementTransform(VGroup(*sub_for_A[4:12]), step_A))  # safe morph
        self.wait()

        A_value = MathTex("A", "=", "-", "1", color=TEAL_A, sheen_factor=-0.25).scale(0.75).move_to(step_A.get_center())
        group4_removal=VGroup(sub_for_A,zero1,underline2_sub_for_A)
        self.play(FadeOut(group4_removal),
            TransformMatchingTex(step_A,A_value),path_along_arc=0.5)
        self.wait()

        # Use Transform (not TransformMatchingTex) to avoid tex_string errors

        sub_for_B = MathTex(
            "x", "=", "4", r"\Rightarrow",
            "1", "=", "A", "(", "4", "-", "4", ")", "+", "B", "(", "4", "-", "3", ")",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.7).next_to(equation_to_find, DOWN, buff=0.4)
        underline3_sub_for_B=Underline(sub_for_B[:3])

        self.play(Write(sub_for_B),Create(underline3_sub_for_B))
        self.wait()

        # Fade A*(4-4) term (indices 6..11 -> "A", "(", "4", "-", "4", ")")
        group3_removal=VGroup(*sub_for_B[6:12])
        zero2=MathTex("0", color=TEAL_A).scale(0.7)
        zero2.move_to(group3_removal.get_center())
        self.play(FadeToColor(group3_removal, GREY),
                  ShrinkToCenter(group3_removal),
                  GrowFromCenter(zero2))
        self.wait()

        step_B = MathTex("1", "=", "B", "(", "1", ")", color=TEAL_A).scale(0.75).next_to(A_value, DOWN, buff=0.3)
        self.play(ReplacementTransform(VGroup(*sub_for_B[4:]), step_B))  # use Transform here too
        self.wait()

        B_value = MathTex("B", "=", "1", color=TEAL_A, sheen_factor=-0.25).scale(0.75).move_to(step_B.get_center())
        self.play(TransformMatchingTex(step_B,B_value))
        self.wait()
###########continue from here 
        
        group5_removal=VGroup(sub_for_B,
                              equation_to_find,
                              underline3_sub_for_B,
                              zero2,
                            #   A_value,
                            #   B_value
        )
        self.play(FadeOut(group5_removal),run_time=0.5)
        self.wait()


        partial_with_values = MathTex(
            "{", "1", r"\over", "(", "x", "-", "3", ")", "(", "x", "-", "4", ")", "}", "=",
            "{", "-", "1", r"\over", "x", "-", "3", "}", "+",
            "{", "1", r"\over", "x", "-", "4", "}",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).move_to(partial_fraction_form.get_center())

        self.play(FadeOut(partial_fraction_form),
            TransformMatchingTex(A_value, partial_with_values),
            TransformMatchingTex(B_value,partial_with_values))
        self.wait()

        integral_split1 = MathTex(
            r"\int", "(", "-", "{", "1", r"\over", "x", "-", "3", "}", "+",
            "{", "1", r"\over", "x", "-", "4", "}", ")", "dx",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).move_to(integral3.get_center())

        self.play(FadeOut(factored_form_integral,run_time=0.5),
            TransformMatchingTex(partial_with_values,integral_split1,run_time=0.7 ))
        self.wait()

        integration_step_numeric = MathTex(
            "-",         # 0
            r"\int",     # 1
            "{",         # 2
            "1",         # 3
            r"\over",    # 4
            "x",         # 5
            "-",         # 6
            "3",         # 7
            "}",         # 8
            "dx",        # 9
            "+",         # 10
            r"\int",     # 11
            "{",         # 12
            "1",         # 13
            r"\over",    # 14
            "x",         # 15
            "-",         # 16
            "4",         # 17
            "}",         # 18
            "dx",        # 19
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).move_to(integral_split1.get_center())

#removing round brackets for smoothness using #list comprehension:
        # group6_removal_indices=[1,-2]
        # group6_removal=VGroup(*[integral_split1[i] for i in group6_removal_indices])
        self.play(#FadeOut(group6_removal,run_time=0.6)),
        TransformMatchingTex(integral_split1,integration_step_numeric))
        self.wait()

#Slice notation for denominator
        integration_step_numeric_denom_1stTerm=VGroup(*[integration_step_numeric[5:8]])
        integration_step_numeric_denom_2ndTerm=VGroup(*[integration_step_numeric[15:18]])

                            #|======================|CREATING BOXES:|======================|
#{{{{{{ Boxes }}}}}}
        #Creating Boxes
        box1=ReusableRectangles(integration_step_numeric_denom_1stTerm)
        box2=ReusableRectangles(integration_step_numeric_denom_2ndTerm)
        self.play(Create(box1),Create(box2))
        self.wait(0.5)

        #boxes copies:
        box1_copy=box1.highlight_at_position(box1.get_center())
        box2_copy=box2.highlight_at_position(box2.get_center())
        self.play(box1_copy.animate.shift([5,0,0]))
        self.wait(0.1)
        # Add equals sign
        equals1 = Text("=", color=RED).next_to(box1_copy,RIGHT)
        equals2=equals1.copy()
        #copy of denominator from slice 
        integration_step_numeric_denom_1stTerm_copy=integration_step_numeric_denom_1stTerm.copy()
        integration_step_numeric_denom_2ndTerm_copy=integration_step_numeric_denom_2ndTerm.copy()
        #Animating:
        self.play(Write(equals1))
        self.wait(0.1)
        self.play(integration_step_numeric_denom_1stTerm_copy.animate.next_to(equals1,RIGHT))
        self.wait(0.5)
        self.play(box2_copy.animate.next_to(integration_step_numeric_denom_1stTerm_copy,RIGHT*1.5))
        self.wait(0.1)
        self.play(equals2.animate.next_to(box2_copy,RIGHT))
        self.wait(0.1)
        self.play(integration_step_numeric_denom_2ndTerm_copy.animate.next_to(equals2,RIGHT))
        self.wait(0.5)

# {{{{{{{{{{ Prime rect }}}}}}}}}} 
        box1_prime = box1.create_prime_version().set_color(BLUE_C).move_to(box1_copy.get_center())
        box2_prime = box2.create_prime_version().set_color(BLUE_C).move_to(box2_copy.get_center())

        
        self.play(box1_prime.animate.next_to(box1_copy, DOWN),
                  box2_prime.animate.next_to(box2_copy,DOWN))
        self.wait(1)

        # Add equals sign
        equals_deriv1 = equals1.copy().set_color(BLUE).next_to(box1_prime, RIGHT).shift(DOWN*0.2)
        equals_deriv2 = equals2.copy().set_color(BLUE).next_to(box2_prime, RIGHT).shift(DOWN*0.2)
        self.play(Write(equals_deriv1),
                  Write(equals_deriv2))
        self.wait(0.5)

        # SHOW DERIVATIVE 
        derivative_exp1=MathTex(r"1")
        derivative_exp2= MathTex(r"1")
        
        #positioning:
        derivative_exp1.next_to(equals_deriv1,RIGHT)
        derivative_exp2.next_to(equals_deriv2, RIGHT)
        #displaying

        self.play(Write(derivative_exp1),
                  Write(derivative_exp2))
        self.wait(1)

        
                            #|======================|CREATING ELLIPSOS:|======================|
# {{{{{{{{{{ ellipsing }}}}}}}}}} 
        ellipso1=ReusableEllipse(mobject=derivative_exp1)
        ellipso2=ReusableEllipse(mobject=derivative_exp2)
        self.play(SpiralIn(ellipso1),SpiralIn(ellipso2))
        self.wait()
# {{{{{{{{{{ assignining variabels }}}}}}}}}} 
        numerator_1stTerm=factor_First_term=integration_step_numeric[3]
        numerator_2ndTerm=factor_Second_term=integration_step_numeric[13]

        integral_sign_1stTerm=integration_step_numeric[1]
        integral_sign_2ndTerm=integration_step_numeric[11]

        dx_sign_1stTerm=integration_step_numeric[9]
        dx_sign_2ndTerm=integration_step_numeric[19]


# {{{{{{{{{{ Using ellipsos on numerator }}}}}}}}}} 
        ellipso1_copy=ReusableEllipse(mobject=factor_First_term)
        ellipso2_copy=ReusableEllipse(mobject=factor_Second_term)
        self.play(DrawBorderThenFill(ellipso1_copy),
                  DrawBorderThenFill(ellipso2_copy))
        self.wait()


# {{{{{{{{{{ Creating Dots }}}}}}}}}} 
        dot1_ellipso1=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso1.next_to(ellipso1_copy,UP,buff=0)
        dot1_ellipso2=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso2.next_to(ellipso2_copy,UP,buff=0)
        self.play(Write(dot1_ellipso1),Write(dot1_ellipso2))
        self.wait()


                #Creating a list for background_colours:
        background_colour=[
        BackgroundRectangle(factor_First_term,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(integral_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(dx_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(factor_Second_term,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(integral_sign_2ndTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(dx_sign_2ndTerm,color=PURPLE_A,fill_opacity=0.3)]
                #list comprehension
        animations1_background_colour=[GrowFromCenter(i) for i in background_colour]    #
        self.play(AnimationGroup(*animations1_background_colour,lag_ratio=0.1))
        self.wait()


                #Creating a list for
        arcs_terms=[ArcBetweenPoints(start=integral_sign_1stTerm.get_top(),
                 end=dot1_ellipso1.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso1.get_center(),
                 end=dx_sign_1stTerm.get_top(),
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=integral_sign_2ndTerm.get_top(),
                 end=dot1_ellipso2.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso2.get_center(),
                 end=dx_sign_2ndTerm.get_top(),
                 angle=-PI/2 )]
        #List comprehension:
        animations2_arcs=[GrowFromCenter(i) for i in arcs_terms]
        self.play(AnimationGroup(*animations2_arcs,lag_ratio=0.1))
        self.wait()

        
        # ====== INTEGRATION STEP ======
        # Create group of elements to remove for first term
        remove_group1 = VGroup(
            ellipso1, ellipso1_copy, dot1_ellipso1,
            background_colour[0], background_colour[1], background_colour[2],
            arcs_terms[0], arcs_terms[1],
            factor_First_term, integral_sign_1stTerm, dx_sign_1stTerm,box1
        )
        
        # Create group of elements to remove for second term
        remove_group2 = VGroup(
            ellipso2, ellipso2_copy, dot1_ellipso2,
            background_colour[3], background_colour[4], background_colour[5],
            arcs_terms[2], arcs_terms[3],
            factor_Second_term, integral_sign_2ndTerm, dx_sign_2ndTerm,box2
        )
        
        # Animate removal with shrinking effect
        self.play(
            remove_group1.animate.scale(0.1).set_opacity(0),
            remove_group2.animate.scale(0.1).set_opacity(0),
            run_time=1.5
        )
        self.remove(remove_group1, remove_group2)
        self.wait(1)
        







#####################
#####################
#####################
#####################

        final_result_numeric = MathTex(
            "-", r"\ln", "|x", "-", "3", "|", "+", r"\ln", "|x", "-", "4", "|", "+", "C",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.75).move_to(integration_step_numeric.get_center())
        final_result_numeric.shift(LEFT*0.3)
        final_result_numeric_copy=final_result_numeric.copy()

        self.play(TransformMatchingTex(integration_step_numeric, final_result_numeric_copy))
        self.wait()

        simplified_final = MathTex(
            r"\ln", r"\left(", r"\frac{|x - 4|}{|x - 3|}", r"\right)", "+", "C",
            color=TEAL_A, sheen_factor=-0.25
        ).scale(0.9).next_to(final_result_numeric, DOWN, buff=0.6)
        simplified_final_copy=simplified_final.copy()

        self.play(TransformMatchingTex(final_result_numeric, simplified_final_copy))
        self.wait()



class Rational4_2(Scene):
    def construct(self):
        # Create title
        text1 = Text("Irreducible Quadratic Factors", gradient=[BLUE_A, BLUE_E], 
                    sheen_factor=-0.75).scale(0.75).shift([0,3,0])
        
        # Create the integral
        integral1 = MathTex(
            r"\int",   # 0
            "{",       # 1
            "1",       # 2  numerator
            r"\over",  # 3
            "1",       # 4  coeff of x^2 (explicit)
            "x",       # 5
            "^2",      # 6  keep ^2 together
            "-",       # 7
            "6",       # 8
            "x",       # 9
            "+",       # 10
            "12",      # 11
            "}",       # 12
            "dx",      # 13
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(text1[1], DOWN, buff=0.9)

        self.play(Write(text1), Write(integral1))
        self.wait(0.5)
###################################
###################################
###################################

        underline1=Underline(mobject=text1[0:10],buff=0.1)
        underline1.set_stroke(PURE_BLUE).set_color_by_gradient(WHITE,BLUE_E).sheen_factor=-0.75
        self.play(Create(underline1))
        self.wait()

        discriminant1 = MathTex(
            "D",         # 0
            "=",         # 1
            "b",         # 2
            "^2",        # 3
            "-",         # 4
            "4",         # 5
            "a",         # 6
            "c",         # 7
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(integral1,RIGHT,buff=2.2)
        self.play(Write(discriminant1))
        self.wait()

        #copying determinant letters
        a_copy=discriminant1[6].copy().move_to(discriminant1[6].get_center()).set_color(BLUE_C) 
        b_copy=discriminant1[2].copy().move_to(discriminant1[2].get_center()) .set_color(TEAL_C) 
        c_copy=discriminant1[7].copy().move_to(discriminant1[7].get_center()) .set_color(MAROON_C) 

        #generating targets 

        for i in (a_copy,b_copy,c_copy):
            i.generate_target()
        a_copy.target.next_to(integral1[4],DOWN,buff=0.2)
        b_copy.target.next_to(integral1[8],DOWN,buff=0.2)
        c_copy.target.next_to(integral1[11],DOWN,buff=0.2)

        #Moving to target 
        self.play(MoveToTarget(a_copy),MoveToTarget(b_copy),MoveToTarget(c_copy))
        self.wait()

#Labeling coefficients for my convenience:
        coeff_a=integral1[4]
        coff_b=integral1[8:10]
        coff_c=integral1[11]

        self.play(
            coeff_a.animate.set_color(a_copy.get_color()),
            coff_b.animate.set_color(b_copy.get_color()),
            coff_c.animate.set_color(c_copy.get_color()),
        )
        self.wait()


        discriminant_sub = MathTex(
            "D",        # 0
            "=",        # 1
            "(",        # 2
            "-",        # 3  # negative sign separated
            "6",        # 4
            ")",        # 5
            "^2",       # 6  # keep exponent together
            "-",        # 7
            "4",        # 8
            "(",        # 9
            "1",        # 10
            ")",        # 11
            "(",        # 12
            "12",       # 13
            ")",        # 14
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(discriminant1, DOWN)
        
    
        discriminant_sub[10].set_color(coeff_a.get_color())
        discriminant_sub[3:5].set_color(coff_b.get_color())
        discriminant_sub[13].set_color(coff_c.get_color())
        
    
        
    
        integral1_denom= MathTex(
            "(",      # 0
            "x",      # 1
            "^2",     # 2
            "-",      # 3
            "7",      # 4
            "x",      # 5
            "+",      # 6
            "12",     # 7
            ")",      # 8
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.75).move_to(integral1[4:11].get_center()).shift([0.1,-0.05,0])
        self.add(integral1_denom)
        self.play(TransformMatchingTex(integral1_denom,discriminant_sub))
        self.wait()

        discriminant_solved= MathTex(
            "D",   # 0
            "=",   # 1
            "-",   # 2
            "12",  #3
            color=TEAL_A,
            sheen_factor=-0.25
            ).scale(0.75).next_to(discriminant_sub, DOWN)
        discriminant_sub_copy=discriminant_sub.copy().move_to(discriminant_sub.get_center())
        
        self.play(TransformMatchingTex(discriminant_sub_copy,discriminant_solved))
        self.wait()

                            #|======================|REMOVING OLD STUFF|======================|
        group1_removal_discriminant=VGroup(discriminant1,
                                           discriminant_sub,
                                           discriminant_solved,
                                           a_copy,
                                           b_copy,
                                           c_copy,
                                           )
        self.play(FadeOut(group1_removal_discriminant))
        self.wait(0.2)




###################################
###################################
###################################
                            #|======================|Boxing denominator invalidation proof|======================|

        # Highlight denominator
        denominator1 = VGroup(*integral1[4:12])
        box1 = ReusableRectangles(denominator1)
        self.play(Create(box1))
        self.wait(2)

# ====== COPY AND MOVE THE BOX ======
        box1_copy = box1.highlight_at_position(box1.get_center())
        self.play(box1_copy.animate.shift([4,0,0]))
        self.wait(0.2)
        
        # Add equals sign
        equals = Text("=", color=RED).next_to(box1_copy, RIGHT)
        self.play(Write(equals))
        self.wait(0.2)
        
        # Add denominator copy
        denominator_copy = denominator1.copy()
        self.play(denominator_copy.animate.next_to(equals, RIGHT))
        self.wait(0.5)
        
# ====== CREATE PRIME VERSION ======
        prime_group = box1.create_prime_version()
        prime_group.set_color(BLUE)
        prime_group.next_to(box1_copy, DOWN)
        self.play(DrawBorderThenFill(prime_group))
        self.wait(1)
        
# ====== SHOW DERIVATIVE ======
        equals_deriv = equals.copy().set_color(BLUE).next_to(prime_group, RIGHT)
        self.play(Write(equals_deriv))
        
        # Derivative of x^2 is 2x
        derivative_exp = MathTex(
            "2",   # 0
            "x",   # 1
            "-",   # 2
            "6",   # 3
            color=TEAL_A,
            sheen_factor=-0.25
        ).next_to(equals_deriv, RIGHT)
        self.play(Write(derivative_exp))
        self.wait(1)
        
        # Highlight derivative with ellipse
        deriv_ellipse = ReusableEllipse(derivative_exp, color=BLUE, fill_opacity=0.3)
        self.play(DrawBorderThenFill(deriv_ellipse))
        self.wait(1)
        
 # ====== COMPARE TO NUMERATOR ======
        # Create ellipse around numerator's 2x
        numerator1 = integral1[2]  # The "2x" term
        num_ellipse = ReusableEllipse(numerator1, color=BLUE_C, fill_opacity=0.3)
        self.play(Transform(deriv_ellipse, num_ellipse))
        self.wait(1)
        

# ====== PLACE CROSS OVER 2x-6 (numerator1)======
        # Create cross
        cross = Cross(numerator1, color=PURE_RED, stroke_width=6)
        
        # Create red circle around the term
        circle = Circle(color=RED, radius=0.5).move_to(numerator1.get_center())
        circle.stretch_to_fit_width(numerator1.width * 1.5)
        circle.stretch_to_fit_height(numerator1.height * 1.5)
        
        # Animate cross and circle
        self.play(Create(circle), Create(cross))
        self.wait(1)
        
        # Flash the cross
        self.play(Flash(cross, color=RED, line_length=0.3, flash_radius=0.7))
        self.wait(2)


                            #|======================|REMOVING OLD STUFF|======================|
         # REMOVING OLD STUFF
        group1_removal_Boxing=VGroup(box1,
                                     box1_copy,
                                     equals,
                                     denominator_copy,
                                     prime_group,
                                     equals_deriv,
                                     derivative_exp,
                                     deriv_ellipse,
                                     num_ellipse,
                                     cross,
                                     circle)
        self.play(FadeOut(group1_removal_Boxing))
        self.wait(2)
        
        ##########################################################
        ################ COMPLETING THE SQUARE ###################
        ##########################################################
        
        # Title for completing the square
        comp_title = Text("Completing the Square").scale(0.65).set_color_by_gradient(RED,GREEN)
        comp_title.next_to(integral1, DOWN, buff=0.8)
        self.play(Write(comp_title))
        self.wait(0.5)
        
        # Show the denominator expression
        denom_expr = MathTex(
            "x", "^2", "-", "6", "x", "+", "12",
            color=TEAL_A
        ).scale(0.9).next_to(comp_title, DOWN, buff=0.5)
        self.play(Write(denom_expr))
        self.wait(0.5)
        
        # Step 1: Group x terms
        step1 = MathTex(
            "\\left(", "x", "^2", "-", "6", "x", "\\right)", "+", "12",
            color=TEAL_A
        ).scale(0.9).move_to(denom_expr.get_center())
        self.play(TransformMatchingTex(denom_expr,step1))
        self.wait(1)


        step2 = MathTex(
            "x",      # 0
            "^2",     # 1
            "-",      # 2
            "6",      # 3
            "x",      # 4
            "+",      # 5
            "(",      # 6
            "-",      # 7
            "3",      # 8
            ")",      # 9
            "^2",     # 10
            "-",      # 11
            "(",      # 12
            "-",      # 13
            "3",      # 14
            ")",      # 15
            "^2",     # 16
            "+",      # 17
            "12",     # 18
            color=TEAL_A
        ).scale(0.9).move_to(step1.get_center())
        self.play(TransformMatchingTex(step1, step2))
        self.wait(0.4)

        # Always-redraw curved arc from the first token (x^2) to the first (-3)^2

        step2_xVariable=[step2[0]]
        step2_3Coeff=[step2[8]]
        curved_arc = always_redraw(
            lambda: ArcBetweenPoints(
                step2_xVariable[0].get_bottom() + DOWN * 0.15,
                step2_3Coeff[0].get_bottom() + DOWN * 0.15,
                angle=PI / 2,
            ).set_stroke(width=3).set_color_by_gradient(BLUE_C,GRAY_C,TEAL_C)
        )
        # Add it so it is visible and will be updated each frame
        self.play(Create(curved_arc))
        self.wait(0.25)

        # Prepare the perfect-square target and overall target expression
        step3 = MathTex(
            "(",      # 0
            "x",      # 1
            "-",      # 2
            "3",      # 3
            ")",      # 4
            "^2",     # 5
            "-",      # 6
            "(",      # 7
            "-",      # 8
            "3",      # 9
            ")",      # 10
            "^2",     # 11
            "+",      # 12
            "12",     # 13
            color=GREEN
        ).scale(0.9).move_to(step2.get_center())

        self.play(
            TransformMatchingTex(step2, step3, path_along_edge=0.4),
            run_time=0.9,
        )
        self.wait(0.5)
        step2_xVariable[0]=step3[1]
        step2_3Coeff[0]=step3[3]

        step4 = MathTex(
            "(",      # 0
            "x",      # 1
            "-",      # 2
            "3",      # 3
            ")",      # 4
            "^2",     # 5
            "+",      # 6
            "3",      # 7
            color=GREEN
        ).scale(0.9).move_to(step3.get_center())

        self.play(TransformMatchingTex(step3,step4),
                  FadeOut(curved_arc))
        self.wait(0.2)
        self.play(step4[0:5].animate.set_color(RED),
                  step4[7].animate.set_color(PURE_GREEN))
        self.wait(0.2)

        integral2_comp_sq=MathTex(
            r"\int",      # 0: integral sign
            "{",          # 1: fraction start
            "1",          # 2: numerator
            r"\over",     # 3: division
            "(",          # 4
            "x",          # 5
            "-",          # 6
            "3",          # 7
            ")",          # 8
            "^2",         # 9
            "+",          # 10
            "3",          # 11
            "}",          # 12: fraction end
            "dx",         # 13: differential
            color=TEAL_A,
            sheen_factor=-0.25
        ).scale(0.9).move_to(integral1.get_center())
        integral2_comp_sq[4:9].set_color(RED)
        integral2_comp_sq[11].set_color(GREEN_C)
        group2_removal_comp=VGroup(comp_title)
        self.play(FadeOut(group2_removal_comp),
                  TransformMatchingTex(integral1,integral2_comp_sq),
                  TransformMatchingTex(step4,integral2_comp_sq))
        self.wait(1)
                            #|======================|Labelling|======================|
# {{{{{{{{{{ Boxing AND Highlighting constant }}}}}}}}}} 
        #boxes
        box2=ReusableRectangles(integral2_comp_sq[4:9])
        self.play(Create(box2))

        #Constant a^2 
        text2=MathTex(
            "a",   # 0
            "^2",  # 1
        ).next_to(integral2_comp_sq[11],DOWN*2).set_color_by_gradient(GREEN_A,GREEN_D)
        equals2 = Text("=", color=PURE_GREEN).next_to(text2,RIGHT)
        self.play(Write(text2),run_time=1.75)
        self.wait(1)

        #Highlighting 
        self.play(Indicate(box2,scale_factor=1.25),Indicate(integral2_comp_sq[4:9],scale_factor=0.65))
        self.wait(1)
        self.play(Indicate(text2,scale_factor=1.25,color=PURE_GREEN),Indicate(integral2_comp_sq[11],scale_factor=0.65,color=PURE_GREEN))
        self.wait(1)


        #Red box move CONTINUING 
        box2_copy=box2.highlight_at_position(box2.get_center())
        self.play(box2_copy.animate.shift([4.5,0,0]))
        self.wait(0.2)

        #equals for box
        equals1= Text("=", color=RED).next_to(box2_copy,RIGHT)
        self.play(Write(equals1))
        self.wait(0.2)

        #Denom
        integral2_comp_sq_Denom=integral2_comp_sq[4:9]
        integral2_comp_sq_Denom_copy=integral2_comp_sq_Denom.copy()
        self.play(integral2_comp_sq_Denom_copy.animate.next_to(equals1,RIGHT))

        #Creating a rect prime 
        rect_Prime=box2_copy.create_prime_version()
        rect_Prime.set_color(BLUE_C)
        rect_Prime.next_to(box2_copy,DOWN)
        self.play(DrawBorderThenFill(rect_Prime)) # Displaying the rectangle and prime symbol
        self.wait(0.2)

           # SHOW DERIVATIVE EXPRESSION 
        equals1_prime =equals1.copy().set_color(BLUE_C)
        equals1_prime.next_to(rect_Prime, RIGHT)
        self.play(Write(equals1_prime))
        self.wait(0.2)

        #Differentiation:
        derivative_exp1=MathTex(r"1")
        derivative_exp1.next_to(equals1_prime,RIGHT)
        self.play(Write(derivative_exp1))
        self.wait(0.2)
                            #|======================|CREATING ELLIPSOS:|======================|
        #ellipsos
        ellipso1=ReusableEllipse(mobject=derivative_exp1)
        ellipso1_copy=ReusableEllipse(mobject=integral2_comp_sq[2])
        self.play(Create(ellipso1))
        self.play(ReplacementTransform(ellipso1,ellipso1_copy))
        self.wait(0.2)

        #Creating dots 
        dot1_ellipso1=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso1.next_to(ellipso1_copy,UP,buff=0)
        self.wait(0.2)
        

        #labelling stuff
        factor_First_term=integral2_comp_sq[2]
        integral_sign_1stTerm=integral2_comp_sq[0]
        dx_sign_1stTerm=integral2_comp_sq[13]

        #Creating a list for background_colours:
        background_colour=[
        BackgroundRectangle(factor_First_term,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(integral_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(dx_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3)]
        #list comprehension
        animations1_background_colour=[GrowFromCenter(i) for i in background_colour]    
        self.play(AnimationGroup(*animations1_background_colour,lag_ratio=0.1))
        self.wait()


        #Creating a list for
        arcs_terms=[ArcBetweenPoints(start=integral_sign_1stTerm.get_top(),
                 end=dot1_ellipso1.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso1.get_center(),
                 end=dx_sign_1stTerm.get_top(),
                 angle=-PI/2 )]
        #List comprehension:
        animations2_arcs=[GrowFromCenter(i) for i in arcs_terms]
        self.play(AnimationGroup(*animations2_arcs,lag_ratio=0.25))
        self.wait()

        
                                                # ====== INTEGRATION STEP ======
        # Create group of elements to remove for first term
        remove_group1 = VGroup(
            ellipso1, ellipso1_copy, dot1_ellipso1,
            background_colour[0], background_colour[1], background_colour[2],
            arcs_terms[0], arcs_terms[1],
            factor_First_term, integral_sign_1stTerm, dx_sign_1stTerm,box1,
            text2
        )
        
        # Animate removal with shrinking effect
        self.play(
            remove_group1.animate.scale(0.1).set_opacity(0),
            run_time=1.5
        )
        self.remove(remove_group1)
        self.wait(1)

        #Integration 
        solution = MathTex(
            "{",          # 0  start outer fraction
            "1",          # 1  outer numerator
            r"\over",     # 2  outer \over
            r"\sqrt{",    # 3  outer sqrt start
            "3",          # 4  outer sqrt radicand
            "}",          # 5  outer sqrt end
            "}",          # 6  end outer fraction

            r"\tan^{-1}", # 7  arctan^{-1} symbol (kept as one token)
            "(",          # 8  open arctan argument

            "{",        # 9  start inner fraction (numerator = x-3)
            "x",        #10
            "-",        #11
            "3",        #12
            r"\over",   #13 inner \over
            r"\sqrt{",  #14 inner sqrt start
            "3",        #15 inner sqrt radicand
            "}",        #16 inner sqrt end
            "}",        #17 end inner fraction

            ")",          #18 close arctan argument
            "+",          #19 plus
            "C",          #20 constant
            color=TEAL_A
        ).scale(0.9).next_to(integral2_comp_sq,DOWN*2.5)  # replace 
        solution[3:6].set_color(PURE_GREEN)
        solution[14:17].set_color(PURE_GREEN)
        solution[9:13].set_color(RED)

        integral2_comp_sq_copy1=integral2_comp_sq.copy()

        self.play(TransformMatchingTex(integral2_comp_sq_copy1,solution),
                  rate_func=smooth,
                  run_time=1.75)
        self.wait(0.2)
        self.play(Circumscribe(mobject=solution,type=Rectangle,time_width=1.75,color=PURE_GREEN))
        self.wait(2)



class Rational5(Scene):
    def construct(self):
        # Create texts objects
        text1 = Text("Rational Function", gradient=[TEAL_B, YELLOW_B]).scale(1.5).scale(0.5).shift([0, 3, 0])
        text2 = Text("Proper", color=TEAL_B, sheen_factor=-0.3).scale(0.75).shift([-4, 0, 0])
        text3 = Text("Improper", color=YELLOW_B, sheen_factor=-0.3).scale(0.75).shift([4, 0, 0])
        dot1=Dot(color=BLACK).shift([-4, 0, 0])
        dot2=Dot(color=BLACK).shift([4, 0, 0])

# Create arrows with accurate positions now
        arrow1 = always_redraw(lambda: Line(
            start=text1.get_bottom(),
            end=dot1.get_top(),
            buff=0.5,
            color=TEAL_B,
        ).add_tip())

        arrow2 = always_redraw(lambda: Line(
            start=text1.get_bottom(),
            end=dot2.get_top(),
            buff=0.5,
            color=YELLOW_B,
        ).add_tip())

# Writing integrals

        integral1 = MathTex(
            r"\int",  # 0: integral sign
            "{",      # 1: begin grouping of integrand
            "x",      # 2: numerator
            r"\over", # 3: fraction bar
            "x^2",    # 4: denominator part 1
            "+",      # 5: denominator part 2
            "1",      # 6: denominator part 3
            "}",      # 7: end grouping of integrand
            r"\,",    # 8: small space
            "dx",     # 9: differential
            color=TEAL_A,
            sheen_factor=-0.25).next_to(text2, DOWN, buff=0.5)

        integral2 = MathTex(
            r"\int",    # 0
            "{",        # 1  begin fraction
            "2",        # 2  numerator: coefficient
            "x^3",      # 3  numerator: x^3
            "-",        # 4
            "4",        # 5
            "x^2",      # 6
            "-",        # 7
            "x",        # 8
            "-",        # 9
            "3",        # 10 numerator: constant
            r"\over",   # 11 fraction bar (infix)
            "x^2",      # 12 denominator: x^2
            "-",        # 13
            "2",        # 14
            "x",        # 15
            "-",        # 16
            "3",        # 17 denominator: constant
            "}",        # 18 end fraction
            "dx",       # 19 differential
            color=YELLOW_B,
            sheen_factor=-0.25
        ).next_to(text3, DOWN, buff=0.5)

        integ2_after_decomp = MathTex(
            r"\int",    # 0
            "(",        # 1 open integrand
            "2",        # 2 coefficient
            "x",        # 3 variable (so 2 and x are separate)
            "+",        # 4 plus
            "{",        # 5 begin inner fraction
            "5",        # 6 numerator: 5
            "x",        # 7 numerator: x
            "-",        # 8 minus
            "3",        # 9 numerator: 3
            r"\over",   #10 infix fraction bar
            "x^2",      #11 denominator: x^2 (kept together)
            "-",        #12
            "2",        #13
            "x",        #14
            "-",        #15
            "3",        #16
            "}",        #17 end inner fraction
            ")",        #18 close integrand
            r"\,",      #19 small space
            "dx",       #20 differential
            color=YELLOW_B,
            sheen_factor=-0.75
        ).next_to(text3, DOWN, buff=0.5)
        

# Animate everything
        group1=VGroup(text1,arrow1,arrow2,dot1,dot2)
        self.play(Create(group1))
        self.wait(0.5)
        self.play(
            ReplacementTransform(dot1,text2),
            ReplacementTransform(dot2,text3),
        )
        self.wait(1)
        self.play(Write(integral1),
                  Write(integral2))
        self.wait(1)
        self.play(Indicate(text3,color=YELLOW,scale_factor=0.75),
                  TransformMatchingTex(integral2,integ2_after_decomp),
                  run_time=1.5)
        self.wait(1)

#cranking integral 2 elsewhere:
        group2=VGroup(text2,integral1)
        dot3=Dot(point=[-4,0,0],color=TEAL_C,radius=0.1)

        svg=SVGMobject("atomBomb.svg")
        svg.shift(ORIGIN).scale(1)
        
        self.play(ReplacementTransform(group2,dot3,run_time=0.5),
                  Uncreate(arrow1),
                  rate_func=smooth)
        self.wait(1)
        self.play(
            dot3.animate.shift([2.5, -1, 0]),
            ReplacementTransform(dot3, svg,path_along_arc=-PI/2),
            rate_func=smooth,
            run_time=1.5
        )
        self.wait(1)
        self.play(svg.animate.shift([0,-5,0]),rate_func=smooth)
        self.wait(1)
        
# Shifting text3 next to text1:
        self.play(Uncreate(arrow2))
        self.play(text3.animate.next_to(text1,LEFT).shift([0.1,-0.05,0]),play_time=1.35)
        self.wait(0.125)
        self.play(integ2_after_decomp.animate.
                  next_to(text3,DOWN,buff=0.5).
                  shift(LEFT * text2.width / 2).
                  scale(1.15))
        self.wait(0.1)




            ############################        |Moving to main animation|        ############################

                            #|======================|CREATING PARTIAL FRACTIONS:|======================|

# {{{{{{{{{{ Expanding expression }}}}}}}}}} o
        expr1 = MathTex(
        "2",        # 0         coefficient multiplying the first integral
        r"\int",    # 1         integral sign
        "x",        # 2         integrand of first integral
        "dx",       # 3         differential of first integral
        "+",        # 4         plus
        r"\int",    # 5         integral sign for second term
        "{",        # 6         begin inner fraction
        "5",        # 7         numerator: 5
        "x",        # 8         numerator: x
        "-",        # 9         numerator: -
        "3",        # 10        numerator: 3
        r"\over",   # 11        infix fraction bar
        "x^2",      # 12        denominator: x^2 (kept together)
        "-",        # 13
        "2",        # 14
        "x",        # 15
        "-",        # 16
        "3",        # 17
        "}",        # 18        end inner fraction
        "dx",       # 19        differential of second integral
        color=YELLOW_B,
        sheen_factor=-0.76
    ).move_to(integ2_after_decomp.get_center()).shift([0.1,-0.05,0])
        
        self.play(TransformMatchingTex(integ2_after_decomp,expr1))
        self.wait()


                            #|======================|Solving first term:|======================|

 # {{{{{{{{{{ #Creating focus of box }}}}}}}}}} 
        focus_box1=SurroundingRectangle(expr1[0:4])
        self.play(Create(focus_box1),
                  FocusOn(expr1[0:4],run_time=2.5))
        self.wait()

 # {{{{{{{{{{ #integrating the first term. }}}}}}}}}} 
        expr1_FirstTerm_simplification = MathTex(
            "{",      # 0 open fraction
            "x",      # 1 base
            "^2",     # 2 exponent (kept together)
            r"\over", # 3 infix fraction bar
            "2",      # 4 denominator
            "}",      # 5 close fraction
            "+",      # 6 plus
            "C",      # 7 constant letter
            "1"       # 8 constant index / digit
        ).next_to(focus_box1,DOWN)

# {{{{{{{{{{ #REWRITING the answer after simplification }}}}}}}}}} 
        expr2 = MathTex(
            "x",        # 0
            "^2",       # 1
            "+",        # 2
            r"\int",    # 3
            "{",        # 4  begin inner fraction
            "5",        # 5  numerator: 5
            "x",        # 6  numerator: x
            "-",        # 7  numerator: -
            "3",        # 8  numerator: 3
            r"\over",   # 9  infix fraction bar
            "x",        #10  denominator: x (now separate)
            "^2",       #11  denominator: ^2 (now separate)
            "-",        #12
            "2",        #13
            "x",        #14
            "-",        #15
            "3",        #16
            "}",        #17  end inner fraction
            "dx",       #18  differential
            color=YELLOW_B,
            sheen_factor=-0.76
        ).move_to(expr1.get_center()).shift([0.1, -0.05, 0])
        
        self.play(TransformMatchingTex(expr1,expr2))
        self.wait()

                            #|======================|Solving second term:|======================|

# {{{{{{{{{{ #Creating focus of box2 for second term }}}}}}}}}} 
        focus_box2=SurroundingRectangle(expr2[3:19])
        self.play(ReplacementTransform(focus_box1,focus_box2),
                  FocusOn(expr2[3:19],run_time=2.5))
        self.wait()

# {{{{{{{{{{ #UNderlining  }}}}}}}}}} 
        underline1=Underline(mobject=text3,buff=0.1)
        underline1.set_stroke(PURE_BLUE).set_color_by_gradient(WHITE,YELLOW_E).sheen_factor=-0.75
        self.play(Create(underline1))
        self.wait()


# {{{{{{{{{{ discriminant check:  }}}}}}}}}} 
        discriminant1 = MathTex(
            "D",         # 0
            "=",         # 1
            "b",         # 2
            "^2",        # 3
            "-",         # 4
            "4",         # 5
            "a",         # 6
            "c",         # 7
            color=YELLOW_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(expr2,RIGHT,buff=2.2)
        self.play(Write(discriminant1))
        self.wait()

        #copying determinant letters
        a_copy=discriminant1[6].copy().move_to(discriminant1[6].get_center()).set_color(TEAL_C) 
        b_copy=discriminant1[2].copy().move_to(discriminant1[2].get_center()) .set_color(GOLD_C) 
        c_copy=discriminant1[7].copy().move_to(discriminant1[7].get_center()) .set_color(PURPLE_C) 

        #generating targets 

        for i in (a_copy,b_copy,c_copy):
            i.generate_target()
        a_copy.target.next_to(expr2[10],DOWN,buff=0.2)
        b_copy.target.next_to(expr2[12:14],DOWN,buff=0.2)
        c_copy.target.next_to(expr2[15:17],DOWN,buff=0.2)

        #Moving to target 
        self.play(MoveToTarget(a_copy),MoveToTarget(b_copy),MoveToTarget(c_copy))
        self.wait()

        #Labeling coefficients for my convenience:
        coeff_a=expr2[10]
        coff_b=expr2[12:14]
        coff_c=expr2[15:17]

        self.play(FadeToColor(coeff_a,TEAL_A),
                  FadeToColor(coff_b,GREEN_A),
                  FadeToColor(coff_c,YELLOW_A))
        self.wait()

        #substituting the values
        discriminant_sub = MathTex(
            "D",   # 0
            "=",   # 1
            "(",   # 2
            "-",   # 3  negative sign for -2
            "2",   # 4
            ")",   # 5
            "^2",  # 6  keep exponent together
            "-",   # 7
            "4",   # 8
            "(",   # 9
            "1",   #10
            ")",   #11
            "(",   #12
            "-",   #13 negative sign for -3
            "3",   #14
            ")",   #15
            color=YELLOW_A,
            sheen_factor=-0.25
        ).scale(0.75).next_to(discriminant1, DOWN)
        
    
        discriminant_sub[10].set_color(a_copy.get_color())
        discriminant_sub[3:5].set_color(b_copy.get_color())
        discriminant_sub[13:15].set_color(c_copy.get_color())
        
    
        
    #Denominator copy 
        integral3_denom= MathTex(
            "x",    # 0
            "^2",   # 1
            "-",    # 2
            "2",    # 3
            "x",    # 4
            "-",    # 5
            "3",    # 6
            color=YELLOW_A,
            sheen_factor=-0.25
        ).move_to(expr2[10:19].get_center()).shift([0.1,-0.05,0])
        self.add(integral3_denom)
        self.play(TransformMatchingTex(integral3_denom,discriminant_sub))
        self.wait()

    #Final answer of discriminant 
        discriminant_solved= MathTex(
            "D",   # 0
            "=",   # 1
            "16",   # 2
            color=YELLOW_A,
            sheen_factor=-0.25
            ).scale(0.75).next_to(discriminant_sub, DOWN)
        discriminant_sub_copy=discriminant_sub.copy().move_to(discriminant_sub.get_center())
        
        self.play(TransformMatchingTex(discriminant_sub_copy,discriminant_solved))
        self.wait()

    #removing everything from the screen after factorizing it, and placing it in the denominator  
# Factored form
        factored_form_integral =MathTex(
            "{",        # 0  open fraction
            "5",        # 1  numerator: 5
            "x",        # 2  numerator: x
            "-",        # 3  numerator: -
            "3",        # 4  numerator: 3
            r"\over",   # 5  infix fraction bar
            "(",        # 6  open first factor in denom
            "x",        # 7
            "-",        # 8
            "3",        # 9
            ")",        #10  close first factor
            "(",        #11  open second factor
            "x",        #12
            "+",        #13
            "1",        #14
            ")",        #15  close second factor
            "}",        #16  close fraction
            color=YELLOW_B,
            sheen_factor=-0.76
        ).move_to(expr2[3:19].get_center())


        self.play(factored_form_integral.animate.next_to(focus_box2,DOWN).shift([-2.5,0,0]))
        self.wait()


        
# Animation

        group1_removal=VGroup(discriminant1,
        discriminant_sub,
        discriminant_solved,
        a_copy,b_copy,c_copy)
        self.play(FadeOut(group1_removal))
        
        self.wait()

        # -------------------------
# -------------------------
# Partial fractions & solve A, B (fixed)
# -------------------------

        partial_fraction_form = MathTex(
            "{",        # 0  open fraction
            "5",        # 1
            "x",        # 2
            "-",        # 3
            "3",        # 4
            r"\over",   # 5  fraction bar
            "(",        # 6
            "x",        # 7
            "-",        # 8
            "3",        # 9
            ")",        #10
            "(",        #11
            "x",        #12
            "+",        #13
            "1",        #14
            ")",        #15
            "}",        #16 close fraction
            "=",        #17
            "{",        #18 open first partial fraction
            "A",        #19
            r"\over",   #20
            "x",        #21
            "-",        #22
            "3",        #23
            "}",        #24 close first fraction
            "+",        #25
            "{",        #26 open second partial fraction
            "B",        #27
            r"\over",   #28
            "x",        #29
            "+",        #30
            "1",        #31
            "}",        #32 close second fraction
            color=YELLOW_A,
            sheen_factor=-0.25
        ).scale(0.75).move_to(factored_form_integral.get_center()).shift([1,0,0])

        self.play(TransformMatchingTex(factored_form_integral,partial_fraction_form))
        self.wait()

        equation_to_find = MathTex(
            "5", "x", "-", "3",
            "=", 
            "A", "(", "x", "+", "1", ")",
            "+",
            "B", "(", "x", "-", "3", ")",
            color=GOLD_A, sheen_factor=-0.25
        ).scale(0.75).next_to(partial_fraction_form, DOWN, buff=0.6)

        self.play(Write(equation_to_find))
        self.wait()

        sub_for_A = MathTex(
            "x", "=", "3", r"\Rightarrow",
            "12", "=",                # 5*3 - 3 = 12
            "A", "(", "3", "+", "1", ")", "+", "B", "(", "3", "-", "3", ")",
            color=GOLD_B, sheen_factor=-0.25
        ).scale(0.75).next_to(equation_to_find, DOWN, buff=0.4)
        underline2_sub_for_A=Underline(sub_for_A[:3])
        self.play(Write(sub_for_A),Create(underline2_sub_for_A,run_time=2))
        self.wait()

        # Fade the B*(3-3) term (indices 14..17 are "(" "3" "-" "3" ")" -> use 14:18)
        group2_removal=VGroup(*sub_for_A[13:])
        self.play(FadeToColor(group2_removal, GREY))
        self.wait()
        zero1=MathTex("0", color=GOLD_B).scale(0.7).next_to(sub_for_A[12], RIGHT, buff=0.1)
        self.play(ShrinkToCenter(group2_removal),
        GrowFromCenter(zero1))
        self.wait()

        step_A = MathTex("12", "=", "4", "A",color=GOLD_B).scale(0.75).next_to(factored_form_integral, RIGHT, buff=2.5)
        self.play(ReplacementTransform(VGroup(*sub_for_A[4:12]), step_A))  # safe morph
        self.wait()

        A_value = MathTex("A", "=", "3", color=GOLD_C, sheen_factor=-0.25).scale(0.75).move_to(step_A.get_center())
        group4_removal=VGroup(sub_for_A,zero1,underline2_sub_for_A)
        self.play(FadeOut(group4_removal),
            TransformMatchingTex(step_A,A_value),path_along_arc=0.5)
        self.wait()

        # Use Transform (not TransformMatchingTex) to avoid tex_string errors

        sub_for_B = MathTex(
            "x", "=", "-", "1", r"\Rightarrow",
            "-", "8", "=",            # 5*(-1) - 3 = -8  (kept '-' and digits separate)
            "A", "(", "-", "1", "+", "1", ")", "+", "B", "(", "-", "1", "-", "3", ")",
            color=GOLD_B, sheen_factor=-0.25
        ).scale(0.7).next_to(equation_to_find, DOWN, buff=0.4)
        underline3_sub_for_B=Underline(sub_for_B[:5])

        self.play(Write(sub_for_B),Create(underline3_sub_for_B,run_time=2))
        self.wait()

        # Fade A*(4-4) term (indices 9..15 -> 
        group3_removal=VGroup(*sub_for_B[9:16])
        zero2=MathTex("0", color=GOLD_B).scale(0.7)
        zero2.move_to(group3_removal.get_center())
        self.play(FadeToColor(group3_removal, GREY),
                  ShrinkToCenter(group3_removal),
                  GrowFromCenter(zero2))
        self.wait()

        step_B = MathTex("-", "8", "=", "-", "4", "B", color=GOLD_B).scale(0.75).next_to(A_value, DOWN, buff=0.3)
        self.play(ReplacementTransform(VGroup(*sub_for_B[4:]), step_B))  # use Transform here too
        self.wait()

        B_value = MathTex("B", "=", "2", color=GOLD_C, sheen_factor=-0.25).scale(0.75).move_to(step_B.get_center())
        self.play(TransformMatchingTex(step_B,B_value))
        self.wait()
###########continue from here 
        
        group5_removal=VGroup(sub_for_B,
                              equation_to_find,
                              underline3_sub_for_B,
                              zero2,
                            #   A_value,
                            #   B_value
        )
        self.play(FadeOut(group5_removal),run_time=0.5)
        self.wait()

# {{{{{{{{{{ Substitutiing values of A and B at their places  }}}}}}}}}} 
        partial_with_values = MathTex(
            "{", "5", "x", "-", "3", r"\over",
            "(", "x", "-", "3", ")", "(", "x", "+", "1", ")", "}",
            "=",
            "{", "3", r"\over", "x", "-", "3", "}",
            "+",
            "{", "2", r"\over", "x", "+", "1", "}",
            color=GOLD_D, sheen_factor=-0.25
        ).scale(0.75).move_to(partial_fraction_form.get_center())

        self.play(FadeOut(partial_fraction_form),
            TransformMatchingTex(A_value, partial_with_values),
            TransformMatchingTex(B_value,partial_with_values))
        self.wait()

        
        integral_split1 = MathTex(
            "x", "^2", "+",
            "3", r"\int", "{", "1", r"\over", "x", "-", "3", "}", "dx",
            "+",
            "2", r"\int", "{", "1", r"\over", "x", "+", "1", "}", "dx",
            color=YELLOW_A, sheen_factor=-0.25
        ).scale(0.75).move_to(expr2.get_center())

        self.play(
            TransformMatchingTex(expr2,integral_split1,rate_func=smooth),
            TransformMatchingTex(partial_with_values,integral_split1,run_time=0.7))
        self.wait()

        integration_step_numeric = MathTex(
            "x",        # 0  x
            "^2",       # 1  ^2 (kept together as requested)
            "+",        # 2  plus
            "3",        # 3  coefficient 3
            r"\int",    # 4  integral sign
            "{",        # 5  open brace for fraction
            "1",        # 6  numerator 1
            r"\over",   # 7  fraction bar
            "x",        # 8  denominator: x
            "-",        # 9  minus
            "3",        # 10 constant 3
            "}",        # 11 close brace for fraction
            "dx",       # 12 differential dx
            "+",        # 13 plus between integrals
            "2",        # 14 coefficient 2
            r"\int",    # 15 integral sign (second)
            "{",        # 16 open brace for second fraction
            "1",        # 17 numerator 1 (second)
            r"\over",   # 18 fraction bar (second)
            "x",        # 19 denominator: x (second)
            "+",        # 20 plus
            "1",        # 21 constant 1
            "}",        # 22 close brace for second fraction
            "dx",        # 23 differential dx (second)
            color=YELLOW_C, sheen_factor=-0.25
        ).scale(0.85).move_to(integral_split1.get_center())


# {{{{{{{{{{ Creating a Focus Box after placing everything back }}}}}}}}}} 
        focus_box3=SurroundingRectangle(integration_step_numeric[3:24]).set_color_by_gradient(YELLOW_A,YELLOW_C,YELLOW_E)

#removing round brackets for smoothness using #list comprehension:

        self.play(#FadeOut(group6_removal,run_time=0.6)),
        TransformMatchingTex(integral_split1,integration_step_numeric),
        ReplacementTransform(focus_box2,focus_box3))
        self.wait()

#Slice notation for denominator
        integration_step_numeric_denom_1stTerm=VGroup(*[integration_step_numeric[8:11]])
        integration_step_numeric_denom_2ndTerm=VGroup(*[integration_step_numeric[19:22]])

                            #|======================|CREATING BOXES:|======================|
#{{{{{{ Boxes }}}}}}
        #Creating Boxes
        box1=ReusableRectangles(integration_step_numeric_denom_1stTerm)
        box2=ReusableRectangles(integration_step_numeric_denom_2ndTerm)
        self.play(Create(box1),Create(box2))
        self.wait(0.5)

        #boxes copies:
        box1_copy=box1.highlight_at_position(box1.get_center())
        box2_copy=box2.highlight_at_position(box2.get_center())
        self.play(box1_copy.animate.shift([5,0,0]))
        self.wait(0.1)
        # Add equals sign
        equals1 = Text("=", color=RED).next_to(box1_copy,RIGHT)
        equals2=equals1.copy()
        #copy of denominator from slice 
        integration_step_numeric_denom_1stTerm_copy=integration_step_numeric_denom_1stTerm.copy()
        integration_step_numeric_denom_2ndTerm_copy=integration_step_numeric_denom_2ndTerm.copy()
        #Animating:
        self.play(Write(equals1))
        self.wait(0.1)
        self.play(integration_step_numeric_denom_1stTerm_copy.animate.next_to(equals1,RIGHT))
        self.wait(0.5)
        self.play(box2_copy.animate.next_to(integration_step_numeric_denom_1stTerm_copy,RIGHT*1.5))
        self.wait(0.1)
        self.play(equals2.animate.next_to(box2_copy,RIGHT))
        self.wait(0.1)
        self.play(integration_step_numeric_denom_2ndTerm_copy.animate.next_to(equals2,RIGHT))
        self.wait(0.5)

# {{{{{{{{{{ Prime rect }}}}}}}}}} 
        box1_prime = box1.create_prime_version().set_color(BLUE_C).move_to(box1_copy.get_center())
        box2_prime = box2.create_prime_version().set_color(BLUE_C).move_to(box2_copy.get_center())

        
        self.play(box1_prime.animate.next_to(box1_copy, DOWN),
                  box2_prime.animate.next_to(box2_copy,DOWN))
        self.wait(1)

        # Add equals sign
        equals_deriv1 = equals1.copy().set_color(BLUE).next_to(box1_prime, RIGHT).shift(DOWN*0.2)
        equals_deriv2 = equals2.copy().set_color(BLUE).next_to(box2_prime, RIGHT).shift(DOWN*0.2)
        self.play(Write(equals_deriv1),
                  Write(equals_deriv2))
        self.wait(0.5)

        # SHOW DERIVATIVE 
        derivative_exp1=MathTex(r"1")
        derivative_exp2= MathTex(r"1")
        
        #positioning:
        derivative_exp1.next_to(equals_deriv1,RIGHT)
        derivative_exp2.next_to(equals_deriv2, RIGHT)
        #displaying

        self.play(Write(derivative_exp1),
                  Write(derivative_exp2))
        self.wait(1)

        
                            #|======================|CREATING ELLIPSOS:|======================|
# {{{{{{{{{{ ellipsing }}}}}}}}}} 
        ellipso1=ReusableEllipse(mobject=derivative_exp1)
        ellipso2=ReusableEllipse(mobject=derivative_exp2)
        self.play(SpiralIn(ellipso1),SpiralIn(ellipso2))
        self.wait()
# {{{{{{{{{{ assignining variabels }}}}}}}}}} 
        numerator_1stTerm=factor_First_term=integration_step_numeric[6]
        numerator_2ndTerm=factor_Second_term=integration_step_numeric[17]

        integral_sign_1stTerm=integration_step_numeric[4]
        integral_sign_2ndTerm=integration_step_numeric[15]

        dx_sign_1stTerm=integration_step_numeric[12]
        dx_sign_2ndTerm=integration_step_numeric[23]


# {{{{{{{{{{ Using ellipsos on numerator }}}}}}}}}} 
        ellipso1_copy=ReusableEllipse(mobject=factor_First_term)
        ellipso2_copy=ReusableEllipse(mobject=factor_Second_term)
        self.play(DrawBorderThenFill(ellipso1_copy),
                  DrawBorderThenFill(ellipso2_copy))
        self.wait()


# {{{{{{{{{{ Creating Dots }}}}}}}}}} 
        dot1_ellipso1=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso1.next_to(ellipso1_copy,UP,buff=0)
        dot1_ellipso2=Dot(ORIGIN,radius=0.1,color=PURPLE_B)
        dot1_ellipso2.next_to(ellipso2_copy,UP,buff=0)
        self.play(Write(dot1_ellipso1),Write(dot1_ellipso2))
        self.wait()


                #Creating a list for background_colours:
        background_colour=[
        BackgroundRectangle(factor_First_term,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(integral_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(dx_sign_1stTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(factor_Second_term,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(integral_sign_2ndTerm,color=PURPLE_A,fill_opacity=0.3),
        BackgroundRectangle(dx_sign_2ndTerm,color=PURPLE_A,fill_opacity=0.3)]
                #list comprehension
        animations1_background_colour=[GrowFromCenter(i) for i in background_colour] 
        self.play(AnimationGroup(*animations1_background_colour,lag_ratio=0.1))
        self.wait()


                #Creating a list for
        arcs_terms=[ArcBetweenPoints(start=integral_sign_1stTerm.get_top(),
                 end=dot1_ellipso1.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso1.get_center(),
                 end=dx_sign_1stTerm.get_top(),
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=integral_sign_2ndTerm.get_top(),
                 end=dot1_ellipso2.get_center(), 
                 angle=-PI/2 ),
                 ArcBetweenPoints(start=dot1_ellipso2.get_center(),
                 end=dx_sign_2ndTerm.get_top(),
                 angle=-PI/2 )]
        #List comprehension:
        animations2_arcs=[GrowFromCenter(i) for i in arcs_terms]
        self.play(AnimationGroup(*animations2_arcs,lag_ratio=0.1))
        self.wait()

        
        # ====== INTEGRATION STEP ======
        # Create group of elements to remove for first term
        remove_group1 = VGroup(
            ellipso1, ellipso1_copy, dot1_ellipso1,
            background_colour[0], background_colour[1], background_colour[2],
            arcs_terms[0], arcs_terms[1],
            factor_First_term, integral_sign_1stTerm, dx_sign_1stTerm,box1
        )
        
        # Create group of elements to remove for second term
        remove_group2 = VGroup(
            ellipso2, ellipso2_copy, dot1_ellipso2,
            background_colour[3], background_colour[4], background_colour[5],
            arcs_terms[2], arcs_terms[3],
            factor_Second_term, integral_sign_2ndTerm, dx_sign_2ndTerm,box2,
            focus_box3
        )
        
        # Animate removal with shrinking effect
        self.play(
            remove_group1.animate.scale(0.1).set_opacity(0),
            remove_group2.animate.scale(0.1).set_opacity(0),
            run_time=1.5
        )
        self.remove(remove_group1, remove_group2)
        self.wait(1)
        





                            #|======================|WRITING FINAL ANSWER|======================|



        final_result_numeric = MathTex(
        "x",        # 0  variable x
        "^2",       # 1  exponent 2
        "+",        # 2  plus
        "3",        # 3  coefficient 3
        r"\ln",     # 4  natural log
        r"\left|",  # 5  open absolute value
        "x",        # 6  variable x
        "-",        # 7  minus
        "3",        # 8  constant 3
        r"\right|", # 9  close absolute value
        "+",        # 10 plus
        "2",        # 11 coefficient 2
        r"\ln",     # 12 natural log
        r"\left|",  # 13 open absolute value
        "x",        # 14 variable x
        "+",        # 15 plus
        "1",        # 16 constant 1
        r"\right|", # 17 close absolute value
        "+",        # 18 plus
        "C",         # 19 constant of integration
        sheen_factor=-0.25
        ).scale(0.85).move_to(integration_step_numeric.get_center()).set_color_by_gradient(WHITE,YELLOW_B)
        final_result_numeric.shift(LEFT*0.3)
        final_result_numeric_copy=final_result_numeric.copy()

        self.play(TransformMatchingTex(integration_step_numeric, final_result_numeric_copy))
        self.wait()
        svg2=SVGMobject("atomBomb.svg").scale(1)

        self.play(ReplacementTransform(text1[0:8],svg2))
        self.wait(2)
        self.play(svg2.animate.shift([0,-2.5,0]),rate_func=smooth)
        self.wait()



class Last(Scene):
    def construct(self):
                                    #|======================|CREATING EQUATION(Lay) |======================|

# {{{{{{{{{{ Title }}}}}}}}}} 
        text1 = Text("Trignometric Substitutions", gradient=[YELLOW_A, YELLOW_E], 
                    sheen_factor=-0.75).scale(1).shift([0,3,0])
        self.play(Write(text1))
        self.wait()

# {{{{{{{{{{ Equations }}}}}}}}}} 
        #First expression 
        sqrt_expr1 = MathTex(
            r"\sqrt{",  # 0  square root start
            "a",        # 1  variable a
            "^2",       # 2  exponent 2
            "+",        # 3  plus
            "x",        # 4  variable x
            "^2",       # 5  exponent 2
            "}",         # 6  close sqrt
            color=YELLOW_A,
            sheen_factor=-0.25
        ).next_to(text1,DL, buff=0.6).scale(0.85).shift(RIGHT*1.5)
        self.play(Write(sqrt_expr1))
        self.wait()

        #Second expression 
        sqrt_expr2 = MathTex(
            r"\sqrt{",  # 0  square root start
            "a",        # 1  variable a
            "^2",       # 2  exponent 2
            "-",        # 3  minus
            "x",        # 4  variable x
            "^2",       # 5  exponent 2
            "}",         # 6  close sqrt
            color=YELLOW_B,
            sheen_factor=-0.25
        ).next_to(sqrt_expr1,RIGHT, buff=1).scale(0.85)
        self.play(Write(sqrt_expr2))
        self.wait()

        #Third expression 
        sqrt_expr3 = MathTex(
            r"\sqrt{",  # 0  square root start
            "x",        # 1  variable x
            "^2",       # 2  exponent 2
            "-",        # 3  minus
            "a",        # 4  variable a
            "^2",       # 5  exponent 2
            "}" ,        # 6  close sqrt
            color=YELLOW_C,
            sheen_factor=-0.25
        ).next_to(sqrt_expr2,RIGHT, buff=1).scale(0.85) 
        self.play(Write(sqrt_expr3))
        self.wait()


# {{{{{{{{{{ Grouping and moving to a side }}}}}}}}}} 
        #Underlining for separation:
        underline1=Underline(text1[-1:-14],color=YELLOW)
        
        #Grouping equations 
        group1_WithEq=VGroup(sqrt_expr1,sqrt_expr2,sqrt_expr3)
        self.play(Create(underline1),
        sqrt_expr2.animate.shift(LEFT*1),
        sqrt_expr3.animate.shift(LEFT*2))
        self.wait(0.25)
        # sqrt_expr2.animate.next_to(sqrt_expr1,RIGHT,buff=0.3),
        # sqrt_expr3.animate.next_to(sqrt_expr2,RIGHT,buff=0.3)

        #Creating a surrounding rectangle:
        roun_Rect1=SurroundingRectangle(group1_WithEq,
                                        corner_radius=0.35,
                                        sheen_factor=0.75).set_color_by_gradient(RED,MAROON)
        self.play(Create(roun_Rect1))
        self.wait()

        #Grouping equations with roun_Rect1
        group2_roun_Rect1=VGroup(group1_WithEq,roun_Rect1)
        self.play(group2_roun_Rect1.animate.scale(0.5/0.85).next_to(text1[-1],DOWN))
        self.wait()
        


        
                            #|======================|CREATING Triangle |======================|
         # Configuration
        HYPOTENUSE_LENGTH = 3
        ADJACENT_LENGTH = 2.5
        ROTATION_SPEED = 0.3
        
        # Create axes for reference (not shown in final animation)
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE},
        )
        
        # Fixed adjacent side (horizontal line)
        adjacent_start = np.array([-3,0,0])
        adjacent_end = adjacent_start+RIGHT*ADJACENT_LENGTH
        adjacent_side = Line(adjacent_start, adjacent_end, color=YELLOW, stroke_width=4)
        
        # Angle tracker
        angle = ValueTracker(PI/180)  # Start at 1 degrees
        
        # Hypotenuse (rotating line)
        def get_hypotenuse_end():
            return adjacent_start + HYPOTENUSE_LENGTH * np.array([
                np.cos(angle.get_value()), 
                np.sin(angle.get_value()), 
                0
            ])
        
        hypotenuse = always_redraw(
            lambda: Line(adjacent_start, get_hypotenuse_end(), color=PURE_RED, stroke_width=4)
        )
        
        # Opposite side (vertical line connecting hypotenuse to adjacent side)
        opposite_side = always_redraw(
            lambda: DashedLine(
                get_hypotenuse_end(), 
                [get_hypotenuse_end()[0], adjacent_start[1], 0],
                color=PURE_GREEN, 
                stroke_width=4
            )
        )
        
        # # Right angle indicator
        # def right_angle_updater():
        #     hyp_end = self._get_hypotenuse_end()
        #     foot = np.array([hyp_end[0], self.adjacent_start[1], 0.0])
        #     # construct two lines that meet at 'foot'
        #     base_line_at_foot = Line(foot, self.adjacent_start)
        #     vertical_line_at_foot = Line(foot, hyp_end)
        #     return RightAngle(base_line_at_foot, vertical_line_at_foot, length=0.18, color=WHITE)
        # self.right_angle = always_redraw(right_angle_updater)  


        right_angle = always_redraw(lambda: (
        RightAngle(
        Line(np.array([get_hypotenuse_end()[0], adjacent_start[1], 0.0]), adjacent_start),
        Line(np.array([get_hypotenuse_end()[0], adjacent_start[1], 0.0]), get_hypotenuse_end()),
        length=0.18,
        color=WHITE)))
        
        # Angle arc and label
        angle_arc = always_redraw(
            lambda: Arc(
                radius=0.4,
                start_angle=0,
                angle=angle.get_value(),
                arc_center=adjacent_start,
                color=BLUE
            )
        )
        
        angle_label = always_redraw(
            lambda: MathTex(r"\theta", color=BLUE).scale(0.8).move_to(
                adjacent_start + 0.6 * np.array([
                    np.cos(angle.get_value()/2), 
                    np.sin(angle.get_value()/2), 
                    0
                ])
            )
        )
        
        # Triangle fill
        triangle_fill = always_redraw(
            lambda: Polygon(
                adjacent_start, 
                get_hypotenuse_end(), 
                [get_hypotenuse_end()[0], adjacent_start[1], 0],
                fill_color=BLUE,
                fill_opacity=0.2,
                stroke_width=0
            ) if get_hypotenuse_end()[0] > 0 else VMobject()
        )
        
        # Labels for sides
        adjacent_label = always_redraw(
            lambda: MathTex("a", color=YELLOW_A).next_to(
                adjacent_side, DOWN, buff=0.1
            )
        )
        
        opposite_label = always_redraw(
            lambda: MathTex("x", color=GREEN_A).next_to(
                opposite_side, RIGHT, buff=0.1
            ) 
            # if get_hypotenuse_end()[0] > 0 else VMobject()
        )
        
        hypotenuse_label = always_redraw(
            lambda: MathTex(
            r"\sqrt{",  # 0  square root start
            "a",        # 1  variable a
            "^2",       # 2  exponent 2
            "+",        # 3  plus
            "x",        # 4  variable x
            "^2",       # 5  exponent 2
            "}",         # 6  close sqrt
            color=RED_A,
            sheen_factor=-0.25).next_to((adjacent_start + get_hypotenuse_end()) / 2,UP,buff=0.1)  # midpoint of hypotenuse
            .rotate(angle.get_value(), about_point=(adjacent_start + get_hypotenuse_end()) / 2))  # rotate with line
        
        # # Angle value display
        # angle_value = always_redraw(
        #     lambda: MathTex(
        #         f"\\theta = {angle.get_value()*180/PI:.1f}^\\circ", 
        #         color=BLUE
        #     ).to_corner(UL)
        # )
        
        # Add all elements to scene
        self.add(triangle_fill)
        self.play(Create(adjacent_side),
                Create(opposite_side),
                Create(hypotenuse))
        # self.wait()
        # self.add(right_angle)
        self.add(angle_arc, angle_label)
        self.play(Write(adjacent_label),
                Write(opposite_label),
                Write(hypotenuse_label))
        self.wait()
        # self.add(angle_value)
        
        # Animate the rotation
        self.play(
            angle.animate.increment_value(33*PI/180), 
            run_time=3, 
            rate_func=smooth
        )
       
        # Keep the final frame for a moment
        self.wait(2)

# {{{{{{{{{{ Highlighting the labels }}}}}}}}}} 
        self.play(Indicate(adjacent_label,scale_factor=0.5,color=YELLOW_C))
        self.wait()
        self.play(Indicate(opposite_label,scale_factor=0.5,color=PURE_GREEN))
        self.wait()
        self.play(Indicate(hypotenuse_label,scale_factor=0.5,color=PURE_RED))
        self.wait()
        self.play(Wiggle(opposite_label,scale_factor=4.5,color=PURE_GREEN,n_wiggles=10,run_time=1))
        self.wait()
        self.play(Circumscribe(adjacent_label,color=YELLOW_C))
        self.wait()
        self.play(ApplyWave(mobject=sqrt_expr1,ripples=3,rate_func=smooth))
        self.wait()



# {{{{{{{{{{ Compiling and moving aside }}}}}}}}}} 
        group3_Triangle1=VGroup(triangle_fill,
                                adjacent_side,opposite_side,hypotenuse,
                                adjacent_label,opposite_label,hypotenuse_label,
                                angle_arc, angle_label)

        self.wait(2)
                            #|======================|TRINAGLE CREATED ABOVE |======================|
#==========================================================================================================================================================
                            #|======================|CREATING 2 MORE TRINAGLES USING FUNCTIONS |======================|
        group3_Triangle1_copy=group3_Triangle1.copy()
        self.play(group3_Triangle1_copy.animate.shift([-3.5,-1,0]).scale(0.7))
        self.wait()

# {{{{{{{{{{ Swapping colors }}}}}}}}}} 
        def animate_swap(scene, m1, m2, run_time=1.0, rate_func=there_and_back):
            c1 = m1.get_color()
            c2 = m2.get_color()
            scene.play(
            m1.animate.set_color(c2),
            m2.animate.set_color(c1),
            run_time=run_time,
            rate_func=rate_func
            )
# {{{{{{{{{{ Creating a second copy for sqrt_expr2 }}}}}}}}}} 
        # 1) create static snapshots of the dynamic labels
        opp_snapshot = opposite_label.copy()
        hyp_snapshot = hypotenuse_label.copy()
        opposite_side_snapshot=opposite_side.copy()
        hypotenuse_side_snapshot=hypotenuse.copy()
        
        # 2) stop them from updating
        opp_snapshot.clear_updaters()
        hyp_snapshot.clear_updaters()
        opposite_side_snapshot.clear_updaters()
        hypotenuse_side_snapshot.clear_updaters()
        
        # 3) put the snapshots where the dynamic labels currently are
        self.add(opp_snapshot, hyp_snapshot,
                opposite_side_snapshot,hypotenuse_side_snapshot)
        
        # 4) remove the dynamic updaters from the scene so they can't interfere
        self.remove(opposite_label, hypotenuse_label,
                    opposite_side,hypotenuse)
        
        # 5) now you can transform snapshots smoothly
        hypotenuse_label2 = MathTex("x").move_to(hyp_snapshot.get_center()
                                       ).next_to((adjacent_start + get_hypotenuse_end()) / 2,UP,buff=0.1
                                       ).rotate(angle.get_value(), about_point=(adjacent_start + get_hypotenuse_end()) / 2)  
        hypotenuse_label2.set_color(opposite_label.get_color())
        self.play(
            CyclicReplace(opp_snapshot, sqrt_expr3),
            TransformMatchingTex(hyp_snapshot, hypotenuse_label2),
            run_time=1.0,
            rate_func=smooth
        )
        self.wait()
        self.play(sqrt_expr3.animate.next_to(opposite_side, RIGHT, buff=0.1).scale(0.85/0.5).shift(RIGHT*0.5).set_color(RED_A))

        animate_swap(self,opp_snapshot, hypotenuse_label2, run_time=1.2, rate_func=smooth)  #opp old x with hyp new x
        # animate_swap(self, sqrt_expr2, opp_snapshot, run_time=1.2, rate_func=smooth)    #old hyp sqrt with new opp sqrt, ruins animation, so done directly above 
        animate_swap(self, opposite_side_snapshot, hypotenuse_side_snapshot, run_time=1.2, rate_func=smooth)
        
        self.wait()
        # optionally remove snapshots and add the new ones afterwards
        # self.remove(opp_snapshot, hyp_snapshot)
        # self.add(sqrt_expr3, hypotenuse_label2)
        group4_Triangle2=VGroup(triangle_fill,
                                adjacent_side,opposite_side_snapshot,hypotenuse_side_snapshot, #Opp and Hyp sides replaced with their respective snapshots
                                adjacent_label,sqrt_expr3,hypotenuse_label2,    #opp label is sqrt_expr3 and hyp label is hypotenuse_label2
                                angle_arc, angle_label)
        
# {{{{{{{{{{ Creating a third copy for sqrt_expr2 }}}}}}}}}} 
        #Copying and shifting 3rd triangle
        group4_Triangle2_copy= group4_Triangle2.copy()
        self.play(group4_Triangle2_copy.animate.shift([3.5,-1,0]).scale(0.7))
        self.wait()

        #Preparing third triangle:
        # {{{{{{{{{{ Creating a second copy for sqrt_expr2 }}}}}}}}}} 
        # 1) create static snapshots of the dynamic labels
        opp_snapshot2 = sqrt_expr3.copy()
        hyp_snapshot2 = hypotenuse_label2.copy()
        adj_snapshot2=adjacent_label.copy()
        opposite_side_snapshot2=opposite_side_snapshot.copy()
        hypotenuse_side_snapshot2=hypotenuse_side_snapshot.copy()
        adjacent_side_snapshot2=adjacent_side.copy()
        #unwanted things to move along:
        group_disposal=VGroup(triangle_fill,angle_arc,angle_label)
        group_disposal_copy=group_disposal.copy()
        
        
        # 2) stop them from updating
        opp_snapshot2.clear_updaters()
        hyp_snapshot2.clear_updaters()
        adj_snapshot2.clear_updaters()
        opposite_side_snapshot2.clear_updaters()
        hypotenuse_side_snapshot2.clear_updaters()
        adjacent_side_snapshot2.clear_updaters()
        for i in group_disposal_copy:
            i.clear_updaters()

        
        # 3) put the snapshots where the dynamic labels currently are
        self.add(opp_snapshot2, hyp_snapshot2,adj_snapshot2,
                opposite_side_snapshot2,hypotenuse_side_snapshot2,adjacent_side_snapshot2,group_disposal_copy)
        
        # 4) remove the dynamic updaters from the scene so they can't interfere
        self.remove(sqrt_expr3, hypotenuse_label2,adjacent_label,
                    opposite_side_snapshot,hypotenuse_side_snapshot,adjacent_side,*group_disposal)
        
        # 5) now you can transform snapshots smoothly

        adjacent_label2 = MathTex("a",color=YELLOW_A).move_to(hyp_snapshot.get_center()
                                       ).next_to((adjacent_start + get_hypotenuse_end()) / 2,UP,buff=0.1
                                       ).rotate(angle.get_value(), about_point=(adjacent_start + get_hypotenuse_end()) / 2) 
        opposite_label2=MathTex("x",color=GREEN_A).next_to(opposite_side_snapshot2,RIGHT,buff=0.1)
        adjacent_label2.set_color(adjacent_side.get_color())
        self.play(
            CyclicReplace(adj_snapshot2, sqrt_expr2),
            TransformMatchingTex(opp_snapshot2,opposite_label2),
            ReplacementTransform(hyp_snapshot2,adjacent_label2),
            run_time=1.0,
            rate_func=smooth
        )
        self.wait()
        self.play(sqrt_expr2.animate.next_to(adjacent_side_snapshot2, DOWN, buff=0.1).shift(DOWN*0.2).scale(0.85/0.5).set_color(RED_A))

        animate_swap(self,opposite_side_snapshot2, adjacent_side_snapshot2, run_time=1.2, rate_func=smooth)  #opp old x with hyp new x
        # animate_swap(self, sqrt_expr2, opp_snapshot, run_time=1.2, rate_func=smooth)    #old hyp sqrt with new opp sqrt, ruins animation, so done directly above 
        animate_swap(self, opposite_side_snapshot2,hypotenuse_side_snapshot2, run_time=1.2, rate_func=smooth)
        
        self.wait()
        # optionally remove snapshots and add the new ones afterwards
        # self.remove(opp_snapshot, hyp_snapshot)
        # self.add(sqrt_expr2, adjacent_label2)
        group5_Triangle3=VGroup(triangle_fill,
                                adjacent_side_snapshot2,opposite_side_snapshot2,hypotenuse_side_snapshot2, #Opp and Hyp sides replaced with their respective snapshots
                                opposite_label2,sqrt_expr2,adjacent_label2,    #opp label is sqrt_expr3 and hyp label is hypotenuse_label2
                                group_disposal_copy)
        # for i in group5_Triangle3:
        #     i.clear_updaters()
        self.play(group5_Triangle3.animate.shift([0,-1,0]).scale(0.7))
        self.wait()

                        #|======================|ADJUSTING EVERYTHING SO TO MAKE IT EASIER TO WRITE ON|======================|
# {{{{{{{{{{ Making VGroups of rect and 3 triangles }}}}}}}}}}
        #Rrmoving the round rectangle 
        group6_downfall1=VGroup(roun_Rect1,sqrt_expr1,adj_snapshot2,opp_snapshot)
        
        #The triangles
        group6_downfall2=VGroup(group3_Triangle1_copy,group4_Triangle2_copy,group5_Triangle3)

        #playing
        self.play(FadeOut(group6_downfall1),
                  group6_downfall2.animate.next_to(text1,DOWN,buff=0.5).scale(0.85/0.7))
        self.wait()
        
class Irrational(Scene):
    def construct(self):
                                #|======================|WRITING DEFINITION:|======================|

# {{{{{{{{{{ Text written and organised }}}}}}}}}} 
        text1 = Tex(
            "Rational ", " = ", "ratio of polynomials.", r"\\[1.2em]",
            "Irrational ", " = ",
            "contains a root or fractional exponent of ", "$x$",
            sheen_factor=-0.6
            ).scale(0.8).shift([0,3,0])
        high1=text1[0].scale(1/0.8).set_color(TEAL_D)
        high2=text1[2].set_color_by_gradient([TEAL_A,TEAL_E])
        high3=text1[4].scale(1/0.8).set_color(YELLOW_D)
        high4=text1[6:8].set_color_by_gradient([YELLOW_A,YELLOW_E])
# {{{{{{{{{{ Underlining text  }}}}}}}}}} 
        underline1=Underline(high1,color=TEAL_E)
        underline2=Underline(high3,color=YELLOW_E)
# {{{{{{{{{{ Showing everything on the screen }}}}}}}}}} 
        self.play(Write(text1,rate_func=smooth),
                  Create(underline1),
                  Create(underline2))
        self.wait()
    
                            #|======================|DISPLAYING EQUATIONS AND MORPHING:|======================|
# {{{{{{{{{{ Equation created: underroot a𝑥² + bx +c }}}}}}}}}} 
        expr1 = MathTex(
            r"\sqrt{",   # 0  start square root
            "a",         # 1
            "x",         # 2
            "^2",        # 3
            "+",         # 4
            "b",         # 5
            "x",         # 6
            "+",         # 7
            "c",         # 8
            "}",         # 9  close square root
            color=YELLOW_B,
            sheen_factor=-0.6
        ).next_to(text1,DOWN,buff=2.2)
        expr1[1:4].set_color(RED_B)
        expr1[5:7].set_color(TEAL_B)
        expr1[8].set_color(BLUE_B)


# {{{{{{{{{{ Showing everything on the screen }}}}}}}}}} 
        self.play(Write(expr1))
        self.wait()


# {{{{{{{{{{ Equation created: underroot a² + 𝑥² }}}}}}}}}} 
        expr2 = MathTex(
            r"\sqrt{",   # 0  start square root
            "a",         # 1
            "^2",        # 2
            "+",         # 3
            "x",         # 4
            "^2",        # 5
            "}",         # 6  close square root
            color=YELLOW_B,
            sheen_factor=-0.6
        )
        expr2[4:6].set_color(RED_B)
        expr2[1:3].set_color(BLUE_B)


        self.play(TransformMatchingTex(expr1,expr2))
        self.wait()

# {{{{{{{{{{ Equation created: underroot a² - 𝑥² }}}}}}}}}} 
        rep1 = MathTex(r"-",color=YELLOW_B,sheen_factor=-0.6).move_to(expr2[3].get_center())
        self.play(ReplacementTransform(expr2[3],rep1))
        self.wait()

# {{{{{{{{{{ Equation created: underroot  𝑥² - a²  }}}}}}}}}} 

        #1) Equation created: underroot 𝑥² - a²:
        self.play(CyclicReplace(expr2[1:3],expr2[4:6]))
        self.wait()
        
class Outro(Scene):
    def construct(self):
        svg1=SVGMobject("ManimCommunity.svg")
        svg2=SVGMobject("icons8-davinci-resolve.svg")
        self.play(DrawBorderThenFill(svg1,run_time=3.0))
        self.wait(2)
        self.play(ReplacementTransform(svg1,svg2,run_time=2.0))
        self.wait(2)

#The end ;-),Syed Rafay Shahzad 

