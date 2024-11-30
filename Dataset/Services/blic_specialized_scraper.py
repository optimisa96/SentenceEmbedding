from bs4 import BeautifulSoup, Tag

from Dataset.Models.ArticleData import ArticleData, ArticleCategory
from Dataset.Services.article_storage_management import store_article_data
import requests

def __get_html_element_textual_content(element: Tag) -> str:
    text_blocks = element.findAll(string=True, recursive=False)
    return ' '.join(str(text_block).strip() for text_block in text_blocks)
    
def __get_article_urls_from_html(html_page: BeautifulSoup):
    article_urls = []
    articles = html_page.body.find("div", class_="section__right").find("section", class_="news-box").find_all("article", class_="news",  recursive=False)
    for article in articles:
        article_urls.append(article.find("div", class_="news__img").find("a")["href"])
    return article_urls

def __get_article_data_from_html(article_html: BeautifulSoup, source_url: str, category: str) -> ArticleData:
    article_header = article_html.find("header", "article__header")
    heading = __get_html_element_textual_content(article_header.find("h1"))
    summary = __get_html_element_textual_content(article_header.find("p"))
    img_url = article_header.find("picture").find("img")["srcset"]
    text = summary
    for paragraph in article_html.find("div", "article__text").find_all("p"):
        text += f" {__get_html_element_textual_content(paragraph)}"
    return ArticleData(source_url, category, heading, summary, text, img_url)

def __parse_html_from_url(source_url) -> BeautifulSoup:
    response = requests.get(source_url)
    if response.status_code != requests.codes.ok:
        print(f"Failed to parse html from url {source_url}")
        return None
    return BeautifulSoup(response.text, "html.parser")

def collect_article_data_from_pages(source_url_with_paging, output_path, category: ArticleCategory):
    pageCountThreshold = 5000
    page = 1
    collected_article_data = []
    while True and page <= pageCountThreshold:
        print(f"Processing article page {page}...")
        responseHtml = __parse_html_from_url(source_url_with_paging.format(page = page))
        if responseHtml == None:
            print(f"Could not find page {page}. Stopping...")
            break
        article_urls = __get_article_urls_from_html(responseHtml)
        collected_article_data.clear()
        for article_url in article_urls:
            article_html = __parse_html_from_url(article_url)
            article_data = __get_article_data_from_html(article_html, article_url, category)
            if (article_data != None):
                collected_article_data.append(article_data)
        store_article_data(collected_article_data, output_path)
        print(f"Successfully parsed and stored {len(collected_article_data)} articles from page {page}.")
        page += 1
