import arxiv
import json
from datetime import datetime, timedelta

RED = '\033[91m'
END = '\033[0m'


def search_and_print_papers(query,
                            max_results,
                            sort_by,
                            sort_order=None,
                            days_back=None):
    search_kwargs = {
        "query": query,
        "max_results": max_results,
        "sort_by": sort_by
    }

    if sort_order is not None:
        search_kwargs["sort_order"] = sort_order

    search = arxiv.Search(**search_kwargs)

    try:
        results = list(client.results(search))
    except arxiv.UnexpectedEmptyPageError as e:
        print(f"Error: no result ...")
        return

    if days_back:
        results = [
            r for r in results
            if r.published.date() >= datetime.today().date() -
            timedelta(days=days_back)
        ]

    if not results:
        print("No papers found.")
    else:
        for i, result in enumerate(results, 1):
            print(f"{RED}{i}. {result.title}{END}")
            print(f"URL: {result.entry_id}")
            print(f"Published: {result.published}")
            print(f"Categories: {', '.join(result.categories)}")
            print(f"Abstract: {result.summary}")
            print("===")


with open("config.json", "r") as json_file:
    config = json.load(json_file)

authors = config["authors"]
categories = config["categories"]
keywords = config["keywords"]
max_results = config["max_results"]
days_back = config["days_back"]

client = arxiv.Client()

print(f"Searching for latest papers by authors: {', '.join(authors)}")
for author in authors:
    print(f"\nLatest {max_results} papers by {author}:")
    search_and_print_papers(f"au:{author}", max_results,
                            arxiv.SortCriterion.SubmittedDate)

print(f"\nSearching for latest papers in categories: {', '.join(categories)}")
for cat in categories:
    print(f"\nLatest {max_results} papers in {cat}:")
    search_and_print_papers(f"cat:{cat}", max_results,
                            arxiv.SortCriterion.SubmittedDate)

print(
    f"\nSearching for papers in the last {days_back} days with keywords: {', '.join(keywords)}"
)
for keyword in keywords:
    print(f"\nPapers with keyword '{keyword}' in the last {days_back} days:")
    search_and_print_papers(f"all:{keyword}", 17,
                            arxiv.SortCriterion.SubmittedDate,
                            arxiv.SortOrder.Descending, days_back)
