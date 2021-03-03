-- Displays by: tv_shows.title - tv_show_genres.genre_id.
-- Order by tv_shows.title and tv_show_genres.genre_id ASC.
-- Display NULL if no genre for a show.
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
