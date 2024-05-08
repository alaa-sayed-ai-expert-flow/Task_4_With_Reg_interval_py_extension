import requests 
import pandas as pd
from bs4 import BeautifulSoup
from langchain.docstore.document import Document
import os
import asyncio
import time
import json
from datetime import datetime, timedelta

def getting_all_meta_tags(response):
    soup = BeautifulSoup(response, 'html.parser')

    meta_tags = soup.find_all('meta')
    metadata = {}
    for tag in meta_tags:
        if 'name' in tag.attrs:
            name = tag.attrs['name']
            content = tag.attrs.get('content')
            metadata[name] = content
            
        elif 'property' in tag.attrs:  # For OpenGraph metadata
            property = tag.attrs['property']
            content = tag.attrs.get('content')
            metadata[property] = content
            
    


def html_parser(data):
    # html_content = """\u003Cdiv id=\"cs-content\" class=\"cs-content\"\u003E\u003Cdiv class=\"x-section e139043-1 m2zab-0 m2zab-1 dimensions\"\u003E\u003Cdiv class=\"x-bg\"\u003E\u003Cdiv class=\"x-bg-layer-lower-img\"\u003E\u003Cimg src=\"https://www.expertflow.com/wp-content/uploads/Mask-group-4.png\" alt=\"customer self-service\" loading=\"lazy\" style=\"object-fit: cover; object-position: center;\"/\u003E\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-row x-container max width e139043-2 m2zab-5\"\u003E\u003Cdiv class=\"x-row-inner\"\u003E\u003Cdiv class=\"x-col e139043-3 m2zab-6\"\u003E\u003Ch1  class=\"h-custom-headline h1w h1\" \u003E\u003Cspan\u003EBusiness Analytics & Insights\u003C/span\u003E\u003C/h1\u003E\u003Cdiv id=\"\" class=\"x-text bannertextw\" style=\"\" \u003E\u003Cp\u003ESimplify reporting and drive more actionable Insights\u003C/p\u003E\n\u003C/div\u003E\u003Ca class=\"x-anchor x-anchor-button e139043-6 m2zab-7 m2zab-8\" tabindex=\"0\" href=\"https://www.expertflow.com/contact-us/\" rel=\"nofollow\"\u003E\u003Cdiv class=\"x-anchor-content\"\u003E\u003Cdiv class=\"x-anchor-text\"\u003E\u003Cspan class=\"x-anchor-text-primary\"\u003EGet in Touch\u003C/span\u003E\u003C/div\u003E\u003C/div\u003E\u003C/a\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-section e139043-7 m2zab-0 m2zab-2 m2zab-3\"\u003E\u003Cdiv class=\"x-container max width marginless-columns e139043-8 m2zab-a\"\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-9 m2zab-b feature_box_column leftTxtColPadding maxwidth_col_mobile\"\u003E\u003Cimg  class=\"x-img feature_box_image_mobile imgSmallScreen x-img-none\"  src=\"https://www.expertflow.com/wp-content/uploads/Group-481918-1.png\" \u003E\u003Ch3  class=\"h-custom-headline font-2023-h3 h3\" \u003E\u003Cspan\u003ELeverage valuable insights from your conversation data\n\u003C/span\u003E\u003C/h3\u003E\u003Cdiv id=\"\" class=\"x-text font-2023-text\" style=\"\" \u003E\u003Cp\u003E\u003Cspan style=\"font-weight: 400;\"\u003EWe give you the tools to leverage \u003C/span\u003E\u003Cspan style=\"font-weight: 400;\"\u003Ethe conversation data your customers provided or agents and AI engines collected during or after the conversation. Learn about your customers needs and preferences as well as your agents capabilities through:\u003C/span\u003E\u003C/p\u003E\n\u003Cul\u003E\n\u003Cli style=\"font-weight: 400;\" aria-level=\"1\"\u003E\u003Cspan style=\"font-weight: 400;\"\u003Eautomated call tagging/wrap up codes\u003C/span\u003E\u003C/li\u003E\n\u003Cli style=\"font-weight: 400;\" aria-level=\"1\"\u003E\u003Cspan style=\"font-weight: 400;\"\u003Esentiment analysis\u003C/span\u003E\u003C/li\u003E\n\u003Cli style=\"font-weight: 400;\" aria-level=\"1\"\u003E\u003Ca href=\"https://www.expertflow.com/customer-profiles/\"\u003E\u003Cspan style=\"font-weight: 400;\"\u003ECustomer Profile\u003C/span\u003E\u003C/a\u003E\u003C/li\u003E\n\u003Cli style=\"font-weight: 400;\" aria-level=\"1\"\u003E\u003Cspan style=\"font-weight: 400;\"\u003EAi generated transcripts/ summaries\u003C/span\u003E\u003C/li\u003E\n\u003Cli style=\"font-weight: 400;\" aria-level=\"1\"\u003E\u003Cspan style=\"font-weight: 400;\"\u003ECustomer Survey\u003C/span\u003E\u003C/li\u003E\n\u003Cli aria-level=\"1\"\u003Eand more...\u003C/li\u003E\n\u003C/ul\u003E\n\u003Cp\u003E\u003Cspan style=\"font-weight: 400;\"\u003EThe collected data can be used to search, filter or retrieve individual calls or can be aggregated for reporting purposes.\u003C/span\u003E\u003C/p\u003E\n\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-13 m2zab-b m2zab-c feature_box_column rightImgColPadding hide_col_mobile x-hide-md x-hide-sm x-hide-xs\"\u003E\u003Cimg  class=\"x-img feature_box_image imagezoom feature_box_img_video_right_margin x-img-none\" style=\"margin: 0px 40px 0px 0px ;\" src=\"https://www.expertflow.com/wp-content/uploads/Group-481774.png\" alt=\"ivr\"\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-section e139043-15 m2zab-0 m2zab-2 m2zab-4\"\u003E\u003Cdiv class=\"x-container max width marginless-columns e139043-16 m2zab-a\"\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-17 m2zab-b feature_box_column leftImgColPadding hide_col_mobile x-hide-md x-hide-sm x-hide-xs\"\u003E\u003Cimg  class=\"x-img feature_box_image imagezoom feature_box_img_video_left_margin x-img-none\" style=\"margin: 0px 40px 0px;\" src=\"https://www.expertflow.com/wp-content/uploads/Group-481750-1.png\" \u003E\u003C/div\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-19 m2zab-b m2zab-c feature_box_column rightTxtColPadding maxwidth_col_mobile\"\u003E\u003Cimg  class=\"x-img feature_box_image_mobile imgSmallScreen x-img-none\"  src=\"https://www.expertflow.com/wp-content/uploads/Group-481817-2.png\" \u003E\u003Ch3  class=\"h-custom-headline font-2023-h3 h3\" \u003E\u003Cspan\u003EAgent Guidance and Customer Satisfaction\u003C/span\u003E\u003C/h3\u003E\u003Cdiv id=\"\" class=\"x-text font-2023-text\" style=\"\" \u003E\u003Cp\u003E\u003Cspan style=\"font-weight: 400;\"\u003ERecorded calls can be reviewed by supervisors in order to score an agent’s performance. Post Collaboration Surveys and Sentiment analysis can contextualize a call recording or transcript.\u003C/span\u003E\u003C/p\u003E\n\u003Cp\u003E\u003Cspan style=\"font-weight: 400;\"\u003EThis data forms the basis for automated post-call processes using AI engines which can contribute valuable insights such as patterns, trends, and areas of strength or weakness.These insights help you refine your ongoing guidance,helping your agents improve their skills over time which can lead to improved customer service.\u003C/span\u003E\u003C/p\u003E\n\u003C/div\u003E\u003Ca class=\"x-anchor x-anchor-button e139043-23 m2zab-7 m2zab-9\" tabindex=\"0\" href=\"https://www.expertflow.com/contact-us/\" rel=\"nofollow\"\u003E\u003Cdiv class=\"x-anchor-content\"\u003E\u003Cdiv class=\"x-anchor-text\"\u003E\u003Cspan class=\"x-anchor-text-primary\"\u003ETalk to an expert\u003C/span\u003E\u003C/div\u003E\u003C/div\u003E\u003C/a\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-section e139043-24 m2zab-0 m2zab-2 m2zab-3\"\u003E\u003Cdiv class=\"x-container max width marginless-columns e139043-25 m2zab-a\"\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-26 m2zab-b feature_box_column leftTxtColPadding maxwidth_col_mobile\"\u003E\u003Cimg  class=\"x-img feature_box_image_mobile imgSmallScreen x-img-none\"  src=\"https://www.expertflow.com/wp-content/uploads/Group-481918-1.png\" \u003E\u003Ch3  class=\"h-custom-headline font-2023-h3 h3\" \u003E\u003Cspan\u003ECustomer Satisfaction\u003C/span\u003E\u003C/h3\u003E\u003Cdiv id=\"\" class=\"x-text font-2023-text\" style=\"\" \u003E\u003Cp\u003ELearn about yourself through your customers.\u003C/p\u003E\n\u003C/div\u003E\u003C/div\u003E\u003Cdiv class=\"x-column x-sm x-1-2 e139043-30 m2zab-b m2zab-c feature_box_column rightImgColPadding hide_col_mobile x-hide-md x-hide-sm x-hide-xs\"\u003E\u003Cimg  class=\"x-img feature_box_image imagezoom feature_box_img_video_right_margin x-img-none\" style=\"margin: 0px 40px 0px 0px ;\" src=\"https://www.expertflow.com/wp-content/uploads/Group-6881.png\" alt=\"ivr\"\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E"""
    html_content = data
    # Assuming your text is stored in a variable called `html_content`
    # print(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get all text content
    text = soup.get_text(separator='\n')
    
    # Print the cleaned text
    return text

def getting_all_span_tags(response):
    soup = BeautifulSoup(response, 'html.parser')

    span_tags = soup.find_all('span')
    #print(span_tags)


def save_docs_to_json(array: [Document], file_path:str)->None:

    with open(file_path, 'a+') as json_file:
        for doc in array:
            json_file.write(doc.json() + ',\n')
            

    
async def updating_datasets_w_reg_interval(page_number , post_number):
    after_parser = ''
    doc = []
    continue_in_event_loop = False
    
    pages_api_url = "http://expertflow.com/wp-json/wp/v2/pages?per_page=100&page="+str(page_number)
    posts_api_url = "http://expertflow.com/wp-json/wp/v2/posts?per_page=100&page="+str(post_number)
    
    pages_response = requests.get(pages_api_url)
    posts_response = requests.get(posts_api_url)
    
    pages_data = pages_response.json()
    posts_data = posts_response.json()

    
    
    # Implement Pages api updates
    if type(pages_data) != dict:
        continue_in_event_loop = True
        print("Page # "+str(page_number) + " has data ")
        pages_meta_data = getting_all_meta_tags(pages_response.text)
        pages_span_tags = getting_all_span_tags(pages_response.text)
        print("We've " + str(len(pages_data)) + " pages ")
        for page_data in range(len(pages_data)):
            after_parser = html_parser(pages_data[page_data].get('content')['rendered']).replace('None' , '')
            link = pages_data[page_data].get('link')
            title = pages_data[page_data].get('title')['rendered']
            doc.append(Document(page_content=after_parser, metadata={"source" : str(page_data)+" page_source " , "title": title , "link" : link , "page_number" : str(page_number)}))
    else:
        if continue_in_event_loop == False:
            print("Page # "+str(page_number) + " has " + str(pages_data['data']['status']) + " code " )
            print("Pages Api now has no data ...")      

    # Implementing Posts api updates
    if type(posts_data) != dict:
        continue_in_event_loop = True
        print("Post # "+str(post_number) + " has data ")
        posts_meta_data = getting_all_meta_tags(posts_response.text)    
        for data_post in range(len(posts_data)):
            after_parser = html_parser(posts_data[data_post].get('content')['rendered']).replace('None' , '')
            link = posts_data[data_post].get('link')
            title = posts_data[data_post].get('title')['rendered']
            doc.append(Document(page_content=after_parser, metadata={"source" : str(data_post) +" post_source " , "title": title , "link" : link , "post_number" : str(post_number)}))
        print("We've " + str(len(posts_data)) + " posts ")
    else:
        if continue_in_event_loop == False:
            print("Post # "+str(post_number) + " has " + str(posts_data['data']['status']) + " code ")
            print("Posts Api now has no data ...")

    if continue_in_event_loop == True:
        save_docs_to_json(doc , 'general_file_posts_pages.json')
        await updating_datasets_w_reg_interval(page_number + 1 , post_number + 1)
    


        
# Function to calculate the time until the next midnight
def seconds_until_midnight(hour , minute):
    tomorrow = datetime.now() + timedelta(1)
    midnight = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=hour, minute=minute, second=0)
    return (midnight - datetime.now()).total_seconds()


# Infinite loop to run the task every day at midnight
while True:
    filePath = "general_file_posts_pages.json"
    if(os.path.isfile(filePath)):
        os.remove(filePath)
        print("The File is Existed ... will be updated from ")

    print("Note : 0 = 12Am and 1 = 1Am therefore, 12 = 12pm")
    hour_for_update = input("Enter the hour for update : ")
    minute_for_update = input("Enter the minutes of update hour : ")
    # Get the number of seconds until midnight
    sleep_time = seconds_until_midnight(int(hour_for_update) , int(minute_for_update))
    # Perform the task
    asyncio.run(updating_datasets_w_reg_interval(1 , 1))
    print("Our Data Updated successfully ...")
    # Sleep until entered time
    time.sleep(sleep_time)
