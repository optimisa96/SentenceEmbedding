from Dataset.Services.blic_specialized_scraper import collect_article_data_from_pages as collect_blic
from Dataset.Services.sportal_specialized_scraper import collect_article_data_from_pages as collect_sportal
from Dataset.Services.article_storage_management import load_article_data
from Dataset.Models.ArticleData import ArticleCategory, ArticleData
from collections import defaultdict

def read_dataset() -> list[ArticleData]:
    path = f"C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/Dataset_Srpski/Blic.csv"
    return load_article_data(path)

def print_dataset_stats():
    dataset = read_dataset()
    print(f"There are {len(dataset)} articles in the dataset.")
    sum_by_category = defaultdict(int)
    for entry in dataset:
        sum_by_category[entry.category] += 1
    print([(category, sum_by_category[category]) for category in sum_by_category])
    
def collect_dataset():
    # url_with_paging = "https://www.blic.rs/politika?strana={page}"
    # category = ArticleCategory.POLITICS
    # output_path = f"C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/Dataset_Srpski/Blic.csv"
    # collect_blic(url_with_paging, output_path, category)

    # url_with_paging = "https://www.blic.rs/kultura?strana={page}"
    # category = ArticleCategory.CULTURE
    # output_path = f"C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/Dataset_Srpski/Blic.csv"
    # collect_blic(url_with_paging, output_path, category)

    url_with_paging = "https://sportal.blic.rs/najnovije-vesti?page={page}"
    category = ArticleCategory.SPORT
    output_path = f"C:/Users/Nignite/Documents/Personal/Diplomski/Materijal/Dataset_Srpski/Blic.csv"
    collect_sportal(url_with_paging, output_path, category)
    