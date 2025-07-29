
{{ config(materialized='view') }}

SELECT
    region,
    DATE_TRUNC('month', order_date::DATE) AS order_month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM {{ ref('superstore_raw') }}
GROUP BY region, order_month
ORDER BY region, order_month
