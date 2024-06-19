from flask import Flask, render_template, request

from app import create_app,db

app =  create_app()
app.app_context().push()

# por ahora vamos a dejar la ruta principal en este archivo, pero a futuro
# tiene que quedar en otro archivo separado dentro de la carpeta resources
# lo hacemos asi para poder ir trabajando mientras tanto en el front end
@app.route('/') 
def inicio(): 
    return render_template('login.html')
# -------------------------------------------------------------------------
@app.route('/form', methods=['GET', 'POST'])
def loginForm():
    resultado ="Falso"
    if request.method == 'POST':
        usuario           = request.form['usuario']
        contraseña        = request.form['contraseña']
        if usuario == "admin" and contraseña=="1234":
            resultado = "Verdadero"
        
        # en la siguiente linea estaba devolviendo resultado para usar un "if" en el html
        # pero no es necesario porque estoy usando el if acá mismo o sea el "resultado=resultado"
        # return render_template('selectturno.html', resultado=resultado)
        # ahora para probar devuelvo "contador"
            # contador = leerdb()
            # print(leerdbturnos())
            contador=1234 #esto hay que sacarlo

            # return render_template('selectturno.html')
            return render_template('reservas.html', varcontador=contador)
        else:
            return render_template('login.html', msg = "Login Incorrecto")
    else:
        return render_template('login.html', msg = "Login Incorrecto")    



@app.route('/reservas')
def reservas():
    dia=23
    return render_template('reservas.html',dia=dia)

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port=5000) 
    print("hello world")
    