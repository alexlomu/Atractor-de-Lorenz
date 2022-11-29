# Atractor-de-Lorenz

El **atractor de Lorenz** es un concepto introducido por [Edward Lorenz](#edward-lorenz) en 1963. Se trata de un [sistema dinámico](#sistema-dinámico) determinista tridimensional no lineal derivado de las ecuaciones simplificadas de rollos de convección que se producen en las ecuaciones dinámicas de la atmósfera terrestre.
$$\frac{dx}{dt}=a(y-x)$$
$$\frac{dy}{dt}=x(b-z)-y$$
$$\frac{dz}{dt}=xy-cz$$

Para ciertos valores de los parámetros a, b, c, el sistema exhibe un comportamiento caótico y muestra lo que actualmente se llama un atractor extraño. El atractor extraño en este caso es un fractal de dimensión de Hausdorff entre 2 y 3. Grassberger (1983) ha estimado la dimensión de Hausdorff en 2,06 ± 0,01 y la dimensión de correlación en 2,05 ± 0,01.

![image_processing20210201-18089-lp24mi](https://user-images.githubusercontent.com/91721888/204562420-6c3fc705-4bf1-4479-b4bc-4e963e7b78a3.gif)



## Ewdard Lorenz

Edward Norton Lorenz (23 de mayo de 1917-16 de abril de 2008) fue un matemático y meteorólogo estadounidense, desarrolló ideas innovadoras sobre la rotación de los fluidos y realizó importantes contribuciones que ayudaron a comprender las dinámicas atmosféricas y las predicciones climatológicas. Fue pionero en el desarrollo de la teoría del caos. Fue quien introdujo el concepto de atractores extraños y acuñó el término [efecto mariposa](#Efecto-mariposa).
Edward estudió matemáticas en el Dartmouth College en Nuevo Hampshire y en la Universidad de Harvard en Cambridge, Massachusetts.
Su padre Edward Henry Lorenz nació en Hartford en 1882 asistió a Hartford High School y al Trinity College antes de obtener el grado en ingeniería mecánica en el Instituto de Tecnología de Massachusetts.
Obtuvo su doctorado en 1948 en el Instituto de Tecnología de Massachusetts , con un trabajo que describió la aplicación de ecuaciones dinámicas de fluidos para la predicción del movimiento de las tormentas donde después fue profesor por muchos años.

![edward](https://user-images.githubusercontent.com/91721507/204312784-95a302d2-0e7e-4284-b9e3-2f8b92e6cc3b.JPEG)

## Introducción

Antes de empezar, vamos a recordar que es un atractor.
 Un atractor es una singularidad en el espacio de acción donde ocurre un fenómeno, hacia el cual convergen las trayectorias de una dinámica, que encuentran en su atractor una condición local de mínima energía. La existencia de un atractor se puede detectar observando la disipación de algún tipo de energía. El atractor de un péndulo oscilando libremente es su punto más bajo, y es puntual. Además de atractores puntuales, existen atractores cíclicos - o ciclos límites - y atractores caóticos o atractores extraños - el conjunto límite de una trayectoria caótica.

El comportamiento del modelo de Lorenz se representa trazando sus variables en el espacio de fase. Es decir que para cada cálculo sucesivo de x, y, z, se traza el punto correspondiente en un espacio de ejes xyz. En un sistema lineal este trazado puede dibujar una trayectoria conducente a un único punto de estabilidad, o alternativamente puede dibujar un bucle cerrado que indica una variación periódica.

El atractor de Lorenz pertenece al conjunto de atractores desconocidos. Si bien no es una estructura geométrica sencilla, tampoco resulta ser una curva complicada. Se caracteriza porque nunca se intersecta a sí mismo ni repite la misma trayectoria. Proyectado en el plano xz, el atractor se parece a una mariposa; mientras que en el plano yz, se asemeja a una máscara de lechuza. La proyección en el plano xy resulta útil para percibir la tridimensionalidad de este atractor. 

Puntualmente, para estudiar este atractor, hemos empleado las siguientes ecuaciones:
dx/dt = -s x + s y
dy/dt = -x y + r x - y
dz/dt = x y - b z
donde s; b; y r son tres constantes que determinan el comportamiento del sistema.

## Propiedades del sistema de Lorenz
Como hemos explicado anteriormente, el atractor de Lorenz cumple las siguientes ecuaciones:
![2](https://user-images.githubusercontent.com/91721507/204572075-0c17c587-5393-4329-b15b-c5abfebe287e.PNG)

que denotaremos por SL. Reescribimos dicho sistema de la siguiente forma:
![1](https://user-images.githubusercontent.com/91721507/204571714-7d950ac6-5f70-439a-b639-bc2b7a24ba9d.PNG)

## Sistema dinámico

Un sistema dinámico es un sistema ( objeto complejo cuyas partes o componentes se relacionan con al menos alguno de los demás componentes, ya sea conceptual o material) cuyo estado evoluciona con el tiempo. Los sistemas físicos en situación no estacionaria son ejemplos de sistemas dinámicos, pero también existen modelos económicos, matemáticos y de otros tipos que son sistemas abstractos y, a su vez, sistemas dinámicos. El comportamiento en dicho estado se puede caracterizar determinando los límites del sistema, los elementos y sus relaciones; de esta forma se pueden elaborar modelos que buscan representar la estructura del mismo sistema.
¿Qué logramos al definir los límites de un sistema?
Al definir los límites del sistema se hace, en primer lugar, una selección de aquellos componentes que contribuyan a generar los modos de comportamiento, y luego se determina el espacio donde se llevará a cabo el estudio, omitiendo toda clase de aspectos irrelevantes.

## Efecto mariposa

«El aleteo de las alas de una mariposa se puede sentir al otro lado del mundo». Este proverbio chino es el origen, junto a las investigaciones del matemático y meteorólogo Edward Lorenz, de una de las más cinematográficas teorías físicas: el efecto mariposa. Según este concepto vinculado a la teoría del caos, el aleteo de un insecto en Hong Kong puede desatar una tempestad en Nueva York. Pero, ¿es posible que el aleteo de una mariposa en Sri-Lanka pueda provocar un huracán en EE.UU?

En un sistema no determinista, pequeños cambios pueden conducir a consecuencias totalmente divergentes. Una pequeña perturbación inicial, mediante un proceso de amplificación, puede generar un efecto considerable a medio y corto plazo. El movimiento desordenado de los astros, el desplazamiento del plancton en los mares, el retraso de los aviones, la sincronización de las neuronas; todos son sistemas caóticos o «dinámicos no lineales».

La teoría del caos y el efecto mariposa viene a explicar que algo tan complejo como el universo (un sistema caótico flexible) es impredecible. La teoría del caos explica sistemas como la atmósfera o las condiciones climatológicas que impiden realizar pronósticos del tiempo fiables más allá de tres días y es particularmente útil para abordar el estudio de los fenómenos sociales, difíciles de resolver en términos de relaciones lineales causa-efecto.

## Bibliografía
https://es.wikipedia.org/wiki/Atractor_de_Lorenz
https://es.wikipedia.org/wiki/Edward_Lorenz
https://www.nationalgeographic.es/ciencia/2017/11/el-efecto-mariposa#:~:text=%C2%ABEl%20aleteo%20de%20las%20alas,teor%C3%ADas%20f%C3%ADsicas%3A%20el%20efecto%20mariposa.
