
from bs4 import BeautifulSoup, Tag
from Dataset.Models.ArticleData import ArticleData, ArticleCategory
from Dataset.Services.article_storage_management import store_article_data
import requests

def __get_html_element_textual_content(element: Tag) -> str:
    text_blocks = element.findAll(string=True, recursive=False)
    return ' '.join(str(text_block).strip() for text_block in text_blocks)
    
def __get_article_urls_from_html(html_page: BeautifulSoup):
    article_urls = []
    titles = html_page.body.find_all("h2", class_="news-item-title")
    for title in titles:
        article_urls.append(title.find("a")["href"])
    return article_urls

def __get_article_data_from_html(article_html: BeautifulSoup, source_url: str, category: str) -> ArticleData:
    article_content = article_html.find("div", class_="single-news-content")
    if article_content == None:
        return None
    heading = __get_html_element_textual_content(article_html.find("h1", class_="single-news-title"))
    summary = __get_html_element_textual_content(article_content.find("h5"))
    img_url = article_html.find("div", class_="single-news-header").find("img")["src"]
    text = summary
    for paragraph in article_content.find_all("p"):
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
        print(f"Found {len(article_urls)} articles on page {page}")
        collected_article_data.clear()
        for article_url in article_urls:
            article_html = __parse_html_from_url(article_url)
            article_data = __get_article_data_from_html(article_html, article_url, category)
            if (article_data != None):
                collected_article_data.append(article_data)
        print(f"Storing {len(collected_article_data)} article data...")
        store_article_data(collected_article_data, output_path)
        print(f"Successfully parsed and stored {len(collected_article_data)} articles from page {page}.")
        page += 1