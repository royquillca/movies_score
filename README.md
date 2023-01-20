# <h1 align=center style="color: #FF2403">Data Engineering - Movies Score - Proyecto Individual</h1>

<div align='center'>
    <img src='https://editor.analyticsvidhya.com/uploads/58713tvshows1.jpeg' alt='streaming services image' style="width:300px; height:150px;">
</div>

## Descripción del proyecto

Este proyecto se enfoca en el desarrollo de una API utilizando el framework FastAPI para comunicar y disponibilizar datos para el equipo de análisis de datos de una empresa. El objetivo principal es realizar transformaciones específicas en los datos y disponibilizarlos a través de endpoints accesibles mediante la API que finalmente debe ser desplegada en Deta.

[Ver más sobre el proyecto](https://github.com/royquillca/movies_score/blob/main/app/data_exploratory.ipynb)
## Evaluación del cumplimiento de lotivos

En resumidas líneas se han completado con los objetivos propuesto del Proyecto Individual, sin embargo, se ha obviado algunas de las transformaciones para que quede normalizado la base de datos que se va ha consumir mediante la API.
De forma específica, se ha completado los siguientes objetivos:

- [x] Transformaciones en las bases de datos: [Link](https://github.com/royquillca/movies_score/blob/main/app/transformations.ipynb)
- [x] Desarrollo de la API.
- [x] Deployment: [Link](https://0l6d6u.deta.dev/)
- [x] Video: [Link]()

## Requerimientos

1. Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
2. Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
3. De haber fechas, deberán tener el formato AAAA-mm-dd
4. Los campos de texto deberán estar en minúsculas, sin excepciones
5. El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

## Endpoints de la API

La API cuenta con los siguientes endpoints:

* Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.
  * Request 1: [get_word_count('netflix','love')](https://0l6d6u.deta.dev/get_word_count/netflix/love)

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
  * Request 2: [get_score_count('netflix',85,2010)](https://0l6d6u.deta.dev/get_score_count/netflix/85/2010)

* La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
  * Request 3: [get_second_score('amazon')](https://0l6d6u.deta.dev/get_second_score/amazon)

* Película que más duró según año, plataforma y tipo de duración
  * Request 4: [get_longest('netflix','min',2016)](https://0l6d6u.deta.dev/get_longest/netflix/min/2016)

* Cantidad de series y películas por rating
  * Request 5: [get_rating_count('18+')](https://0l6d6u.deta.dev/get_rating_count/18+)

## Deployment

Para realizar el deploy de esta aplicación se utilizó [Deta](https://www.deta.sh/) (no necesita dockerizacion) Sin embargo, también se puede usar [Railway](https://railway.app/) y [Render](https://render.com/)

**Requisitos previos:**

  * Servidor con sistema operativo Windows que tenga instalado PowerShell y/o Git Bash
  * Tener instalado ``Python`` (version mayor a 3.9) y ``pip 22.3.1``
  * Registrarse en [Deta](https://www.deta.sh/)

**Instrucciones detalladas:**

* Clonar el repositorio con ```git clone https://github.com/royquillca/movies_score/blob/main/app/data_exploratory.ipynb```
* Para replicar el despligue del proyecto es importante considerar que se han creado dos ambientes virtuales; una general en ``movies_score/`` y otra en ``deta_deploy/`` que esta contenida en la primera, por tanto no será raro que algunos archivos en el repositorio se repitan, es normal. La carpeta que contiene el proyecto a desplegar en Deta es ``deta_deploy`` por tanto usted debe acceder a dicha carpeta mediante la linea de comandos ``cd /ruta/hasta/el/proyecto/movies_score/data_deploy`` una vez clonada o descargada.
* Crear un ambiente virtual en la carpeta principal al mismo nivel de ``app/`` usando en comando ``python -m venv venv --upgrade-deps`` para que gestione un entorno de ambiente con las dependencias actualizadas (esencialmente de ``pip``)
* Activar el ambiente virtual creado con ``source venv/Scripts/activate`` o ``.\venv\Scripts\activate`` en Git Bash y Power Shell, respectivamente.
* Instalar las dependencias del proyecto mediante la ejecución de ``pip install -r requirements.txt`` y asegurarse que dicho archivo tenga el formato ``UTF-8`` (puede usar Visual Studio Code para verificar) para no tener problemas al momento de desplegar con el comando ``deta new``. Para mayor información revisar la [Documentación de Common Issues](https://docs.deta.sh/docs/common_issues/)
* Ejecutar el proyecto con el comando ``uvicorn main:app --reload`` y previamente habiendo isntalado uvicorn con ``pip install uvicorn`` para probar el proyecto en local accediendo al navegador en ``localhost:8000``
* Una vez funciona en local iniciamos con el despligue en [Deta](https://www.deta.sh/) para ello primero descargamos el CLI de Deta con: ``iwr https://get.deta.dev/cli.ps1 -useb | iex`` usando el PowerShell (si está en Git Bash escriba el comando ``powershell`` para acceder a la terminal de Power Shell).
*  Generalmente ocurre un problema al momento de ejecutar comandos de Deta en este paso, por tanto, si obtienes un error similar a:

```powershell
deta : El término 'deta' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable. Compruebe si escribió correctamente el nombre o, si incluyó una ruta de
acceso, compruebe que dicha ruta es correcta e inténtelo de nuevo.
En línea: 1 Carácter: 1
+ deta --help
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (deta:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```
Recomiendo agregar la ruta del archivo ``deta.exe`` al PATH de PowerShell ejecutando ``$env:Path += ";C:\Users\Roy Quillca Pacco\.deta\bin"``

* Iniciar sesión con la línea de comandos (CLI) de Deta ejecutando ``deta login`` en Power Shell.
* Desplegar la aplicación API ejecutando ``deta new`` y a través del log podrá observar un dictionario que contiene ``"endpoint": "https://0l6d6u.deta.dev/"`` (este es el mío el/la suy@ será diferente). Al acceder al link podrá ver su proyecto de API desarrollado en FastAPI desplegado en Deta. La interacción es lo mismo como `cuando ejecutamos en local con ``uvicorn``.
* Otro error que puede encontrarse al ejecutar ``deta new`` es similar a:
```bash
Error: failed to update dependencies: error on one or more dependencies, 
no dependencies were added, see output for details.
```
Asegúrate de que la codificación del archivo de ``requirements.txt`` sea ``UTF-8`` y revise el siguiente [link del issue](https://docs.deta.sh/docs/common_issues/).
* Para mayor detalle revise usted la documentación de Deta en [Documentación de despliegue de FastAPI en Deta](https://fastapi.tiangolo.com/deployment/deta/#__tabbed_1_2)
* Ya podrá realizar las consultas respectivas a la API usando Swagger UI.
## Contribuciones

Este proyecto es perfecto para desarrollar habilidades de Data Engineering, es de código abierto y está abierto a contribuciones y sugerencias. Si desea contribuir, por favor siga las siguientes instrucciones:

* Haga un fork del repositorio
* Cree una nueva rama con su característica o corrección
* Realice sus cambios y asegúrese de seguir las mejores prácticas de codificación y documentación
* Realice un pull request y espere la revisión y aprobación.
## Licencia

* Este proyecto está licenciado bajo la licencia MIT [MIT](https://opensource.org/licenses/MIT)

## Contacto

Si tiene alguna pregunta o comentario sobre este proyecto, no dude en ponerse en contacto a través de un mensaje directo a mi Linkedin [Roy Quillca](https://www.linkedin.com/in/royquillca/) o abriendo un issue en este repositorio.