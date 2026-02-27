-- LISTS ALL SHOWS IN HBTN_0D_TVSHOWS THAT HAVE AT LEAST ONE GENRE LINKED
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
