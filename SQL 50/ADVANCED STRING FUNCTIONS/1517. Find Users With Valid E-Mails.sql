SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'

--  Regular Expression Pattern
-- `^`: Asserts the start of the string.
-- `[a-zA-Z]`: Matches any uppercase or lowercase letter. This ensures that the email address starts with a letter.
-- `[a-zA-Z0-9_.-]*`: Matches zero or more occurrences of uppercase or lowercase letters, digits, underscores (`_`), dots (`.`), or hyphens (`-`). 
-- `@leetcode`: Matches the literal string `@leetcode`.
-- `\\.com`: Matches the literal string `.com`. The backslash (`\\`) is used to escape the dot. By escaping it, we specify that we want to match an actual dot.
-- `$`: Asserts the position at the end of the string.
