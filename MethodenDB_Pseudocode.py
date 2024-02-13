Klasse App:
    Statische Variable appUser
    Instanzvariable appUser
    Instanzvariable title
    Instanzvariable release_date
    Instanzvariable wishlist
    Instanzvariable watched_movies

    Methode __init__(self, appU, title, release_date):
        Setze appUser auf appU
        Setze title auf title
        Setze release_date auf release_date
        Initialisiere wishlist als leere Liste
        Initialisiere watched_movies als leere Liste

    Methode rate_movie(self, movie, rating):
        Wenn movie in watched_movies:
            Gib aus: "Du hast {movie.title} bereits bewertet."
        Sonst:
            # Hier könnte die Logik zur Bewertung des Films implementiert werden
            # Zum Beispiel: movie.rating = rating
            Gib aus: f"Du hast {movie.title} mit {rating} Sternen bewertet."
            Füge movie zu watched_movies hinzu

    Methode create_wishlist(self, movies, filename="wishlist.json"):
        Setze wishlist auf movies
        Erstelle wishlist_data als Liste der Filme in der Wishlist mit den Attributen title und release_date
        Öffne die Datei mit dem angegebenen Dateinamen im Schreibmodus ('w')
        Schreibe wishlist_data in die Datei als JSON mit Einrückung von 2 Zeichen
        Schließe die Datei

    Methode notify_wishlist(self):
        Für jeden Film in wishlist:
            Wenn der Film nicht in watched_movies ist:
                Gib aus: f"Benachrichtigung: {movie.title} ist verfügbar! Schau ihn dir an."

    Methode search_movie(self, title):
        Für jeden Film in wishlist:
            Wenn der Titel des Films in Kleinbuchstaben gleich dem gesuchten Titel in Kleinbuchstaben ist:
                Gib den Film zurück
        Gib aus: f"Film mit dem Titel {title} nicht gefunden."
        Gib None zurück
