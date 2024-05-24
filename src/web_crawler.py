import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random
import time

# Function to extract details from a video link
def web_crawler_():
    def get_video_details(video_url):
        res_video = requests.get(video_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        res_video.encoding = 'utf-8'
        soup_video = BeautifulSoup(res_video.text, 'html.parser')
        title = soup_video.find('title').text
        description = soup_video.find('meta', {'name': 'description'})['content']
        source = soup_video.find('span', class_='laiyuan').text
        time = soup_video.find('span', class_='time').text
        content = soup_video.find('div', id='content_area').text.strip()
        return f"标题: {title}\n描述: {description}\n来源: {source}\n时间: {time}\n内容: {content}"

    # Initialize DataFrame
    df = pd.DataFrame(columns=['Video Title', 'Video Link', 'Video Image', 'Video Duration', 'Details'])

    # Specify the date range
    start_date = datetime.strptime('20240312', '%Y%m%d') # 在这里更改收集开始日期
    end_date = datetime.strptime("20240318",'%Y%m%d') # 在这里更改收集结束日期

    # Iterate over each day in the date range
    while start_date <= end_date:
        date_str = start_date.strftime('%Y%m%d')
        url = f'https://tv.cctv.com/lm/xwlb/day/{date_str}.shtml'

        # Fetch HTML content with random delay
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.8 and 1.2 seconds
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        res.encoding = 'utf-8'
        html_code = res.text
        soup = BeautifulSoup(html_code, 'html.parser')

        # Temporary list to store data
        temp_data = []

        # Extract information from each video entry
        for li in soup.find_all('li'):
            a_tag = li.find('a', {'alt': True})
            if a_tag:
                video_title = a_tag.get('alt')
                video_link = li.find('a', {'href': True}).get('href')
                video_image = li.find('img').get('src')
                video_duration = li.find('span').text

                # Fetch video details with random delay
                time.sleep(random.uniform(0.8, 1.2))  # Random delay between 0.8 and 1.2 seconds
                details = get_video_details(video_link)

                # Append data to temporary list
                temp_data.append({'Video Title': video_title,
                                  'Video Link': video_link,
                                  'Video Image': video_image,
                                  'Video Duration': video_duration,
                                  'Details': details})

        # Concatenate temporary data to the DataFrame
        if temp_data:
            df = pd.concat([df, pd.DataFrame(temp_data)], ignore_index=True)

        # Save DataFrame to CSV
        df.to_csv(f'videos_{date_str}.csv', index=False)

        # Clear the DataFrame for the next iteration
        df = pd.DataFrame(columns=['Video Title', 'Video Link', 'Video Image', 'Video Duration', 'Details'])

        # Move to the next day
        start_date += timedelta(days=1)

if __name__ == "__main__":
    web_crawler_()