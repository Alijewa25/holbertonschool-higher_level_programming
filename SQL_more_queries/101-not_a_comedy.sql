-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title sorted in ascending order.
SELECT title
FROM tv_shows
WHERE title NOT IN (
    SELECT title
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;
