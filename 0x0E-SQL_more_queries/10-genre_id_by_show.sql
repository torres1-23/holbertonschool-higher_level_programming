-- List all shows contained in a database passed as argument.
-- Show must have at leats one genre linked.
-- Display records in this way: tv_shows.title - tv_show_genres.genre_id
-- Order by tv_shows.title and tv_show_genres.genre_id in ASC.
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
