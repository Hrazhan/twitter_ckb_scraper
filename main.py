import datetime
import os
import pathlib

path = pathlib.Path("./data/")
path.mkdir(parents=True, exist_ok=True)

since_date = str(datetime.datetime.today().date() - datetime.timedelta(days=1))
json_file = path/str(datetime.datetime.today().date())

def sns_scrape():
    os.system(f'snscrape --jsonl --progress --since {since_date} twitter-search "lang:ckb" > {json_file}.json')


if __name__ == "__main__":
    sns_scrape()
