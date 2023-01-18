import peewee
from decouple import config


HOST_MYSQL = config('HOST_MYSQL')
PORT_MYSQL = int(config('PORT_MYSQL'))
USER_MYSQL = config('USER_MYSQL')
PASSWORD_MYSQL = config('PASSWORD_MYSQL')
DB_MYSQL = config('DB_MYSQL')

database = peewee.MySQLDatabase(
    DB_MYSQL,
    host=HOST_MYSQL,
    port=PORT_MYSQL,
    user=USER_MYSQL,
    passwd= PASSWORD_MYSQL
)

class MoviesScores(peewee.Model):
    show_id = peewee.CharField()
    type = peewee.CharField(max_length=50)
    title = peewee.CharField(max_length=100)
    director = peewee.CharField(max_length=50)
    cast = peewee.CharField(max_length=300)
    country = peewee.CharField(max_length=100)
    date_added = peewee.CharField(max_length=200)
    release_year = peewee.IntegerField()
    rating = peewee.CharField(max_length=10)
    duration = peewee.CharField(max_length=50)
    duration_int = peewee.IntegerField()
    duration_type = peewee.CharField(max_length=10)
    listed_in = peewee.CharField(max_length=50)
    description = peewee.CharField(max_length=500)
    score = peewee.IntegerField()
    class Meta:
        database = database
        db_table = 'movies_scores'