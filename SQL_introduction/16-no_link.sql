-- Lists all records of the table second_table of the database hbtn_0c_0
-- Don't list rows where the name column does not contain a value
-- Results display the score and the name (in this order)
-- Records are listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;