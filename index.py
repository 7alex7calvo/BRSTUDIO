from flask import Flask, render_template

web = Flask(__name__)

@web.route('/')
def home():
    return render_template('inicio.html')

@web.route('/Galeria')
def Galeria():
    return render_template('Galeria.html')

@web.route('/Galeria/Servicios')
def Servicios():
    return render_template('Servicios.html')

@web.route('/Galeria/Servicios/Quienes_Somos')
def Quienes_Somos():
    return render_template('Quienes_Somos.html')

@web.route('/Galeria/Servicios/Quienes_Somos/Contactanos')
def Contactanos():
    return render_template('Contactanos.html')

@web.route('/Galeria/Servicios/Quienes_Somos/Contactanos/Logo')
def Logo():
    return render_template('Logo.html')







if __name__ == '__main__':
    web.run(debug=True)