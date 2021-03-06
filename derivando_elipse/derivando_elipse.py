from manim import *
from pathlib import Path
import os
import itertools as it
from typing import *



class DerivandoElipse(Scene):
    def construct(self):
        self.abertura()
        self.init_dados()
        self.init_objetos()
        self.mostrar_definicoes_em_objetos()
        self.mostrar_definicoes()
        self.manipulacao_algebrica()
        self.fechamento()

    def init_dados(self):
        a = 3
        b = 2
        c = np.sqrt(a**2 - b**2 if a >= b else b**2 - a**2)
        f1, f2 = ((-c, 0, 0), (c, 0, 0)) if a >= b else ((0, -c, 0), (0, c, 0))
        self.a = a
        self.b = b
        self.c = c
        self.f1 = f1
        self.f2 = f2
        
    
    def init_objetos(self):
        escala_objetos = 0.6
        posicao_objetos = 4*LEFT
        cor_elipse = RED
        cor_focos = GREEN
        cor_ponto = PURPLE
        cor_c = BLUE
        cor_b = ORANGE
        cor_a = YELLOW
        posicao_definicoes = 4*RIGHT
        escala_definicoes = 0.6
        cor_segmento_focal = MAROON
        posicao_def_elipse = 2*RIGHT

        # -------- Elementos da Elipse --------

        # -------- Eixos --------
        eixos = Axes(x_length=2*(self.a+1), x_axis_config={"include_ticks": False}, y_axis_config={"include_ticks": False})
        eixos_labels = eixos.get_axis_labels("x", "y")

        # -------- Elipse --------
        elipse = Ellipse(width=2*self.a, height=2*self.b).set_color(cor_elipse)
        elipse_label = MathTex("E").move_to(elipse.point_from_proportion(0.4) + UP).set_color(cor_elipse)
        
        # -------- Focos --------
        f1 = Dot(self.f1).set_color(cor_focos)
        f2 = Dot(self.f2).set_color(cor_focos)
        f1_label = MathTex("F_1").next_to(f1, UP*0.5).set_color(cor_focos)
        f2_label = MathTex("F_2").next_to(f2, UP*0.5).set_color(cor_focos)

        # -------- Função para pegar y do ponto --------
        f = lambda x: np.sqrt(self.b**2 * (1 - (x**2/self.a**2))) if (x**2/self.a**2) <= 1 and self.a != 0 else None
        x = 2
        y = f(x)

        # -------- Ponto pertencente a Elipse --------
        p = Dot((x, y, 0)).set_color(cor_ponto)
        p_label = MathTex("P_1").next_to(p, UP*0.5).set_color(cor_ponto)

        # -------- Distância focal (c) --------
        dist_c_1 = Line(self.f1, ORIGIN).shift(DOWN).set_color(cor_c)
        dist_c_2 = Line(ORIGIN, self.f2).shift(DOWN).set_color(cor_c)
        dist_c_1_label = MathTex("c").next_to(dist_c_1, UP*0.5).set_color(cor_c)
        dist_c_2_label = MathTex("c").next_to(dist_c_2, UP*0.5).set_color(cor_c)

        # -------- Semi-eixo maior (a) --------
        dist_a_1 = Line(elipse.point_from_proportion(0), ORIGIN).shift(self.b * DOWN).set_color(cor_a)
        dist_a_2 = Line(ORIGIN, elipse.point_from_proportion(0.5)).shift(self.b * DOWN).set_color(cor_a)
        dist_a_1_label = MathTex("a").next_to(dist_a_1, DOWN, 0.5).set_color(cor_a)
        dist_a_2_label = MathTex("a").next_to(dist_a_2, DOWN, 0.5).set_color(cor_a)

        # -------- Semi-eixo menor (b) --------

        dist_b_1 = Line(elipse.point_from_proportion(0.25), ORIGIN).shift(self.a * LEFT).set_color(cor_b)
        dist_b_2 = Line(ORIGIN, elipse.point_from_proportion(0.75)).shift(self.a * LEFT).set_color(cor_b)
        dist_b_1_label = MathTex("b").next_to(dist_b_1, LEFT, 0.5).set_color(cor_b)
        dist_b_2_label = MathTex("b").next_to(dist_b_2, LEFT, 0.5).set_color(cor_b)


        # -------- Segmento focal --------
        segmento_focal = Line(self.f1, self.f2).set_color(cor_segmento_focal)

        # -------- Agrupando objetos para manipulá-los juntos --------
        objetos = VGroup(
            eixos, elipse, elipse_label, f1, f2, f1_label, f2_label, 
            p, p_label, dist_c_1, 
            dist_c_2, dist_c_1_label, dist_c_2_label, 
            dist_a_1, dist_a_2, dist_a_1_label, dist_a_2_label,
            segmento_focal, dist_b_1, dist_b_2, dist_b_1_label, dist_b_2_label,
            eixos_labels)\
            .scale(escala_objetos).move_to(posicao_objetos)

        # -------- Agrupando objetos para manipulá-los separados --------
        self.eixos = objetos[0]
        self.elipse = objetos[1]
        self.elipse_label = objetos[2]
        self.f1 = objetos[3]
        self.f2 = objetos[4]
        self.f1_label = objetos[5]
        self.f2_label = objetos[6]
        self.p = objetos[7]
        self.p_label = objetos[8]
        self.dist_c_1 = objetos[9]
        self.dist_c_2 = objetos[10]
        self.dist_c_1_label = objetos[11]
        self.dist_c_2_label = objetos[12]
        self.dist_a_1 = objetos[13]
        self.dist_a_2 = objetos[14]
        self.dist_a_1_label = objetos[15]
        self.dist_a_2_label = objetos[16]
        self.segmento_focal = objetos[17]
        self.dist_b_1 = objetos[18]
        self.dist_b_2 = objetos[19]
        self.dist_b_1_label = objetos[20]
        self.dist_b_2_label = objetos[21]
        self.eixos_labels = objetos[22]

        self.focos = VGroup(self.f1_label, self.f2_label, self.f1, self.f2)
        self.distancia_focal = VGroup(self.dist_c_1, self.dist_c_2, self.dist_c_1_label, self.dist_c_2_label)
        self.eixo_maior = VGroup(self.dist_a_1, self.dist_a_2, self.dist_a_1_label, self.dist_a_2_label)
        self.eixo_menor = VGroup(self.dist_b_1, self.dist_b_2, self.dist_b_1_label, self.dist_b_2_label)

        # -------- Criando as definições --------
        definicoes = Tex(
            '$E$', ': elipse\n\n',
            '$P_1$', ': ponto\n\n',
            '$F_1, F_2$', ': focos\n\n',
            '$\\overline{F_1F_2}$', ': segmento focal\n\n',
            '$2c$', ': distância focal\n\n',
            '$2a$', ': eixo maior\n\n',
            '$2b$', ': eixo menor\n\n',
            tex_environment="flushleft"
        ).scale(escala_definicoes).move_to(posicao_definicoes)
        
        self.def_elipse = definicoes[0:2]
        self.def_ponto = definicoes[2:4]
        self.def_focos = definicoes[4:6]
        self.def_segmento_focal = definicoes[6:8]
        self.def_distancia_focal = definicoes[8:10]
        self.def_eixo_maior = definicoes[10:12]
        self.def_eixo_menor = definicoes[12:14]

        self.eq_elipse = MathTex('E = \{(x, y)\ /\ d(P_1, F_1) + d(P_1, F_2) = 2a\}').move_to(posicao_def_elipse).scale(escala_definicoes)
        self.eq_f1 = MathTex('F_1 = (-c, 0)').scale(escala_definicoes)
        self.eq_f2 = MathTex('F_2 = (c, 0)').scale(escala_definicoes)
        self.eq_ponto = MathTex(
            'P_1 = (x, y) \\in E \\rightarrow', 
            'd(P_1, F_1)', 
            '+', 
            'd(P_2, F_2)', 
            '= 2a'
        ).scale(escala_definicoes).move_to(1.5*RIGHT)

        self.eq_dist_1 = MathTex('d(P_1, F_1) = \\sqrt{(x - (-c))^2 + (y - 0)^2}').scale(escala_definicoes).move_to(RIGHT)
        self.eq_dist_2 = MathTex('d(P_1, F_2) = \\sqrt{(x - (c))^2 + (y - 0)^2}').scale(escala_definicoes).move_to(RIGHT)

        equations_positions = it.cycle([
            2.5 * RIGHT,
            2.5 * RIGHT + 0.7*DOWN, 
            2.5 * RIGHT + 1.4*DOWN,
            2.5 * RIGHT + 2.1*DOWN,
            2.5 * RIGHT + 2.8*DOWN,
        ])

        eqs_str = [
            'd(P_1, F_1) + d(P_2, F_2) = 2a',
            '\\sqrt{(x + c)^2 + y^2} + \\sqrt{(x - c)^2 + y^2} = 2a',
            '\\sqrt{(x + c)^2 + y^2} = 2a - \\sqrt{(x - c)^2 + y^2}',
            '(\\sqrt{(x + c)^2 + y^2})^2 = (2a - \\sqrt{(x - c)^2 + y^2}^2)',
            '(x + c)^2 + y^2 = 4a^2 - 4a\\sqrt{(x - c)^2 + y^2} + (x - c)^2 + y^2',
            '(x + c)^2 = 4a^2 - 4a\\sqrt{(x - c)^2 + y^2} + (x - c)^2',
            'x^2 + 2cx + c^2 = 4a^2 -4a\\sqrt{(x - c)^2 + y^2} + x^2 - 2cx + c^2',
            '2cx = 4a^2 - 4a \\sqrt{(x-c)^2 + y^2} - 2cx',
            '4a \\sqrt{(x-c)^2 + y^2} = 4a^2 - 2cx - 2cx',
            '4a \\sqrt{(x-c)^2 + y^2} = 4a^2 - 4cx',
            '{4a \\sqrt{(x-c)^2 + y^2} \\over 4} = {4a^2 - 4cx \\over 4}',
            'a \\sqrt{(x-c)^2 + y^2} = a^2 - cx',
            '(a \\sqrt{(x-c)^2 + y^2})^2 = (a^2 - cx)^2',
            'a^2 [(x-c)^2 + y^2] = a^4 - 2a^2 cx + c^2 x^2',
            'a^2 [x^2 - 2cx + c^2 + y^2] = a^4 - 2a^2cx + c^2x^2',
            'a^2 x^2 - 2a^2 cx + a^2 c^2 + a^2 y^2 = a^4 - 2a^2 cx + c^2 x^2',
            'a^2 x^2 + a^2 c^2 + a^2 y^2 = a^4 + c^2 x^2',
            'a^2 x^2 - c^2 x^2 + a^2 y^2 = a^4 - a^2 c^2',
            '(a^2 - c^2) x^2 + a^2 y^2 = a^2 (a^2 - c^2)',
            'b^2 \\equiv a^2 - c^2',
            'b^2 x^2 + a^2 y^2 = a^2 b^2',
            '{b^2 x^2 \\over a^2 b^2} + {a^2 y^2 \\over a^2 b^2} = {a^2 b^2 \\over a^2 b^2}',
            '{x^2 \\over a^2} + {y^2 \\over b^2} = 1'
        ]

        self.eqs = [
            MathTex(eq_str).scale(escala_definicoes).move_to(eq_pos)
            for eq_str, eq_pos in zip(eqs_str, equations_positions)
        ]

    def mostrar_definicoes_em_objetos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.eixos), Write(self.eixos_labels))

        play(Write(self.def_elipse))
        play(Transform(self.def_elipse[0].copy(), self.elipse_label))
        play(FadeIn(self.elipse))

        play(FadeIn(self.def_ponto))
        play(Transform(self.def_ponto[0].copy(), self.p_label))
        play(FadeIn(self.p))

        play(FadeIn(self.def_focos))
        play(Transform(self.def_focos[0].copy(), self.focos))
        
        play(FadeIn(self.def_segmento_focal))
        play(Transform(self.def_segmento_focal[0].copy(), self.segmento_focal))

        play(FadeIn(self.def_distancia_focal))
        play(Transform(self.def_distancia_focal[0].copy(), self.distancia_focal))

        play(FadeIn(self.def_eixo_maior))
        play(Transform(self.def_eixo_maior[0].copy(), self.eixo_maior))

        play(FadeIn(self.def_eixo_menor))
        play(Transform(self.def_eixo_menor[0].copy(), self.eixo_menor))

        play(
            self.def_elipse.animate.shift(2*UP+1.5*RIGHT),
            self.def_ponto.animate.shift(2*UP+1.5*RIGHT),
            self.def_focos.animate.shift(2*UP+1.5*RIGHT),
            self.def_segmento_focal.animate.shift(2*UP+1.5*RIGHT),
            self.def_distancia_focal.animate.shift(2*UP+1.5*RIGHT),
            self.def_eixo_maior.animate.shift(2*UP+1.5*RIGHT),
            self.def_eixo_menor.animate.shift(2*UP+1.5*RIGHT),
        )

        self.wait(1)

    def mostrar_definicoes(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        play(Write(self.eq_elipse))
        play(self.eq_elipse.animate.shift(3*UP + LEFT))
        play(Write(self.eq_f1))
        play(self.eq_f1.animate.shift(2.5*UP + 0.8*LEFT))
        play(Write(self.eq_f2))
        play(self.eq_f2.animate.shift(2.5*UP + 1.5*RIGHT))
        play(Write(self.eq_ponto))
        play(self.eq_ponto.animate.shift(2*UP + LEFT)) 
        play(Write(self.eq_dist_1))
        play(self.eq_dist_1.animate.shift(1.5*UP + 0.5*RIGHT))
        play(TransformMatchingShapes(self.eq_dist_1, MathTex('d(P_1, F_1) = \\sqrt{(x + c)^2 + y^2}').scale(0.6).move_to(self.eq_dist_1.get_center())))
        play(Write(self.eq_dist_2))
        play(self.eq_dist_2.animate.shift(1*UP + 0.5*RIGHT))
        play(TransformMatchingShapes(self.eq_dist_2, MathTex('d(P_1, F_2) = \\sqrt{(x - c)^2 + y^2}').scale(0.6).move_to(self.eq_dist_2.get_center())))
        play(TransformMatchingShapes(self.eq_ponto[1:5].copy(), self.eqs[0]))

        
            
    
    def manipulacao_algebrica(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        play(TransformMatchingShapes(self.eqs[0].copy(), self.eqs[1].move_to(2.5 * RIGHT + 0.6*DOWN)), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[1].copy(), self.eqs[2]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[2].copy(), self.eqs[3]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[3].copy(), self.eqs[4]), t=2)
        self.wait(2)
        play(FadeOut(self.eqs[0]))
        play(TransformMatchingShapes(self.eqs[4].copy(), self.eqs[5]), t=2)
        self.wait(2)
        
        play(FadeOut(
            self.eqs[1],
            self.eqs[2],
            self.eqs[3],
            self.eqs[4]
            ))

        self.wait(2)

        play(TransformMatchingShapes(self.eqs[5].copy(), self.eqs[6]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[6].copy(), self.eqs[7]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[7].copy(), self.eqs[8]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[8].copy(), self.eqs[9]), t=2)
        self.wait(2)
        play(FadeOut(self.eqs[5]))
        play(TransformMatchingShapes(self.eqs[9].copy(), self.eqs[10]), t=2)
        self.wait(2)

        play(FadeOut(
            self.eqs[6],
            self.eqs[7],
            self.eqs[8],
            self.eqs[9]
            ))

        self.wait(2)

        play(TransformMatchingShapes(self.eqs[10].copy(), self.eqs[11]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[11].copy(), self.eqs[12]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[12].copy(), self.eqs[13]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[13].copy(), self.eqs[14]), t=2)
        self.wait(2)
        play(FadeOut(self.eqs[10]))
        play(TransformMatchingShapes(self.eqs[14].copy(), self.eqs[15]), t=2)
        self.wait(2)

        play(FadeOut(
            self.eqs[11],
            self.eqs[12],
            self.eqs[13],
            self.eqs[14]
            ))

        self.wait(2)

        play(TransformMatchingShapes(self.eqs[15].copy(), self.eqs[16]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[16].copy(), self.eqs[17]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[17].copy(), self.eqs[18]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[18].copy(), self.eqs[19]), t=2)
        self.wait(2)
        play(FadeOut(self.eqs[15]))
        play(TransformMatchingShapes(self.eqs[19].copy(), self.eqs[20]), t=2)
        self.wait(2)

        play(FadeOut(
            self.eqs[16],
            self.eqs[17],
            self.eqs[18],
            self.eqs[19],
            ))

        self.wait(2)

        play(TransformMatchingShapes(self.eqs[20].copy(), self.eqs[21]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(self.eqs[21].copy(), self.eqs[22]), t=2)
        self.wait(2)
        play(FadeOut(self.eqs[20],self.eqs[21]))
        self.wait(2)
        play(Write(SurroundingRectangle(self.eqs[22])))

        play(FadeOut(*[mob for mob in self.mobjects]))

    def abertura(self):
        titulo = Tex('A Equação da Elipse').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)
        self.play(FadeIn(titulo))
        self.wait(1.5)
        self.play(FadeOut(titulo))
        self.wait()

    def fechamento(self):
        pibit = MathTex("\\text{PIBIT/CNPQ: 0220036212472856}").scale(1.5).move_to(2*UP).set_color(DARK_BLUE)
        autor = MathTex("\\text{Autor: Eric Satoshi Suzuki Kishimoto}").set_color("#dc6a40").move_to(ORIGIN)
        orientador = MathTex("\\text{Orientador: Prof. Vitor Rafael Coluci}").set_color("#dc6a40").move_to(DOWN)
        ft = ImageMobject("./logo-FT.jpeg").scale(0.4).shift(1.5*DOWN+3*RIGHT)
        unicamp = ImageMobject("./logo-unicamp.jpeg").scale(0.3).shift(1.5*DOWN+3*LEFT)

        self.play(FadeIn(pibit))
        self.wait(1)
        self.play(FadeIn(unicamp), FadeIn(ft))
        self.wait(1)
        self.play(FadeOut(unicamp), FadeOut(ft))
        self.wait(0.8)
        self.play(FadeIn(autor), FadeIn(orientador))
        self.wait(2)
        self.play(FadeOut(*[mob for mob in self.mobjects]))
        self.wait(2)



ARQ_NOME = Path(__file__).resolve()
CENA = DerivandoElipse.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')