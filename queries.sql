-- 1. Count the number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- 2. Calculate the time period of the collected data in minutes
SELECT 
    (MAX(timestamp) - MIN(timestamp)) * 24 * 60 AS time_period_minutes
FROM transactions;

-- 3. Find the destination IP address with the highest number of transactions
SELECT destination_ip, COUNT(*) AS transaction_count
FROM transactions
GROUP BY destination_ip
ORDER BY transaction_count DESC
LIMIT 1;

-- 4. Find the destination IP and port combinations with the highest average session time
SELECT destination_ip, destination_port, AVG(session_time) AS average_session_time_minutes
FROM transactions
GROUP BY destination_ip, destination_port
ORDER BY average_session_time_minutes DESC
LIMIT 1;

-- 5. Find the busiest times of the day in terms of number of transactions (15-minute intervals)
SELECT 
    DATE_TRUNC('quarter_hour', timestamp) AS interval_start,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY interval_start
ORDER BY interval_start;