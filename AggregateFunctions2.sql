SELECT title, score FROM hacker_news ORDER BY score DESC LIMIT 5;

SELECT SUM(score) FROM hacker_news;

SELECT SUM(score), user FROM hacker_news GROUP BY user HAVING SUM(score) > 200;

SELECT(309 + 304 + 282 + 517)/6366.0;

SELECT user, url, COUNT(url) FROM hacker_news WHERE url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' GROUP BY user;

SELECT CASE
  WHEN url LIKE '%github.com%' THEN 'Github'
  WHEN url LIKE '%medium.com%' THEN 'Medium'
  WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
  ELSE 'Other'
 END AS 'Source',
 COUNT(url)
FROM hacker_news
GROUP BY 1; 

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
  strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20; 

SELECT 
  strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1; 

SELECT 
  strftime('%H', timestamp),
  AVG(score)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC; 

SELECT 
  strftime('%H', timestamp),
  AVG(score),
  COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC; 

SELECT 
  strftime('%H', timestamp),
  ROUND(AVG(score)),
  COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC; 

SELECT 
  strftime('%H', timestamp) AS hour,
  ROUND(AVG(score)) AS avg_score,
  COUNT(*) AS num_stories
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC; 

SELECT 
  strftime('%H', timestamp) AS hour,
  ROUND(AVG(score)) AS avg_score,
  COUNT(*) AS num_stories
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC; 
