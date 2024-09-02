import requests
import json
import os
from sys import stdout
from bs4 import BeautifulSoup

from models import ArticleData

class ArticleDataCollector:
    def __init__(self, sourceUrlWithPaging, outputPath = "C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/DatasetSrpski/ArticleData.json"):
        self.sourceUrlWithPaging = sourceUrlWithPaging
        self.outputPath = outputPath

    def get_article_urls_from_html(self, htmlPage: BeautifulSoup):
        return []
    
    def get_article_data_from_html(self, articleHtml: BeautifulSoup, sourceUrl: str):
        return None

    def __get_article_urls_from_all_pages(self, sourceUrlWithPaging: str):    
        print("Collecting urls for processing...")
        pageCountThreshold = 5000
        page = 1
        articleUrls = []
        while True:
            response = requests.get(sourceUrlWithPaging.format(page = page))
            if response.status_code != requests.codes.ok or page > pageCountThreshold:
                break
            responseHtml = BeautifulSoup(response.text, "html.parser")
            articleUrls.extend(self.get_article_urls_from_html(responseHtml))
            page += 1

        print(f"Found {len(articleUrls)} articles to process.")
        return articleUrls

    def __collect_article_data(self, articleUrl):
        response = requests.get(articleUrl)
        if (response.status_code != requests.codes.ok):
            return False, None
        responseHtml = BeautifulSoup(response.text, "html.parser")
        return self.get_article_data_from_html(responseHtml, articleUrl)

    def __dump_article_data(self, data: list[ArticleData], outputPath):
        
        with open(outputPath, "x") as file:
            json.dump(data, file)

    def __collect_and_dump_article_data(self, urlWithPaging: str, outputPath):
        if not self.__validate_output_path():
            return
        collectedData = []
        articleUrls = self.__get_article_urls_from_all_pages(urlWithPaging)
        urlCount = len(articleUrls)
        print(f"Processing {urlCount} urls:")
        for i, articleUrl in enumerate(articleUrls):
            stdout.write(f"{i+1}/{urlCount}      \r")
            stdout.flush();
            collectedData.append(self.__collect_article_data(articleUrl))
        print(f"Finished processing")
        self.__dump_article_data(collectedData, outputPath)

    def __validate_output_path(self):
        outputDir = os.path.dirname(self.outputPath)
        if not os.path.exists(outputDir):
            print(f"The folder {outputDir} not found.")
            return False
        if os.path.exists(self.outputPath):
            print("The file already exists. Please choose a different file name or path.")
            return False
        return True

    def execute(self):
        self.__collect_and_dump_article_data(self.sourceUrlWithPaging, self.outputPath)
        
