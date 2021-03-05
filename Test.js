// Uso de variables
Raton = "Mouse";
a = "Pickachu";
Edad = 50;

document.write(a + "<br></br>");
// Unir 2 o más variables
num = 15;
num2 = 15;
total = num / num2;

document.write(total + "<br></br>");

f = 4;
g = 7;
h = 3;
salario = f + g + h;
document.write(salario + "<br></br>");
// Conctenar
nombre = "Edgar";
Frase = "¿Quien es " + nombre + "?";
document.write(Frase + "<br></br>");

nombre = "Edgar";
Num3 = 2; 
Num4 = 3;
frase2 = Num3 + Num4;
document.write(frase2 + "<br></br>");

// RECIBIR DATOS PROMPT
respuesta = prompt("¿Quien eres?");
d1 = "Bienvenido " + respuesta + "<br></br>";
document.write(d1 + "<br></br>");
// OPERERAR DATOS PROMPT
ReDates = parseInt(prompt("Numero prra"))
sumaprompt = ReDates + 4;
document.write(sumaprompt + "<br></br>");

num_1 = parseInt(prompt("Primer numero para la suma"));

num_2 = parseInt(prompt("Segundo numero para la suma"));

answer = num_1 + num_2;

document.write(answer + "<br></br>");
// Condicional

prra = "perra";
if (prra == "perra") {
    document.write("Bien hecho prra" + "<br></br>")   
} else {
    document.write("De nuevo prra" + "<br></br>")
}

// EJERCICIOS

Pregunta1 = prompt("Cual es tu nombre");
Pregunta2 = parseInt(prompt("Cual es tu edad"));

respueta =  "Hola " + Pregunta1 + " de " + 
Pregunta2;

if (Pregunta2 >= 18) { 
    document.write(respueta + " Con que eres mayor de edad" + "<br></br>")
} else {
    document.write(respueta + " Que haces aqui bb" + "<br></br>")
}


Edgar = 15;
Pedro = Edgar + 7;
roberto1 = pedro - 2;
roberto2 = roberto1 * 2; 

document.write("Edgar: " + Edgar + "<br></br>");

document.write("Pedro: " + Pedro + "<br></br>");

document.write("Roberto: " + roberto2 + "<br></br>");