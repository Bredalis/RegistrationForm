
var clave = document.getElementById("contraseña");

// Mostrar la contraseña
clave.addEventListener("focusin", () => {
	clave.type = "text";
});

// No mostrar la contraseña
clave.addEventListener("focusout", () => {
	clave.type = "password";
});