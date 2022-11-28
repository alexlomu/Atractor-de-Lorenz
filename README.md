# Atractor-de-Lorenz

El **atractor de Lorenz** es un concepto introducido por [Edward Lorenz](#edward-lorenz) en 1963. Se trata de un [sistema dinámico](#sistema-dinámico) determinista tridimensional no lineal derivado de las ecuaciones simplificadas de rollos de convección que se producen en las ecuaciones dinámicas de la atmósfera terrestre.

## Ewdard Lorenz

Edward Norton Lorenz (23 de mayo de 1917-16 de abril de 2008) fue un matemático y meteorólogo estadounidense, desarrolló ideas innovadoras sobre la rotación de los fluidos y realizó importantes contribuciones que ayudaron a comprender las dinámicas atmosféricas y las predicciones climatológicas. Fue pionero en el desarrollo de la teoría del caos. Fue quien introdujo el concepto de atractores extraños y acuñó el término efecto mariposa.
Edward estudió matemáticas en el Dartmouth College en Nuevo Hampshire y en la Universidad de Harvard en Cambridge, Massachusetts.
Su padre Edward Henry Lorenz nació en Hartford en 1882 asistió a Hartford High School y al Trinity College antes de obtener el grado en ingeniería mecánica en el Instituto de Tecnología de Massachusetts.
Obtuvo su doctorado en 1948 en el Instituto de Tecnología de Massachusetts , con un trabajo que describió la aplicación de ecuaciones dinámicas de fluidos para la predicción del movimiento de las tormentas donde después fue profesor por muchos años.

![edward](https://user-images.githubusercontent.com/91721507/204312784-95a302d2-0e7e-4284-b9e3-2f8b92e6cc3b.JPEG)

## Introducción

Antes de empezar, vamos a recordar que es un atractor.
 Es una singularidad en el espacio de acción donde ocurre un fenómeno, hacia el cual convergen las trayectorias de una dinámica, que encuentran en su atractor una condición local de mínima energía. La existencia de un atractor se puede detectar observando la disipación de algún tipo de energía. El atractor de un péndulo oscilando libremente es su punto más bajo, y es puntual. Además de atractores puntuales, existen atractores cíclicos - o ciclos límites - y atractores caóticos o atractores extraños - el conjunto límite de una trayectoria caótica.

El comportamiento del modelo de Lorenz se representa trazando sus variables en el espacio de fase. Es decir que para cada cálculo sucesivo de x, y, y z, se traza el punto correspondiente en un espacio de ejes xyz. En un sistema lineal este trazado puede dibujar una trayectoria conducente a un único punto de estabilidad, o alternativamente puede dibujar un bucle cerrado que indica una variación periódica.

El atractor de Lorenz pertenece al conjunto de atractores desconocidos. Si bien no es una estructura geométrica sencilla, tampoco resulta ser una curva complicada. Se caracteriza porque nunca se intersecta a sí mismo ni repite la misma trayectoria. Proyectado en el plano xz, el atractor se parece a una mariposa; mientras que en el plano yz, se asemeja a una máscara de lechuza. La proyección en el plano xy resulta útil para percibir la tridimensionalidad de este atractor. 

Puntualmente, para estudiar este atractor, hemos empleado las siguientes ecuaciones:
dx/dt = -s x + s y
dy/dt = -x y + r x - y
dz/dt = x y - b z
donde s; b; y r son tres constantes que determinan el comportamiento del sistema.

## Sistema dinámico

Un sistema dinámico es un sistema ( objeto complejo cuyas partes o componentes se relacionan con al menos alguno de los demás componentes, ya sea conceptual o material) cuyo estado evoluciona con el tiempo. Los sistemas físicos en situación no estacionaria son ejemplos de sistemas dinámicos, pero también existen modelos económicos, matemáticos y de otros tipos que son sistemas abstractos y, a su vez, sistemas dinámicos. El comportamiento en dicho estado se puede caracterizar determinando los límites del sistema, los elementos y sus relaciones; de esta forma se pueden elaborar modelos que buscan representar la estructura del mismo sistema.
¿Qué logramos al definir los límites de un sistema?
Al definir los límites del sistema se hace, en primer lugar, una selección de aquellos componentes que contribuyan a generar los modos de comportamiento, y luego se determina el espacio donde se llevará a cabo el estudio, omitiendo toda clase de aspectos irrelevantes.
