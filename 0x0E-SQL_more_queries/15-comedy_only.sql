-- List all comedy shows in a database passed as argument.
-- Display records by: tv_shows.title.
-- Order by tv_shows.title in ascending order.
SELECT tv_shows.title
    FROM tv_shows
    INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
