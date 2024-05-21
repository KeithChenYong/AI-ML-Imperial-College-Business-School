# Stock Price Prediction (TSLA) using LSTM & hyperparameter tuning with Optuna
This project serves to fulfil the capstone project for <b>Professional Certificate in Machine Learning and Artificial Intelligence</b> by Imperial College Business School. 


## NON-TECHNICAL EXPLANATION OF YOUR PROJECT
Timing the market has always been a far-fetched idea. Markets are highly complex, and individual stock prices are influenced by a multitude of factors, including earnings, news, potential business prospects, speculation, macroeconomics, and more. However, since the late Jim Simons, founded Renaissance Technologies, a quantitative hedge fund, an avalanche of companies has begun to explore the question: Could a machine learning model accurately and consistently predict where prices are heading? 

The objective of this project is to create algorithms that predict the stock price of a specific company, giving users a data-driven perspective to optimize their trading decisions. This approach aims to increase our position in a company without adding new capital through buying and selling.


## DATA
This project will download market data from yahoo! finance (yfinance). This is a open souce library developed by Ran Aroussi which offers a threaded and Pythonic way to [download market data from Yahoo!Finance](https://pypi.org/project/yfinance/). 


## MODEL 
This project will utilize Recurrent Neural Network (RNNs) to predict the future from sequence of variable lengths. Due to the vanishing/exploding gradient problem from unrolling a large number of sequential, LSTM comes into play. As the project advances, we can explore more features that can help us accurately predicts the model prices to be more robust.

LSTM (Long Short-Term Memory) networks are commonly used for stock price prediction due to their ability to effectively capture and learn from sequential data. 

1. Handling Sequential Data: Stock prices are inherently sequential, which makes LSTMs an ideal algorithms for time series forcasting tasks such as stock price prediction.
2. Long-Term Dependencies: From the naming, LSTMs are capable of learning long-term dependencies in the data due to their unique architecture. The model includes a memory cell that can maintain information over long periods. Historical prices can influence future stock prices over extended periods.
3. Flexibility: LSTMs can be used to model both univariate time series (predicting future stock prices based solely on past stock prices) and multivariate time series (predicting stock prices based on multiple features (i.e. trading volume, financial indicators, macroeconomic and more). This flexibility allows LSTMs to capture complex relationships in the data and we will explore this in a more complex project.
4. Robustness: LSTMs are robust to noise and fluctuations in the data, which are common in stock prices. The ability to filter out noise and focus on significant patterns helps in making more accurate predictions.


## HYPERPARAMETER OPTIMIZATION
1.	Number of hidden dimensions - LSTM hyperparameter
2.	Number of layers - LSTM hyperparameter
3.	Dropout - LSTM hyperparameter
4.	Learning rate - ADAM optimizer
5.	Epochs - training loop
6.	Window - training data partition

Using Optuna to automate the search for hyperparameters (and other parameters) that generate the lowest MSE for our stock prediction, we set the number of trials to an extensive 100. The best hyperparameters found within these trials are:

{'hidden_dim': 270, 'num_layers': 2, 'dropout': 0.40157739382028523, 'learning_rate': 0.028986462884432136, 'epochs': 236, 'window': 6}

Using these optimized variables with the saved LSTM model, we obtained an optimal stock price prediction. Compared to the initial prediction, we observed that the algorithm's predictions are much sharper and fit the test data more accurately.


## RESULTS
Using LSTM with the initial hyperparameters/parameters, we obtained a reasonably accurate prediction of the test data on 'TSLA' stock. The image below shows the initial performance with an MSE loss of 0.0030.

{'hidden_dim': 128, 'num_layers': 2, 'dropout': 0.2, 'learning_rate': 0.01, 'epochs': 100, 'window': 10}

![image](https://github.com/KeithChenYong/AI-ML-Imperial-College-Business-School/assets/133010489/cbcb1cec-c56d-4240-befc-c28e770d8ff2)


By optimizing the hyperparameters/parameters to find the global minimum via Optuna, we achieved a more accurate prediction on the test data. Through the optimization trials, the best performing model was saved with weights and biases as 'best_model.pth' in the same folder as this 'README.md' file. Using the optimal variables and model, the image below shows the improvement with an MSE loss of 0.0013.

{'hidden_dim': 245, 'num_layers': 1, 'dropout': 0.30846183372287017, 'learning_rate': 0.047182207992924365, 'epochs': 264, 'window': 8}


Let's put our model to the test. The image below was generated before the market opening on May 22, 2024.



## CONTACT DETAILS
Email:     keith.chenyong@gmail.com <br>
LinkedIn:  linkedin.com/in/keithchenyong

## Citation
[Optuna](https://optuna.readthedocs.io/en/stable/index.html)
Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama. 2019.
Optuna: A Next-generation Hyperparameter Optimization Framework. In KDD.

[LSTM](https://medium.com/analytics-vidhya/lstms-explained-a-complete-technically-accurate-conceptual-guide-with-keras-2a650327e8f2)
[LSTM - Pytorch](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)
