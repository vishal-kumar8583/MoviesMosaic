A Django web application for discovering, reviewing, and organizing movies using the TMDB API. Users can search for movies, create playlists, write and save reviews, and manage their favorite films—all in one place.

Features :- 
User Authentication: Sign up, log in, and log out securely.
Movie Discovery: Browse popular and now-playing movies from TMDB, or search by title.
Playlists: Create and manage personal movie playlists.
Reviews: Write, submit, and save reviews for movies.
Save Reviews: Save your favorite reviews for quick access.
Responsive UI: User-friendly interface for seamless navigation.


Data Models :- 
UserProfile: Extends Django’s User model.
Movie: Stores movie details from TMDB.
Playlist: User-created playlists containing movies.
Review: User reviews for movies (one per user per movie).
SavedReview: Users can save reviews for later.
UserMoviePlaylist: Tracks which movies users have added to their playlists.

Getting Started :-

Prerequisites
Python 3.10+
pip

