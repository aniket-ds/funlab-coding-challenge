-- CTE to find log-on and log-off times along with their durations
WITH log_sessions AS (
    SELECT
        l1.times AS LOG_ON
        , MIN(l2.times) AS LOG_OFF
        , ROUND(TIMESTAMPDIFF(MINUTE, l1.times, MIN(l2.times))) AS DURATION
    FROM login_details l1
    JOIN login_details l2 ON l1.status = 'on' AND l2.status = 'off' AND l2.times > l1.times
    GROUP BY l1.times
    ORDER BY l1.times
),
-- CTE to rank log sessions by log-off times
ranked_log_sessions AS (
    SELECT 
        LOG_ON
        , LOG_OFF
        , DURATION
        , ROW_NUMBER() OVER(PARTITION BY LOG_OFF ORDER BY LOG_OFF) AS rnk
    FROM log_sessions
)
-- Filtering log sessions with the earliest log-off time
SELECT 
    LOG_ON
    , LOG_OFF
    , DURATION 
FROM ranked_log_sessions 
WHERE rnk = 1;
