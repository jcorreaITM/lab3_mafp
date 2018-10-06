# Sistema de recomendaciones basico usando Pandas 

# La idea de este ejercicio practico es desarrollar un corto script que permite hacer una recomendacion de acuerdo a
# la calificacion y a la popularidad de una pelicula.

#En primer lugar cargue los datasets "ratings.csv" y "movies.csv" en dataframes

#Observe los dataframe, que columnas contienen, que datos son relevantes, hay alguna columna en comun entre ambos dataframe

#La recomendacion es de acuerdo a la popularidad y calificacion de las peliculas, sin embargo la calificacion y el nombre
#de la pelicula estan en dataframes distintos, entonces es necesario que combine los dataframe en uno solo, se puede 
#al aprovechar la existencia de una columna en comun (pista: merge)

#Es comun encontrar peliculas con altas calificaciones ('ratings'), pero no es prenda de garantia de que la pelicula sea
#popular, puede observarse que una pelicula con calificacion de 5 hecha por un solo usuario tiene or tanto una calificacion promedio de 5
#Obtenga y visualice la calificacion (rating) promedio de las peliculas del dataframe, agrupelas por titulo y organice los promedios
#en orden descendente

#Para medir la popularidad de una pelicula es necesario saber cuantos usuarios la han calificado, las peliculas mas populares son por lo general
#las que reciben mas calificaciones de parte de los usuarios. Agrupe las peliculas por titulo y obtenga en orden descendente el numero de calificaciones
#para cada pelicula del dataframe

#Ahora implemente un nuevo dataframe cuyas columnas sean la calificacion promedio de la pelicula 'promedio_rating' y la cantidad de calificaciones 'numero_califs'
#que recibio la pelicula. Utilice las operaciones que ya utilizo para medir esas mismos parametros

#Compruebe que estdisticamente las peliculas con mas calificaciones son tambien las peliculas con las mas altas calificaciones en promedio
#Tenga en mente una de las peliculas que se obtengan en este punto, preferiblemente la primera de la lista, con base en esta pelicula se va hacer
#la recomendacion (titulo de la pelicula)

#Implemente un nuevo dataframe donde el indice sea la columna 'userID' del dataframe, las columnas sean los titulos de las peliculas y los valores
#sean las calificaciones individuales de cada usuario a las peliculas (pista: pivot)

#Obtenga una lista con las calificaciones que los usuarios dieron a la pelicula mas popular (la que se tiene en mente luego de la comprobacion estadistica)

#Haga una nueva lista con la correlacion entre la lista anterior y el ultimo dataframe que se implemento, en esta instancia se va calcular la correlacion entre 
#todas las peliculas del dataframe y la pelicula mas popular y mejor calificada del dataframe (pista: corrwith)

#Implemente un nuevo dataframe con la ultima lista (la de las correlaciones) y a la columna llamela 'Correlaciones'
#Elimine de esta lista todos los valores NaN

#A este ultimo dataframe agreguele la columna del dataframe donde se registraron la cantidad de calificaciones por pelicula ('numero_califs') (pista: join)

#Visualice las recomendaciones como las peliculas con un numero de calificaciones mayores al percentil 60 del numero de calificaciones por pelicula ('numero_califs')
#y ordene el dataframe en orden descendente de la columna 'Correlaciones'




