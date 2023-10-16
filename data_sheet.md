# Datasheet Template

As far as you can, complete the model datasheet. If you have got the data from the internet, you may not have all the information you need, but make sure you include all the information you do have. 

## Motivation

- For what purpose was the dataset created? The dataset was created to build a machine learning model to accurately predict the direction of where the stock prices is heading.
  
- Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)? Who funded the creation of the dataset? Dataset are pulled directly from Yahoo! Finance API. Market data are downloaded from Yahoo! Finance’s API with the intention of personal usage only. Note that Yahoo, inc is not affiliated with this.
   •	License: Apache Software
   •	Author: Ran Aroussi
   •	https://pypi.org/project/yfinance/


 
## Composition

- What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? The dataset consists of TESLA (‘TSLA’) stock closing price. Dataset is obtained from external resources, Yahoo! Finance API.
  
- How many instances of each type are there? Consisting of up to 3347 and growing each trading day and features containing Open, High, Low, Close, Adjusted Close, Volume. There are also other data that could be imported as the dataset such as income statement, balance sheet, cash flow, news, and such. However, this model will be sticking with just the ‘Closing’ price for simplicity’s sake.  Also noting, due to the inherently stochastic nature of the data, dataset will be using 3 months, which contains the latest 64 instances.
  
- Is there any missing data? No missing information from the input features and no outliers are detected.
  
- Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor–patient confidentiality, data that includes the content of individuals’ non-public communications)? Dataset is not considered confidential as information are readily available to be downloaded. Dataset was made public and are not considered sensitive information that will cause discomfort / harm to anybody.

## Collection process

- How was the data acquired? Data are downloaded from Yahoo! Finance API (yfinance 0.2.31).
  
- If the data is a sample of a larger subset, what was the sampling strategy? Data is a subset of the original dataset, however, no sampling strategy was used.
  
- Over what time frame was the data collected? 3 months

## Preprocessing/cleaning/labelling

- Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section. Dataset are filtered to have the latest 3 months data and are normalized by a min/max scaling. No cleaning and labelling required.
  
- Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? "raw" data are not saved as newer data 
 
## Uses

- What other tasks could the dataset be used for? Dataset can also be used to identify potentially profitable company as other data that could be imported as the dataset such as income statement, balance sheet, cash flow, news, and such.
  
- Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms? As new data can always be downloaded, future uses will not be affected. Dataset are not susceptible to unfair treatment of individuals or groups. 
  
- Are there tasks for which the dataset should not be used? If so, please provide a description. Model is not intended to provide financial advice and trades made upon the model’s prediction are not liable to monetary loss/gain. User are advised to conduct their own due diligence when making trades. 

## Distribution

- How has the dataset already been distributed? As an open-source tool, dataset is free to download and use for educational or research purposes. 
  
- Is it subject to any copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? Dataset was made public. 

## Maintenance

- Who maintains the dataset? Maintenance is done by the Author Ran Aroussi. 

