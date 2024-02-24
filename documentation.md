Notas para Jorge:

Mi web pretende facilitar la búsqueda de recetas, siendo el hecho de poder buscar por ingredientes y categorías lo que la hace diferente a otras webs de recetas. (A una persona celiaca y vegana no le interesa ver recetas de espaguetis a la boloñesa, por ejemplo).

Permite crear, borrar, editar tus propias recetas. Y guardar recetas en favoritos. (Y ver las recetas guardadas en favoritos, y las que hayas creado).
De momento no tiene funcionalidad de seguir a otros usuarios, o ver sus perfiles, pues no quiero convertirlo aún en red social, pero para un futuro me parece chulo y puede que un botón de compartir en twitter o algo así también.

Recipes es la app que contiene las recetas, la barra de búsqueda y funcionalidades relacionadas con las recetas.
La app de Recipes tiene como modelos las recetas, y las categorías. 

Los ingredientes no son un modelo porque no tienen una vista propia, sino que se muestran en la vista de la receta. 

Pese a poder duplicar datos, evito que estén creando objetos en la base de datos. 
(Y si alguien pusiera ingredientes con faltas ortográficas o diferentes nombres, como maíz y palta por ejemplo, no se estarían creando dos objetcos diferentes).
Así como tampoco se crean objetos de pasos, sino que se guardan en un campo de texto en la receta.

La funcionalidad de búsqueda está implementada con queryset y filter, y se puede buscar por nombre de receta, categoría, o ingredientes. (Los ingredientes los separos por comas y los busco en el campo de texto de la receta). 
(Llegué a usar Haystack y woosh como engine, pero tener que rebuildearlo era un problema, y no me parecía necesario para un proyecto de esta escala).

Las recetas también tienen relación con el usuario que las creó, y con los usuarios que las guardaron en favoritos.

En la app de usuarios tengo implementado un modelo de perfil que tiene relación con el usuario, y que contiene la foto de perfil, la biografía, y las recetas guardadas en favoritos.

Así como todo el proceso de autentificación y registro de usuarios.
Y los loginMixin y los decoradores para restringir el acceso a ciertas vistas a usuarios autenticados. (A sus perfiles).

Por último con el Django rest framework y los serializers, tengo implementada una API para las recetas.