-- Select genre names linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres

-- Join with tv_show_genres to link genres and shows
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

-- Join with tv_shows to filter by show title
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id

-- Filter only the show "Dexter"
WHERE tv_shows.title = 'Dexter'

-- Sort results by genre name in ascending order
ORDER BY tv_genres.name ASC;
