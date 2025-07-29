
{{ config(materialized='view') }}

SELECT
    product_id,
    product_name,
    category,
    sub_category,
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_quantity,
    SUM(profit) AS total_profit
FROM {{ ref('superstore_raw') }}
GROUP BY product_id, product_name, category, sub_category
ORDER BY total_sales DESC
