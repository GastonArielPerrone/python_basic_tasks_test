💻 Ejercicios de repaso de Python (NIVEL - BÁSICO)

1. *️⃣ Características:
a) Cada archivo de Python (.py) contiene más de un ejercicio para realizar en modo de práctica.
b) Cada ejercicio se "engloba" en una función. Además pueden haber ejercicios donde se utilice
una función ya guardada en alguna variable del mismo archivo.
c) Es de código abierto para interesados, es decir, es PÚBLICO.
d) Cada ejercicio está testeado para ejecutar y mirar resultados en cuestión SI PASAN (pass)
o NO PASA (fail). Observar detalladamente el test que contienen feedback para cada función
(exceptuando a la que pasó - pass).

2. ✔️ Requisitos:
a) Python instalado (full extension).
b) VSCode.
c) Pytest (Para que corra el test): Instalación: pip install pytest

3. 💻 Modo de uso:

Para realizar los ejercicios debés ingresar a la carpeta "Tasks" y allí encontrarás cada
archivo .py con su nombre (tema en particular).

Para testear, fuera de la carpeta "Task" se encuentran los archivos de testing (NOTA: Es
SUMAMENTE IMPORTANTE NO MODIFICARLOS YA QUE DEBPENDE DEL DESAROLLO PARA QUE CADA ARCHIVO Y
EJERCICIO SEA TESTEADO DE FORMA CORRECTA) [test_tiposDeDatos.py por ejemplo].

Entonces veamos un ejemplo de su uso:

Supongamos que ingresamos a Task -> tiposDeDatos.py y realizamos un ejercicio (o todos).
Para testear este documento ingresaremos en la terminal el siguiente comando en el CLI:

pytest -v test_tiposDeDatos.py

Y allí nos dará el resultado:

❗ **IMPORTANTE** Cada archivo tiene su propio test con su nombre; pero lo que difiere es su
inicio con la palabra "test_"