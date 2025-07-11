import requests
from django.shortcuts import render
from django.conf import settings
from ..models import Review
from ..utils import get_time_ago

TMDB_API_KEY = settings.TMDB_API_KEY


def movie_detail(request, movie_id):
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"

    movie_resp = requests.get(movie_url).json()
    credits_resp = requests.get(credits_url).json()

    director = next(
        (c["name"] for c in credits_resp.get("crew", []) if c["job"] == "Director"), ""
    )
    cast = [c["name"] for c in credits_resp.get("cast", [])[:5]]

    reviews_qs = Review.objects.filter(movie_id=movie_id).order_by("-created_at")
    for r in reviews_qs:
        r.time_ago = get_time_ago(r.created_at)

    context = {
        "movie": {
            "title": movie_resp.get("title"),
            "release_date": movie_resp.get("release_date"),
            "overview": movie_resp.get("overview"),
            "poster_url": (
                f"https://image.tmdb.org/t/p/w500{movie_resp['poster_path']}"
                if movie_resp.get("poster_path")
                else ""
            ),
            "director": director,
            "cast": cast,
            "rating": movie_resp.get("vote_average"),
            "genres_names": [g["name"] for g in movie_resp.get("genres", [])],
        },
        "reviews": reviews_qs,
        "movie_id": movie_id,
    }
    return render(request, "movie_detail.html", context)
