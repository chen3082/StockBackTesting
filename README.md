# StockBackTesting
Select US top 2000 market cap company to perform backtesting (in progress)

## Requirements
yfinance==0.1.74
backtrader==1.9.76

## Download the data
### retrieve top 2000 market cap company by using web crawler

python3 top2000.py

## Execute MAP over top 2000 stock  to select best strategy

python3 map.py

## Sample Result

AAPL

[*********************100%***********************]  1 of 1 completed

Starting Portfolio Value: 100000.00

2021-12-31, (MA Period 10) Ending Value 365466.86

2021-12-31, (MA Period 20) Ending Value 819701.52

2021-12-31, (MA Period 60) Ending Value 406549.06

2021-12-31, (MA Period 120) Ending Value 611262.68

MSFT

[*********************100%***********************]  1 of 1 completed

Starting Portfolio Value: 100000.00

2021-12-31, (MA Period 10) Ending Value 94671.79

2021-12-31, (MA Period 20) Ending Value 137795.79

2021-12-31, (MA Period 60) Ending Value 226345.97

2021-12-31, (MA Period 120) Ending Value 356088.30

GOOG

[*********************100%***********************]  1 of 1 completed

Starting Portfolio Value: 100000.00

2021-12-31, (MA Period 10) Ending Value 139287.43

2021-12-31, (MA Period 20) Ending Value 256199.70

2021-12-31, (MA Period 60) Ending Value 355100.50

2021-12-31, (MA Period 120) Ending Value 309490.27

AMZN

[*********************100%***********************]  1 of 1 completed

Starting Portfolio Value: 100000.00

2021-12-31, (MA Period 10) Ending Value 393842.66

2021-12-31, (MA Period 20) Ending Value 459019.41

2021-12-31, (MA Period 60) Ending Value 339704.31

2021-12-31, (MA Period 120) Ending Value 340515.29




