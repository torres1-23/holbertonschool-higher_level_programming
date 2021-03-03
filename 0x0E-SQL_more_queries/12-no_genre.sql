-- Lists all shows contained in a database passed as argument wihtout a genre linked.
-- Display records by: tv_shows.title - tv_show_genres.genre_id.
-- Results order by tv_shows.title and tv_show_genres.genre_id ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
