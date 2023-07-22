from django.db import models


class RatingCategory(models.TextChoices):
    Rated_G = "G"
    Rated_PG = "PG"
    Rated_PG_13 = "PG-13"
    Rated_R = "R"
    Rated_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=RatingCategory.choices, null=True, default=RatingCategory.Rated_G
        )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")

    orders = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="ordered_movies"
        )

    def __str__(self) -> str:
        return f"<Movie ({self.id}) - ({self.title})>"


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
        )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
        )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"<MovieOrder ({self.id}) - ({self.price})>"
