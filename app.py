from flask import Flask, render_template, request



app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def home():

    #Se o método for igual a POST, faça isso
    #Isso já liga a informação do html com o python

    if request.method == "POST":

        salario_bruto = float(request.form["salario_bruto"])

        if salario_bruto <= 1621 :
            inss = salario_bruto * 75/1000

        elif 1621 < salario_bruto < 2902 :
            faixa_1 = 1621 * 75/1000
            faixa_2 = (salario_bruto - 1621) * 9/100

            inss = faixa_1 + faixa_2

        elif 2902 < salario_bruto <= 4354 :
            faixa_1 = 1621 * 75/1000
            faixa_2 = (2902-1621) * 9/100
            faixa_3 = (salario_bruto - 2902) * 12/100

            inss = faixa_1 + faixa_2 + faixa_3

        elif 4354 < salario_bruto <= 8475 :
            faixa_1 = 1621 * 75/1000
            faixa_2 = (2902-1621) * 9/100
            faixa_3 = (4354-2902) * 12/100
            faixa_4 = (salario_bruto-4354) * 14/100

            inss = faixa_1 + faixa_2 + faixa_3 + faixa_4 

        inss = round(inss, 2)

        return render_template("index.html", salario_bruto=salario_bruto, inss=inss)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
