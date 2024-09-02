import os
from bs4 import BeautifulSoup, Tag

from models import ArticleData
from articleDataCollector import ArticleDataCollector

class BlicArticleDataCollector(ArticleDataCollector):
    def __init__(self, urlWithPaging, outputPath):
        super(BlicArticleDataCollector, self).__init__(urlWithPaging, outputPath)

    def __get_tag_textual_content(self, tag: Tag):
        return tag.get_text().strip()
        
    def get_article_urls_from_html(self, htmlPage: BeautifulSoup):
        articleUrls = []
        articles = htmlPage.body.find("div", class_="section__right").find("section", class_="news-box").find_all("article", class_="news",  recursive=False)
        for article in articles:
            articleUrls.append(article.find("div", class_="news__img").find("a")["href"])
        return articleUrls

    def get_article_data_from_html(self, articleHtml: BeautifulSoup, sourceUrl: str):
        articleHeader = articleHtml.find("header", "article__header")
        heading = self.__get_tag_textual_content(articleHeader.find("h1"))
        summary = self.__get_tag_textual_content(articleHeader.find("p"))
        text = summary
        for paragraph in articleHtml.find("div", "article__text").find_all("p"):
            text += f" {self.__get_tag_textual_content(paragraph)}"
        return ArticleData(sourceUrl, heading, summary, text)


urlWithPaging = "https://www.blic.rs/kultura?strana={page}"
outputPath = "C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/DatasetSrpski/Blic/Kultura.json"

BlicArticleDataCollector(urlWithPaging, outputPath).execute()