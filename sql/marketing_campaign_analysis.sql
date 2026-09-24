-- 1. Total Marketing Performance
SELECT
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue
FROM campaigns;


-- 2. Performance by Channel
SELECT
    channel,
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue
FROM campaigns
GROUP BY channel
ORDER BY total_revenue DESC;


-- 3. Performance by Campaign
SELECT
    campaign,
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue
FROM campaigns
GROUP BY campaign
ORDER BY total_revenue DESC;


-- 4. Monthly Performance
SELECT
    DATE_FORMAT(date, '%Y-%m') AS month,
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue
FROM campaigns
GROUP BY DATE_FORMAT(date, '%Y-%m')
ORDER BY month;


-- 5. Channel KPIs
SELECT
    channel,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue,
    ROUND(SUM(clicks) / SUM(impressions) * 100, 2) AS ctr,
    ROUND(SUM(conversions) / SUM(clicks) * 100, 2) AS conversion_rate,
    ROUND(SUM(spend) / SUM(clicks), 2) AS cpc,
    ROUND(SUM(spend) / SUM(conversions), 2) AS cpa,
    ROUND(SUM(revenue) / SUM(spend), 2) AS roas,
    ROUND((SUM(revenue) - SUM(spend)) / SUM(spend) * 100, 2) AS roi
FROM campaigns
GROUP BY channel
ORDER BY total_revenue DESC;


-- 6. Top Campaigns by ROAS
SELECT
    campaign,
    SUM(spend) AS total_spend,
    SUM(revenue) AS total_revenue,
    ROUND(SUM(revenue) / SUM(spend), 2) AS roas
FROM campaigns
GROUP BY campaign
ORDER BY roas DESC
LIMIT 10;


-- 7. Top Campaigns by Conversions
SELECT
    campaign,
    SUM(conversions) AS total_conversions,
    SUM(spend) AS total_spend,
    SUM(revenue) AS total_revenue,
    ROUND(SUM(spend) / SUM(conversions), 2) AS cpa
FROM campaigns
GROUP BY campaign
ORDER BY total_conversions DESC
LIMIT 10;


-- 8. Monthly ROAS
SELECT
    DATE_FORMAT(date, '%Y-%m') AS month,
    SUM(spend) AS total_spend,
    SUM(revenue) AS total_revenue,
    ROUND(SUM(revenue) / SUM(spend), 2) AS roas
FROM campaigns
GROUP BY DATE_FORMAT(date, '%Y-%m')
ORDER BY roas DESC;


-- 9. Campaign ROI
SELECT
    campaign,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        (SUM(revenue) - SUM(spend)) / SUM(spend) * 100,
        2
    ) AS roi
FROM campaigns
GROUP BY campaign
ORDER BY roi DESC;


-- 10. Channel ROI
SELECT
    channel,
    ROUND(SUM(spend), 2) AS total_spend,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(conversions), 0) AS total_conversions,
    ROUND(
        (SUM(revenue) - SUM(spend)) / SUM(spend) * 100,
        2
    ) AS roi
FROM campaigns
GROUP BY channel
ORDER BY roi DESC;


-- 11. Channel Cost Efficiency
SELECT
    channel,
    SUM(spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(spend) / SUM(conversions), 2) AS cpa,
    ROUND(SUM(revenue) / SUM(spend), 2) AS roas
FROM campaigns
GROUP BY channel
ORDER BY cpa ASC;