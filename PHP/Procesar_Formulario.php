<?php

// Verificar si se enviaron datos mediante POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    
    // Obtener los datos del formulario
    $nombre = $_POST["nombre"];
    $nacimiento = $_POST["nacimiento"];
    $telefono = $_POST["telefono"];
    $correo = $_POST["correo"];
    $clave = $_POST["clave"];

    // Establecer conexión con la base de datos SQLite
    $conexion = new SQLite3("../Datos_Del_Formulario.db");

    // Verificar la conexión
    if (!$conexion) {
        die("Error al conectar a la base de datos: " . $conexion->lastErrorMsg());
    }

    // Insertar los datos en la tabla
    $insertQuery = "
        INSERT INTO Formulario(Nombre, Nacimiento, Telefono, Correo, Clave) 
        VALUES ("$nombre", "$nacimiento", "$telefono", "$correo", "$clave")";

    $resultado = $conexion->exec($insertQuery);

    if ($resultado) {
        echo "Datos insertados correctamente.";
    } else {
        echo "Error al insertar datos: " . $conexion->lastErrorMsg();
    }

    // Cerrar la conexión
    $conexion->close();
} else {
    echo "No se recibieron datos del formulario.";
}

?>