import flet as ft


def main(pagina:ft.Page):
    pagina.title = "Calculadora - Simulador Juros"
    pagina.bgcolor = "#806D58"
    pagina.horizontal_alignment = "center"
    pagina.window.height = 800 #altura da janela
    pagina.window.width = 1000 # largura da janela

    titulo = ft.Text(value="Calculadora",
                     size = 40,
                     font_family = "Broadway",
                     color= "#462E01")

    titulo2 = ft.Text(value="Simulador de juros",
                         size = 30,
                         font_family = "Broadway",
                         color= "#462E01")

    historico = ft.Text(value="histórico de calculos",
                         size = 30,
                         font_family = "Elephant",
                         color= "#462E01",
                        )

    campo_capital = ft.TextField(label = "CAPITAL (R$)",
                               bgcolor = "#c2b3a5",
                               border_radius = 50,
                               border_color= "#6d5433",
                               border_width= 3,
                               value = "")

    campo_taxa = ft.TextField(label = "TAXA (%)",
                                   bgcolor = "#c2b3a5",
                                   border_radius = 50,
                                   border_color= "#6d5433",
                                   border_width= 3,
                                   value = "")

    campo_tempo = ft.TextField(label = "TEMPO (MESES)",
                                       bgcolor = "#c2b3a5",
                                       border_radius = 50,
                                       border_color= "#6d5433",
                                       border_width= 3,
                                       value = "")

    linha_valores = ft.Row(controls = [campo_capital,
                                      campo_taxa,
                                      campo_tempo],
                                      alignment = "center")

    lista_contas = []

    def simples():

        try:
            campo1 = int(campo_taxa.value)
            campo2 = int(campo_tempo.value)
            campo3 = int(campo_capital.value)

        except:
            pagina.show_dialog(ft.SnackBar("Digite um número"))
            return

        resultado = campo3 + campo3 * (campo1/100) * campo2                          
        lista_contas.append(ft.TextField(value=f"C:{campo3}| i: {campo1}| t: {campo2} | SIMPLES: {resultado}",
                                                bgcolor="#553922",
                                                color="#FFFFFF",
                                                border_radius=10,
                                                border_color= "#553922",
                                                width=500))

    def composto():
    
            try:
                campo1 = int(campo_taxa.value)
                campo2 = int(campo_tempo.value)
                campo3 = int(campo_capital.value)
    
            except:
                pagina.show_dialog(ft.SnackBar("Digite um número"))
                return
    
            resultado = campo3 * ((1+campo1/100) ** campo2)  
            resultado = round(resultado,2)
            lista_contas.append(ft.TextField(value=f"C:{campo3}| i: {campo1}| t: {campo2} | COMPOSTOS: {resultado}",
                                                    bgcolor="#553922",
                                                    color="#FFFFFF",
                                                    border_radius=10,
                                                    border_color= "#553922",
                                                     width=500))
            

    def excluir_historico():
        lista_contas.clear()

    botao_simples = ft.Button(content = "simples",
                      width= 200,
                      height= 45,
                        color= "#473b3b",
                        bgcolor= "#d4c7b8",
                        on_click=simples
                        )

    botao_composto = ft.Button(content = "composto",
                          width= 200,
                          height= 45,
                            color= "#473b3b",
                            bgcolor= "#d4c7b8",
                            on_click=composto
                            )

    botao_limpar = ft.Button(content = "limpar",
                              width= 400,
                              height= 45,
                                color= "#ffffff",
                                bgcolor= "#753838",
                                on_click=excluir_historico
                                )

    linha_botoes = ft.Row(controls = [botao_simples,
                                          botao_composto,],
                                          alignment = "center")

    container1 = ft.Container(content=ft.Column(controls=[linha_valores,
                                                            linha_botoes,
                                                            botao_limpar],
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                                       bgcolor= "#533B27",
                                       padding=30,
                                       border_radius = 30)

    container2 = ft.Container(content=ft.Column(controls=[historico,
                                                          ft.Column(controls=lista_contas,),],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                                        bgcolor= "#6E5641",
                                        padding=30,
                                        border_radius = 30,
                                        width=1000,
                                        height=390)

    

    


    pagina.controls = [titulo,
                       titulo2,
                       container1,
                       container2
                       ]



    pagina.update()
ft.run(main)