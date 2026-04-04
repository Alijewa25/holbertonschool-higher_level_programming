-- Select all show titles and their genre_id (if exists)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows

-- LEFT JOIN to include shows without genres
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Sort by title, then by genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
