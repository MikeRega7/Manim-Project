#!/usr/bin/python3
# Miguel Regalado
from manim import *

class TransformFunctionWithDetailedLatex(Scene):
    def construct(self):
        # Texto introductorio explicando la tarea
        intro_text = Text("Vamos a transformar la función cuadrática en una función lineal.", font_size=24)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Define las ecuaciones en LaTeX
        quadratic_eq = MathTex("f(x) = x^2", color=BLUE)
        linear_eq = MathTex("g(x) = x", color=GREEN)
        transformation_explanation = MathTex(r"\text{Eliminamos el término } x^2 \text{ para hacerla lineal}", color=WHITE)

        # Posiciona la ecuación lineal y la explicación abajo de la cuadrática
        linear_eq.next_to(quadratic_eq, DOWN)
        transformation_explanation.next_to(linear_eq, DOWN)

        # Muestra la ecuación cuadrática
        self.play(Write(quadratic_eq), run_time=2)  # Ajusta la duración de la animación
        self.wait(1)

        # Explica la transformación
        self.play(Write(transformation_explanation), run_time=2)  # Ajusta la duración de la animación
        self.wait(2)

        # Transición de la ecuación cuadrática a lineal con una explicación
        self.play(ReplacementTransform(quadratic_eq, linear_eq), run_time=3)  # Ajusta la duración de la animación
        self.wait(1)
        self.play(FadeOut(transformation_explanation))

        # Ahora, crea los gráficos de las funciones
        graph_quadratic = FunctionGraph(lambda x: x**2, x_range=[-10,10], color=BLUE)
        graph_linear = FunctionGraph(lambda x: x, x_range=[-10,10], color=GREEN)
        graph_explanation = Text("Observa la transformación de la gráfica", font_size=24).to_edge(DOWN)

        # Muestra la gráfica cuadrática
        self.play(Create(graph_quadratic), run_time=2)  # Ajusta la duración de la animación
        self.wait(1)

        # Explica la transformación de la gráfica
        self.play(Write(graph_explanation), run_time=2)  # Ajusta la duración de la animación
        self.wait(1)

        # Transforma el gráfico de la función cuadrática en el gráfico lineal
        self.play(Transform(graph_quadratic, graph_linear), run_time=3)  # Ajusta la duración de la animación
        self.wait(1)

        # Conclusión
        self.play(FadeOut(graph_quadratic), FadeOut(graph_explanation))
        conclusion_text = Text("La función ahora es lineal!", font_size=24).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(2)

        # Muestra el gráfico final
        self.play(Create(graph_linear), run_time=2)  # Ajusta la duración de la animación
        self.wait(2)

        # Finaliza mostrando la nueva ecuación
        self.play(Write(linear_eq), run_time=2)  # Ajusta la duración de la animación
        self.wait(2)

        # Limpia la pantalla
        self.play(FadeOut(linear_eq), FadeOut(conclusion_text), FadeOut(graph_linear))

