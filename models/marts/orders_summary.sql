SELECT
    order_id,
    order_date,
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(*) AS total_items,
    SUM(quantity) AS total_quantity
FROM {{ ref('superstore_raw') }}
GROUP BY order_id, order_date, region
ORDER BY order_date
