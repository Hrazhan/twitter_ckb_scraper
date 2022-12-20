# Twitter Central Kurdish Scraper

[![Twitter Central Kurdish Dataset](https://github.com/Hrazhan/twitter_ckb_scraper/actions/workflows/scrape.yml/badge.svg)](https://github.com/Hrazhan/twiiter_ckb_scraper/actions/workflows/scrape.yml)

This repository contains a set of scripts and configurations for scraping Central Kurdish tweets on a daily basis using Github Actions. Central Kurdish, also known as Sorani, is a Kurdish dialect spoken in Iraq and parts of Iran.

Dependencies:
- snscrape

# Running the scraping script

To run the script, simply execute the following command:
```bash
python main.py
````
The script will use the `snscrape` to search for tweets in Central Kurdish and save them to a json file in the `data` directory.

# Setting up daily scraping using Github Actions

1. Navigate to the .github/workflows directory in the repository.
2. Edit the scrape.yml file to specify the frequency of scraping (e.g., daily, hourly, etc.).
3. Commit and push the changes to your repository.

Github Actions will now run the `main.py` script at the specified frequency and commit the results to the repository.

# Further customization

The scrape.py script can be customized to scrape tweets with different search parameters or to perform additional processing on the scraped data. Simply edit the script and push the changes to your repository to apply the changes.
