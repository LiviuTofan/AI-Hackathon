# Here I generate short company description anm IndustryField using AI, giving information from "about us" page to gpt, it generate description and save them in description.txt file in JSON format.

import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import json

# Function that returns URL of Last Added Company from file companyURL.txt
def read_url_from_file(file_path="companyURL.txt"):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.get("lastAddedCompany").get("website")

# Function that returns URL for "about us page"
def web_scraper(url, keywords, protocols):
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags in the body
            for a_tag in soup.body.find_all('a'):
                # Extract the text content and href attribute of the anchor tag
                text_content = a_tag.get_text()
                href_attribute = a_tag.get('href')

                # Check if href is not None, and if it has one from protocols, if not then add the href to URL, because sometimes it is all link http...., but sometimes it is continue of original link like .../content
                if href_attribute is not None:
                    if not any(protocol in href_attribute for protocol in protocols):
                        href_attribute = url + href_attribute

                # Convert both text content and keywords to lowercase for case-insensitive comparison
                text_content_lower = text_content.lower()
                keywords_lower = [keyword.lower() for keyword in keywords]

                # Check if any keyword is present, and return it's href
                if any(keyword in text_content_lower for keyword in keywords_lower):
                    return href_attribute
        else:
            return None

# Function that returns all text from "about us" page
def get_description(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        body_text = soup.body.get_text()

        return body_text
    else:
        return None

def generate_description(text):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": '''You are a good Company description writer. On given text from user, you generate a description from around 200 characters.
            Also based on given information you have to generate Company Industry. Here is an example of good Description and Industry:
            Description: Adidas, a premier global brand in sportswear and athletic footwear, renowned for its inventive designs and dedication to empowering individuals through the influence of sport.
            Industry: Sportswear and Athletic footwear.'''},
            {"role": "user", "content": "Generate Description and Industry for the company based on the given text." + text}
        ]
    )

    return completion.choices[0].message.content

#Function to return Industry from description
def divide_text(GPTtext):
    if 'Industry' in GPTtext:
        industry_index = GPTtext.find('Industry')
        industry = GPTtext[industry_index + len('Industry:'):].strip()
        description = GPTtext[13:industry_index].strip()
        return industry, description

