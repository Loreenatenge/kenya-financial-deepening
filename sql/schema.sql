CREATE DATABASE IF NOT EXISTS kenya_financial_deepening;

USE kenya_financial_deepening;

CREATE TABLE IF NOT EXISTS economic_indicators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    inflation DECIMAL(10,4),
    gdp_growth DECIMAL(10,4),
    exchange_rate DECIMAL(10,4),
    broad_money_gdp DECIMAL(10,4),
    private_credit_gdp DECIMAL(10,4),
    interest_rate_spread DECIMAL(10,4),
    external_debt_gni DECIMAL(10,4),
    debt_service_exports DECIMAL(10,4),
    UNIQUE KEY country_year (country, year)
);

CREATE TABLE IF NOT EXISTS indicator_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    indicator_name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(50),
    source VARCHAR(100),
    UNIQUE KEY indicator_name_unique (indicator_name)
);