-- Select show titles and genre_id (will be NULL for shows without genres)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows

-- LEFT JOIN to include all shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Keep only shows that have no genre
WHERE tv_show_genres.genre_id IS NULL

-- Sort results by title, then by genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
