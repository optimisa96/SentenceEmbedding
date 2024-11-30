from Dataset.Models.ArticleData import ArticleData
import csv
import os

def store_article_data(article_data_list: list[ArticleData], output_path : str):
    if not __validate_path(output_path):
        raise Exception(f"Invalid output path: {output_path}");

    serializable_article_data = [article_data.to_dict() for article_data in article_data_list]
    with open(output_path, "a", encoding="utf-8") as csv_file:
        fieldnames = list(serializable_article_data[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames)
        if os.stat(output_path).st_size == 0:
            writer.writeheader()
        writer.writerows(serializable_article_data)

def load_article_data(path) -> list[ArticleData] :
    __validate_path(path)
    article_data = list[ArticleData]
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        article_data = [ArticleData.from_dict(entry) for entry in reader]
    return article_data

def __validate_path(output_path) -> bool:
    outputDir = os.path.dirname(output_path)
    if not os.path.exists(outputDir):
        print(f"The folder {outputDir} not found.")
        return False
    
    if not str.endswith(output_path, ".csv"):
        print("The output file extension should be .csv")
        return False

    return True