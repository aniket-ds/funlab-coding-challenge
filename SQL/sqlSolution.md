# SQL Query Documentation: Funab Web User Analytics

## Objective:
The objective of this SQL query is to analyze login sessions of a Funlab web user recorded in the `login_details` table. Each login session has a start time ('on' status) and an end time ('off' status). The goal is to determine the duration (in mins) of each login session.

## Database Schema:
The `login_details` table has the following schema:
- `times` (TIME): Stores the timestamp of login or logout events.
- `status` (VARCHAR): Indicates whether the session is 'on' (login) or 'off' (logout).

## Query Structure:
The [query](webUserAnalytics.sql) consists of two Common Table Expressions (CTEs) and a final SELECT statement.

### Common Table Expression 1: log_sessions
- Calculates the duration of each login session by finding the start time ('on') and end time ('off') for each session.

### Common Table Expression 2: ranked_log_sessions
- Ranks the login sessions based on their end times.

### Final SELECT Statement:
- Retrieves the login sessions with the earliest end times.

## Step-by-Step Execution:
1. **Common Table Expression 1: log_sessions**
   - **SELECT Statement:**
     - The `l1` and `l2` aliases are used to reference the `login_details` table twice to match each 'on' status with the next 'off' status.
     - The `TIMESTAMPDIFF` function calculates the difference in minutes between the start time (`l1.times`) and end time (`MIN(l2.times)`).
   - **GROUP BY Clause:**
     - Groups the results by the start time of each session (`l1.times`).

2. **Common Table Expression 2: ranked_log_sessions**
   - **SELECT Statement:**
     - Ranks the login sessions based on their end times (`LOG_OFF`) within each partition.
     - Uses the `ROW_NUMBER()` window function to assign a row number to each session.

3. **Final SELECT Statement:**
   - **SELECT Clause:**
     - Retrieves the start time of each session (`LOG_ON`), the end time of each session (`LOG_OFF`), and the duration of each session (`DURATION`).
   - **WHERE Clause:**
     - Filters the results to include only the login sessions with the earliest end times (`rnk = 1`).

## Explanation of Inbuilt Functions Used:
- **TIMESTAMPDIFF:**
  - Calculates the difference between two timestamps.
  - Used to calculate the duration of each login session in minutes.
- **ROW_NUMBER() OVER():**
  - Assigns a unique sequential integer to each row within a partition of a result set.
  - Used to rank login sessions based on their end times.

## Conclusion:
This SQL query provides insights into login session durations, allowing for analysis of user activity patterns and session management.