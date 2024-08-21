
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def formulario_inscripcion():

	app = Flask(__name__)

	# Conectar la bbdd
	cliente = MongoClient(os.getenv("CLAVE_MONGO"))
	app.db = cliente["FormularioInscripcion"]
	coleccion = app.db["Solicitante"]

	@app.route("/", methods = ["GET", "POST"])
	def index():

		if request.method == "POST":

		    # Obtener los datos del formulario
		    nombre = request.form.get("nombre")
		    nacimiento = request.form.get("nacimiento")
		    telefono = request.form.get("telefono")
		    correo = request.form.get("correo")
		    clave = request.form.get("clave")
		    tecnico = request.form.get("tecnico")

		    if nombre and nacimiento and telefono and correo and clave and tecnico:

			    coleccion.insert_one({
			    	"Nombre": nombre,
			    	"Nacimiento": nacimiento,
			    	"Telefono": telefono,
			    	"Email": correo,
			    	"Contraseña": clave,
			    	"Tecnico": tecnico
			    })

			    print("Se enviaron los datos! \U0001F642")

		return render_template("index.html")

	@app.errorhandler(404)
	def error_404(e):
		return render_template("404.html"), 404

	return app

if __name__ == "__main__":
	app = formulario_inscripcion()
	app.run()