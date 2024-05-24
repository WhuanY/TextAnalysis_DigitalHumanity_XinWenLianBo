# Text Analysis for digital humanity: XinWenLianBo

## Overview

The project aims to uncover insights into Chinese society's changes over time by analyzing the frequency of geographic names mentioned in the news program over a decade. This analysis seeks to interpret the importance of these cities in national politics, economics, or societal aspects.

## Objective

- Describe the clear structure of the project.
- Highlight the importance of tracking contributions and ensuring project integrity.

## Project File Structure

```
DigitalHumanity_XinWenLianBo/
│
├── README.md               # Project overview and setup instructions
├── LICENSE                 # The license file
│
├── src/                    # Source files
│   ├── web_crawler_.py             # Main application script
│   ├── module1.py          # Sample module
│   └── module2.py          # Another module
│
├── viz/                    # Files for visualizaiton effects
│   ├── *_news.html         # TF-IDF Results
│   └── barchartrace_exposure.gif    #Exposure Results
│   └── ProvinceExposure.html    
│
├── data/                   
│   ├── [videos_{yyyymmdd}.csv] 
│   └── ...                 # Data collected from crawler.py
│   └── [news_document-distribution.csv] 
│   └── ...                 # Data generated for TF-IDF Analysis
│   └── [news_document-top-topic-words.csv] 
│   └── ...                 # Data generated for TF-IDF Analysis
│   └── other documents     # Involve Other Documents for further studies
│   └── ... 
│
├── bar_chart_race/         # Dependency Package for drawing .gif
├── XWLB_news.ipynb         # Overall Project
├── requirements.txt        # Project dependencies
└── .gitignore              # Specifies intentionally untracked files to ignore
```

## Initialization

Here are the steps to set up this project locally:

1. Reorganize the file structure as necessary.
2. Ensure all dependencies are installed

## Understanding the code

### 1. Data Collection

The code defines a function `web_crawler_()` which uses a web scraping approach to collect data. This function iterates over a specified date range, constructing URLs for each day, fetching HTML content, and extracting details from video links found on the daily news pages. The extracted details include video title, description, source, time, and content. The data is temporarily stored in pandas DataFrames and saved as CSV files for each day.

As a reminder, the time phase for news data collections can be changed by modify the code accroding to your need.

### 2. Data Preprocessing

This section is intended to merge the individual daily CSV files into a single DataFrame, facilitating easier analysis. It also details steps to extract structured information from the "Detail" field in the data, which contains structured text describing video content. The intent is to use fuzzy matching to separate different components like description, source, time, and content into separate columns.

### 3. Analysis

The analysis would involve time series analysis of text data, possibly using techniques like word frequency analysis, topic modeling (LDA), and geographical data visualization (using tools like pyecharts for mapping).
## What can be done further

1. Graphical Viz Analysis for interactions between regions

2. Other themes alternations by time

## Acnowledgement

[1] Thanks for the original author for the WeChat Passage [哪个城市是中央眼中的心头爱？基于新闻联播文本的大数据分析](https://mp.weixin.qq.com/s/EvhdkXQBHZVYenYg1U74YQ) That makes the process for data collection easier and makes it possible for more exciting analysis.

[2] Thanks for Jindi Mo and Xuan Li for the explanation job for the code. Their contribution makes the project with potential impact.

## License and Additional Clause

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.

Use of this project in any form must also comply with the applicable laws and regulations of the People's Republic of China.