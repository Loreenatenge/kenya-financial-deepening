USE kenya_financial_deepening;

INSERT IGNORE INTO indicator_metadata (indicator_name, description, unit, source) VALUES
('inflation', 'Annual percent change in consumer prices', 'Annual percent change', 'World Bank WDI'),
('gdp_growth', 'Annual GDP growth rate', 'Annual percent change', 'World Bank WDI'),
('exchange_rate', 'KES per USD', 'KES per USD', 'World Bank WDI'),
('broad_money_gdp', 'Broad money as percent of GDP', 'Percent of GDP', 'World Bank WDI'),
('private_credit_gdp', 'Domestic credit to private sector as percent of GDP', 'Percent of GDP', 'World Bank WDI'),
('interest_rate_spread', 'Lending rate minus deposit rate', 'Percentage points', 'World Bank WDI'),
('external_debt_gni', 'External debt as percent of GNI', 'Percent of GNI', 'World Bank WDI'),
('debt_service_exports', 'Debt service as percent of exports', 'Percent of exports', 'World Bank WDI');