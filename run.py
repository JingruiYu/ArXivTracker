import arxiv
import json
from datetime import datetime, timedelta

# 从本地config.json文件读取配置信息
with open("config.json", "r") as json_file:
    config = json.load(json_file)

# 提取配置信息
authors = config["authors"]
categories = config["categories"]
keywords = config["keywords"]
max_results = config["max_results"]
days_back = config["days_back"]

# 初始化API客户端
client = arxiv.Client()

# 按作者查询最新论文
print(f"Searching for latest papers by authors: {', '.join(authors)}")
for author in authors:
    search = arxiv.Search(
        query = f"au:{author}",
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    print(f"\nLatest {max_results} papers by {author}:")
    for i, result in enumerate(client.results(search), 1):
        print(f"{i}. {result.title}")
        print(f"URL: {result.entry_id}")
        print(f"Published: {result.published}")

# 按领域查询最新论文
print(f"\nSearching for latest papers in categories: {', '.join(categories)}")
for cat in categories:
    search = arxiv.Search(
        query = f"cat:{cat}",
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    print(f"\nLatest {max_results} papers in {cat}:")
    for i, result in enumerate(client.results(search), 1):
        print(f"{i}. {result.title}")
        print(f"URL: {result.entry_id}")
        print(f"Published: {result.published}")

# 按关键词查询最近一周的论文
print(f"\nSearching for papers in the last {days_back} days with keywords: {', '.join(keywords)}")
for keyword in keywords:
    search = arxiv.Search(
        query = f"all:{keyword}",
        max_results = float('inf'),
        sort_by = arxiv.SortCriterion.SubmittedDate,
        sort_order = arxiv.SortOrder.Descending
    )

    print(f"\nPapers with keyword '{keyword}' in the last {days_back} days:")

    results = [r for r in client.results(search) if r.published.date() >= datetime.today().date() - timedelta(days=days_back)]

    for i, result in enumerate(results, 1):
        print(f"{i}. {result.title}")
        print(f"URL: {result.entry_id}")
        print(f"Published: {result.published}")