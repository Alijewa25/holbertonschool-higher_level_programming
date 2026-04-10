-- Select show title and corresponding genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows

-- Join with tv_show_genres to get linked genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- Only shows with at least one genre are included automatically by JOIN
-- Sort results by show title, then by genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
