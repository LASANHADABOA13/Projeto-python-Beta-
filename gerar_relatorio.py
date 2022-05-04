from fpdf import FPDF
import pandas as pd
import os
import matplotlib.pyplot as plt

pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()
pdf.set_font('times', '', 20)

estado = pd.read_excel('covid-19_estado.xlsx')
municipios = pd.read_excel('covid-19_municipios.xlsx')

mun_casos = municipios["Mun_Total de casos"]
mun_obitos = municipios["Mun_Total de óbitos"]
mun = municipios["Município"]
total_casos = estado["Total de casos"]
datas_casos = estado["Data"]
casos_dia = estado["Casos por dia"]
obitos_dia = estado["Óbitos por dia"]
municipios_casos = []
municipios_obitos = []
maior_caso = 0
maior_obito = 0
index_maior_caso = 0
index_maior_obito = 0
texth1 = "\n\n"

for x in range (len(list(mun_casos))):
    try:
        if int(list(mun_casos)[x])>maior_caso:
            maior_caso=int(list(mun_casos)[x])
            indice_maior_caso=x
    except:
        print(".")

    try:
        if int(list(mun_obitos)[x])>maior_obito:
            maior_obito=int(list(mun_obitos)[x])
            indice_maior_obito=x
    except:
        print(".")

for y in range (len(list(mun))):
    try:
        if int(list(municipios_casos)[y])==maior_caso:
            municipios_casos.append(list(mun)[y])
    except:
        print(".")

    try:
        if int(list(municipios_obitos)[y])==maior_obito:
            municipios_obitos.append(list(mun)[y])
    except:
        print(".")

texth1+="Municípios com maior registro de casos("+str(maior_caso)+"): "

for j in range (len(municipios_casos)):
    if (j+1)!=len(municipios_casos):
        texth1+=municipios_casos[j]+", "
    else:
        texth1+=municipios_casos[j]
    texth1+="\n\n"

texth1+="Municípios com o maior registro de obito("+str(maior_obito)+"): "

for l in range (len(municipios_obitos)):
    if (l+1)!=len(municipios_obitos):
        texth1+=municipios_obitos[l]+", "
    else:
        texth1+=municipios_obitos[l]
    texth1+="\n\n"
texto_problema = "Covid-19, O pior inimigo da educação. \n\n Sem sombra de duvidas que a pandemia afetou totalmente a educaçao no mundo enteiro. De acordo com os resultados do Sistema de Avaliação de Rendimento Escolar do Estado de São Paulo (Saresp), aproximadamente 96,6 dos estudantes terminaram a escola com o desempenho abaixo do adequado, isso apenas em matematica, na pratica, um estudante do 3° ano do ensino medio saiu da escola com o desempenho pouco parecido com um estudante da 7ª serie, uma defazagem realmente grande \n\n Bibliografia \n\n https://www.seade.gov.br/coronavirus/ \n https://g1.globo.com/"

plt.plot(datas_casos, total_casos)
plt.xlabel('Datas')
plt.ylabel('Total de casos')
plt.savefig("grafico1.png")
plt.close()

pdf.multi_cell(w=0, h=12, txt="Covid-19 x Educação", ln=2, align='C')
pdf.multi_cell(w=0, h=18, txt="Evolução da covid-19 em SP", ln=2, align='C')

pdf.image(x=20, y=40, w=180, h=80, name='grafico1.png')

plt.plot(datas_casos, casos_dia)
plt.xlabel('Datas')
plt.ylabel('Casos por dia')
plt.savefig("grafico2.png")
plt.close()

pdf.multi_cell(w=0, h=230, txt="Casos diários no estado de SP", ln=1, align='C')
pdf.image(x=20, y=160, w=180, h=80, name='grafico2.png')

plt.plot(datas_casos, obitos_dia)
plt.xlabel('Data')
plt.ylabel('total de obitos por dia')
plt.savefig("grafico3.png")
plt.close()

pdf.multi_cell(w=0, h=30, txt="Obitos diários no Estado de SP", ln=1, align='C')
pdf.image(x=20, y=50, w=200, h=80, name='grafico3.png')
pdf.add_page()
pdf.multi_cell(w=0, h=10, txt=texto_problema, ln=1, align='C')

pdf.output('Relatório.pdf')