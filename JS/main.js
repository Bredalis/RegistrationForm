
var clave = document.getElementById("contraseña");

clave.addEventListener("focusin", () => {
	clave.type = "text";
});

clave.addEventListener("focusout", () => {
	clave.type = "password";
});