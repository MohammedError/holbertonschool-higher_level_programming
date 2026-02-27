-- Computes the score average of all records in the table second_table
SELECT score, AVG(score) AS average FROM second_table GROUP BY score;
