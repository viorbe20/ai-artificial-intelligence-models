# Práctica Red Neuronal - Clasificación de Colores

## Descripción del Proyecto

Este proyecto implementa una interfaz web simple que utiliza una red neuronal para clasificar y mostrar información sobre el color seleccionado por el usuario.

## Funcionalidades

Actualización en tiempo real: La interfaz se actualiza en tiempo real mientras el usuario selecciona diferentes colores.

## Clasificación de Color: Utiliza una red neuronal para clasificar el color seleccionado en categorías predefinidas como "verde", "azul", "rojo", etc.

## Instalación

1. Clonar el Repositorio:

```bash
## Copy code
git clone https://github.com/TuUsuario/Practica-Red-Neuronal.git
cd Practica-Red-Neuronal
```

2. Abrir el Archivo HTML

Abre el archivo index.html en tu navegador favorito.

## Uso

Utiliza el control de selección de color para cambiar el fondo.

![color_picker](img/color_picker.jpeg)

1. Observa cómo la interfaz se actualiza y la red neuronal aplica el color seleccionado al h1.

![sample_1](img/sample_1.jpeg)

2. Un poco más abajo, otra red neuronal intentaré adivinar el color seleccionado y te indicará la probabilidad.

![sample_2](img/sample_2.jpeg)

## Configuración

El programa establece un evento que se activa cuando se ha cargado completamente el DOM (DOMContentLoaded). 

Aquí hay un desglose de lo que hace cada parte del código:

1. Inicialización de variables:

colorInput: Obtiene el elemento del DOM con el ID "color-input".
subtitleElement: Obtiene el elemento del DOM con el ID "subtitle".

2. Evento de cambio de color

colorInput.addEventListener('input', function () { ... }): Este evento se activa cada vez que el valor del color de entrada cambia. Dentro de esta función, se llama a dos funciones: update y classifyColor.
Redes neuronales:

3. Creacion de redes neuronales

network: Se inicia una nueva red neuronal con el nombre network.
classificatorNetwork: Se inicia otra red neuronal con el nombre classificatorNetwork.
Ambas redes neuronales se entrenan con conjuntos de datos específicos. network se entrena para determinar el color del texto en función del fondo, mientras que classificatorNetwork se entrena para clasificar colores en categorías específicas.
Función classifyColor:

4. Obtención de los valores RGB normalizados del color seleccionado.
La red neuronal classificatorNetwork se ejecuta con estos valores y el resultado se almacena en colorOutput.
Se utiliza Object.keys y reduce para encontrar el nombre del color con la probabilidad más alta.
Se establece el color del texto en subtitleElement para que coincida con el color del fondo.
Se actualiza el contenido de classificator con el nombre del color y la probabilidad.

5. Función update:
Se obtienen los valores RGB normalizados del color seleccionado.
La red neuronal network se ejecuta con estos valores y el resultado se almacena en colorOutput.
Dependiendo de la probabilidad de que el color del fondo sea oscuro o claro, se establece el color del texto del elemento con el ID "title" en blanco o negro.
En resumen, el código utiliza dos redes neuronales para realizar tareas específicas: una para determinar el color del texto según el fondo y otra para clasificar colores en categorías específicas. El evento de cambio de color activa estas funciones cuando el usuario selecciona un color.


## Discrepancias en la Clasificación de Colores

El ejercicio tiene fines académicos por lo que la red neuronal no es lo suficientemente compleja como para capturar todas las variaciones posibles de colores. Debido a esto, existen algunas anomalías en la clasificación de colores. Además, algunos colores pueden ser difíciles de distinguir y podrían estar cerca en el espacio de características RGB.

## Tecnologías Utilizadas

- HTML
- CSS
- JavaScript (biblioteca brain.js)

## Contribuciones

Siéntete libre de contribuir al proyecto. Puedes abrir un problema o enviar una solicitud de extracción con mejoras o correcciones.

## Autora

Virginia Ordoño Bernier