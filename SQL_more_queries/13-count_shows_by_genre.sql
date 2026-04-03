-- Select genre name and count of shows linked to it
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres

-- Join with tv_show_genres to link genres to shows
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

-- Group results by genre
GROUP BY tv_genres.name

-- Sort by number of shows in descending order
ORDER BY number_of_shows DESC;
