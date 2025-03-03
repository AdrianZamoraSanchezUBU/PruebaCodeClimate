// Archivo de prueba para Code Climate

function badFunction() {
    console.log("Esta función no está muy bien hecha...");
    for (let i = 0; i < 10; i++) {
        console.log("Número:", i); // Código duplicado
        console.log("Número:", i);
    }
    return 42;
}

var unusedVar = "Esto no es alcanzable";

badFunction();
