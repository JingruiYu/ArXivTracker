# ArXivTracker

ArXivTracker is a Python script that allows you to track and retrieve the latest papers from arXiv based on specific authors, categories, and keywords. It provides a convenient way to stay up-to-date with the latest research in your areas of interest.

## Features

- Search for the latest papers by specific authors
- Search for the latest papers in specific categories
- Search for papers published in the last 7 days containing specific keywords
- Retrieve paper details such as title, URL, published date, categories, and abstract
- Highlight paper titles in red for better visibility
- Customize search parameters using a configuration file

## Requirements

- Python 3.x
- `arxiv` library (can be installed via `pip install arxiv`)

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/JingruiYu/ArXivTracker.git
   ```

2. Install the required dependencies:

   ```
   pip install arxiv
   ```

3. Create a `config.json` file in the project directory with the following structure:

   ```json
   {
     "authors": ["Author1", "Author2"],
     "categories": ["cat1", "cat2"],
     "keywords": ["keyword1", "keyword2"],
     "max_results": 3,
     "days_back": 7
   }
   ```

   - `authors`: List of authors to search for
   - `categories`: List of arXiv categories to search in
   - `keywords`: List of keywords to search for
   - `max_results`: Maximum number of results to retrieve for each search
   - `days_back`: Number of days to look back for keyword search

4. Run the script:

   ```
   python arxiv_tracker.py
   ```

   The script will perform the searches based on the configured parameters and display the results in the console.

## Example Output

```
Searching for latest papers by authors: Author1, Author2

Latest 3 papers by Author1:
1. Paper Title 1
URL: http://arxiv.org/abs/1234.5678
Published: 2023-05-20 00:00:00+00:00
Categories: cat1, cat2
Abstract: This is the abstract of paper 1.
===
2. Paper Title 2
URL: http://arxiv.org/abs/2345.6789
Published: 2023-05-19 00:00:00+00:00
Categories: cat1
Abstract: This is the abstract of paper 2.
===

...
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache-2.0 license](LICENSE).