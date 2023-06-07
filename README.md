# Algorithmic-Trading-Simulation


This repository provides a Python implementation of the Bollinger Bands indicator trading strategy. The Bollinger Bands indicator is a popular technical analysis tool that helps identify overbought and oversold conditions in the financial markets.

## Overview

The Bollinger Bands indicator consists of three lines:

1. Middle Band (20-day Moving Average)
2. Upper Band (Middle Band + 2 standard deviations)
3. Lower Band (Middle Band - 2 standard deviations)

This trading strategy generates buy and sell signals based on the price crossing above or below the Bollinger Bands. When the price crosses above the upper band, it is considered overbought, and a sell signal is generated. Conversely, when the price crosses below the lower band, it is considered oversold, and a buy signal is generated.

## Features

- Calculation of the Bollinger Bands (Middle Band, Upper Band, Lower Band)
- Generation of buy and sell signals based on the Bollinger Bands
- Calculation of cumulative returns from the trading strategy
- Visualization of stock prices, Bollinger Bands, and trading signals

## Requirements

- Python 3.x
- pandas
- yfinance
- matplotlib

# Sample Output

![image](https://github.com/itsmekartikgupta/Algorithmic-Trading-Simulation/assets/80156877/a72f98da-97b0-4356-81d2-e90409f22c7a)

![image](https://github.com/itsmekartikgupta/Algorithmic-Trading-Simulation/assets/80156877/14658667-c2f1-4409-83a8-340728055737)



## Contributing

If you would like to contribute to the development of the Bollinger Bands indicator or have suggestions for improvement, feel free to submit a pull request or open an issue in the repository. Contributions and feedback are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

The implementation of the Bollinger Bands indicator is based on the original concept introduced by John Bollinger. Special thanks to John Bollinger for his contributions to technical analysis.


