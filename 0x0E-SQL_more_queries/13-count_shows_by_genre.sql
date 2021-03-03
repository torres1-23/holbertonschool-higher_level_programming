-- Lists all genres from a database passed as argument with number of shows linked.
-- Display records by: genre - number_of_shows.
-- Don't display genres without shows.
-- Order by number_of_shows in descending order.
SELECT tv_genres.name AS genre,
        COUNT(*) AS number_of_shows
    FROM tv_genres
    INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
