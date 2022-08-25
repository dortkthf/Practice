from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()

bong = {
    "id" : director.id,
    "name" : director.name,
    "debut" : director.debut,
    "country" : director.country
}
for i in bong:
    print(f'{i} : {bong[i]}')

genre = Genre.objects.get(title='드라마')

g_dic = {
    'id' : genre.id,
    'title' : genre.title
}

for i in g_dic:
    print(f'{i} : {g_dic[i]}')

for mov in movies:
    print(mov.director,mov.genre,mov.title,mov.opening_date,mov.running_time,mov.screening)

for mov in movies:
    print(mov.director.name,mov.genre,mov.title,mov.opening_date,mov.running_time,mov.screening)

for mov in movies:
    print(mov.director.name,mov.genre.title,mov.title,mov.opening_date,mov.running_time,mov.screening)

movies = Movie.objects.order_by('-opening_date')

movies = Movie.objects.order_by('opening_date')[0]
