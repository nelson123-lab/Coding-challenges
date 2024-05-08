SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) as name FROM Users
ORDER BY user_id

-- Here we are extracting the first character of the string first and then converting that to upper case. 
-- LEFT is used to the extract just the first character.
-- Then we are extracting the character from the second charater to last to the substring and converting into lower case.
-- Finally concatinating it and order it by user_id
