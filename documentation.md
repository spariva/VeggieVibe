Notas para Jorge: Mucho texto pero te doy los puntos claves de mi código para que no te aburras.
## Intro
Mi web pretende facilitar la búsqueda de recetas, siendo el hecho de poder buscar por ingredientes y categorías lo que la hace diferente a otras webs de recetas. (A una persona celiaca y vegana no le interesa ver recetas de espaguetis a la boloñesa, por ejemplo).

Permite crear, borrar, editar tus propias recetas. Y guardar recetas en favoritos. (Y ver las recetas guardadas en favoritos, y las que hayas creado).
De momento no tiene funcionalidad de seguir a otros usuarios, o ver sus perfiles, pues no quiero convertirlo aún en red social, pero para un futuro me parece chulo y puede que un botón de compartir en twitter o algo así también.

## Modelos
Recipes es la app que contiene las recetas, la barra de búsqueda y funcionalidades relacionadas con las recetas.
La app de Recipes tiene como modelos las recetas, y las categorías. 

Los ingredientes no son un modelo porque no tienen una vista propia, sino que se muestran en la vista de la receta. 

Pese a poder duplicar datos, evito que estén creando objetos en la base de datos. 
(Y si alguien pusiera ingredientes con faltas ortográficas o diferentes nombres, como maíz y palta por ejemplo, no se estarían creando dos objetcos diferentes).
Así como tampoco se crean objetos de pasos, sino que se guardan en un campo de texto en la receta.

Luego profile es one to one con el user de Django, y aparte de que profile añade campos nuevos he hecho un par de decoradores para que al crear o editar users, se cree o edite también el profile asociado.


Las recetas también tienen relación con el usuario que las creó, y con los usuarios que las guardaron en favoritos.

En la app de usuarios tengo implementado un modelo de perfil que tiene relación con el usuario, y que contiene la foto de perfil, la biografía, y las recetas guardadas en favoritos.

Así como todo el proceso de autentificación y registro de usuarios.
Y los loginMixin y los decoradores para restringir el acceso a ciertas vistas a usuarios autenticados. (A sus perfiles).

## Búsqueda

La funcionalidad de búsqueda está implementada con queryset y filter, y se puede buscar por nombre de receta, categoría, o ingredientes. (Los ingredientes los separos por comas y los busco en el campo de texto de la receta). 
(Llegué a usar Haystack y woosh como engine, pero tener que rebuildearlo era un problema, y no me parecía necesario para un proyecto de esta escala).

Ha sido complicado que la búsqueda por ingredientes funcionara bien, pero al final he logrado que busque por exclusión, es decir que acumule en el queryset las recetas que cumplan todo, no solo algún filtro. Aparte, que da igual el orden, mayúsculas, tildes, etc. Lo único que en ingredientes pido separar por coma porque así hago el split().

## Paginación
La paginación ha sido fácil por usar una listView, pero al estar usando querysets por get, he tenido que añadir mucho código para lograr que si estás en "recetas veganas, celiacas con tomate y patata" y le das a la página 2, no te lleve a "?page=2" de todas las recetas sino a "recetas veganas, celiacas con tomate y patata&page=2". 

(Por eso el pop (para que al volver a pasar de página no salga "page3&page4 etc") y el geturl para meter el queryset y después el número de página. Anéccdota: copilot se inventó durante horas apps de django que no existen para lograr esto, y la etiqueta META no funcionaba no sé por qué). 

Tiene estilos de bootstrap, y se ve bien en móvil y en ordenador.

## Autentificación
Dos backends de autentificación, uno para el login normal, y otro para el login con el email. Mucho problema a veces, y definitivamente última vez que uso allauth para algo que no sea OAuth.
El navbar (base.html) cambia dependiendo de si el usuario está autenticado o no. Login signup y si está autenticado, logout y perfil.

Para que esto funcione, al registrar usuarios con mi createView, he tenido usar login antes, para que request.user exista y no de error en el template. Pero también he tenido que usar antes authenticate, para que el primer backend que respondiese bien fuese el que se guardase en la sesión. (Sino, al tener dos, django no sabía con cuál hacer login y explotaba).
Han sido muchas horas intentando no romper la base de datos según el método usado pero ahora ya todo está estable y cohesionado.

Y los redirects salen bien, y gracias al request.user del LoginMixinRequired, me permito tener una vista menos (la del login), y que su url de detalle no necesite de un id (que al final queda un poco feo user/3465123 por ejemplo).

## Bootstrap-django
He usado bootstrap para el diseño, y es 100% responsive, utilizando breakpoints y súperpoderes de front. 

## Views
He intentadoo usar siempre el código más "pitónico" posible, y más fiel a la filosofía de Django. Por ello he tirado por las vistas basadas en clases, y he optado por CRUD views en vez de vistas de función o una mezcla de forms.py con views.py. 
Lo malo es que no he podido usar por tanto gadgets como me hubiera gustado, así que he añadido lógica de más en las templates para poder modificar los formularios (la persona que hizo la documentación de Django no le gustarían mis templates...)

## API 
He implementado una API con Django Rest Framework, que permite ver todas las recetas, o ver una receta en concreto. 
También he generado la documentación de la API con Swagger, que es muy chulo y me ha gustado mucho.

## Varias Apps 
He dividido el proyecto en apps, y he intentado que cada app tenga una funcionalidad clara.
Users se encarga de la autentificación y el perfil de usuario, y Recipes de las recetas y la búsqueda. Ambas están relacionadas entre sí, y con el user de Django.


## Templates
Aparte de la típica lógica de extends e include, he añadido lógica para tener persistencia de datos en las búsquedas, y para que los formularios se vean bien en el front.
