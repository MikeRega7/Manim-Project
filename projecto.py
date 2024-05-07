#!/usr/bin/python3
# Juan Miguel Regalado Nuño

from manim import *

class TransformFunctionWithDetailedMath(Scene):
    def construct(self):
        # Texto introductorio más completo
        intro_text = Text("Transformaremos paso a paso una función cuadrática en una función lineal.", font_size=24)
        self.play(Write(intro_text), run_time=5)
        self.play(FadeOut(intro_text), run_time=2)

        # Define las ecuaciones y los pasos matemáticos en LaTeX
        quadratic_eq = MathTex("f(x) = x^2", color=BLUE)
        step1 = MathTex(r"\text{Paso 1: Identificar términos. }", color=WHITE)
        step2 = MathTex(r"\text{Paso 2: Eliminar } x^2.", color=WHITE)
        linear_eq = MathTex("g(x) = x", color=GREEN)

        # Posicionamiento de los textos
        step1.next_to(quadratic_eq, DOWN)
        step2.next_to(step1, DOWN)
        linear_eq.next_to(step2, DOWN)

        # Muestra la ecuación cuadrática y el primer paso
        self.play(Write(quadratic_eq), run_time=3)
        self.play(Write(step1), run_time=4)

        # Explicación de eliminación del término cuadrático
        self.play(Write(step2), run_time=4)

        # Transición a la ecuación lineal
        self.play(ReplacementTransform(quadratic_eq, linear_eq), run_time=4)
        self.play(FadeOut(step1), FadeOut(step2), run_time=2)

        # Gráficos de las funciones con explicaciones
        graph_quadratic = FunctionGraph(lambda x: x**2, x_range=[-10, 10], color=BLUE)
        graph_linear = FunctionGraph(lambda x: x, x_range=[-10, 10], color=GREEN)
        graph_explanation = Text("Observa cómo la gráfica cuadrática se transforma en una lineal.", font_size=24).to_edge(DOWN)

        # Muestra y transforma las gráficas
        self.play(Create(graph_quadratic), run_time=4)
        self.play(Write(graph_explanation), run_time=3)
        self.play(Transform(graph_quadratic, graph_linear), run_time=5)

        # Conclusión detallada
        conclusion_text = Text("La transformación ha sido completada: la función ahora es lineal.", font_size=24).to_edge(DOWN)
        self.play(FadeOut(graph_quadratic), FadeOut(graph_explanation), Create(graph_linear), run_time=3)
        self.play(Write(conclusion_text), run_time=4)

        # Finaliza mostrando la nueva ecuación con tiempo para absorber la información
        self.play(Write(linear_eq), run_time=3)
        self.play(FadeOut(linear_eq), FadeOut(conclusion_text), FadeOut(graph_linear), run_time=2)
