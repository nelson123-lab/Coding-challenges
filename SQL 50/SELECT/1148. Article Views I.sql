# Write your MySQL query statement below
select distinct author_id as id from views where author_id = viewer_id order by id

/* Here distinct authors are taken as duplicates were present. The authors with authors id and viewers id are selected id are ordered by authors_id */
