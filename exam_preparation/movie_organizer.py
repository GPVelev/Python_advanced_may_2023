def movie_organizer(*name_and_genre):
    organized = {}

    for movie,genre in name_and_genre:
        if genre not in organized:
            organized[genre] = []

        organized[genre].append(movie)

    sorted_result = sorted(organized.items(), key=lambda x: (-len(x[-1]), x[0]))

    result = ''
    for genre, movie in sorted_result:
        sorted_movies = sorted(movie)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
