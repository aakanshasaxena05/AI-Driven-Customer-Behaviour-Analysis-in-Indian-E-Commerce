-- All queries run by 02_sql_analysis.ipynb against table `customer_behavior`.
-- Format: each query starts with "-- name: <result_name>".

-- name: kpis
SELECT
    SUM(revenue_inr)                              AS total_revenue,
    SUM(purchased)                                AS total_orders,
    SUM(revenue_inr) / NULLIF(SUM(purchased), 0)  AS avg_order_value,
    AVG(purchased) * 100                          AS conversion_rate,
    AVG(cart_abandoned) * 100                     AS cart_abandoned_rate
FROM customer_behavior;

-- name: monthly_revenue
SELECT month, SUM(revenue_inr) AS revenue
FROM customer_behavior
WHERE month IS NOT NULL
GROUP BY month
ORDER BY month;

-- name: session_outcome
SELECT
    CASE
        WHEN purchased = 1 THEN 'Purchased'
        WHEN cart_abandoned = 1 THEN 'Cart Abandoned'
        ELSE 'No Purchase'
    END AS session_outcome,
    COUNT(*) AS total_sessions
FROM customer_behavior
GROUP BY session_outcome;

-- name: category_revenue
SELECT product_category, SUM(revenue_inr) AS revenue
FROM customer_behavior
GROUP BY product_category
ORDER BY revenue DESC;

-- name: state_revenue
SELECT state, SUM(revenue_inr) AS revenue
FROM customer_behavior
GROUP BY state
ORDER BY revenue DESC;

-- name: payment_analysis
SELECT
    payment_method,
    COUNT(*)          AS total_sessions,
    SUM(purchased)    AS total_purchases,
    SUM(revenue_inr)  AS revenue
FROM customer_behavior
GROUP BY payment_method
ORDER BY total_purchases DESC;

-- name: device_sessions
SELECT device_type, COUNT(*) AS total_sessions
FROM customer_behavior
GROUP BY device_type
ORDER BY total_sessions DESC;
