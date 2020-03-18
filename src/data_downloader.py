import kaggle
import os


class Kaggle():
    def __init__(self):
        kaggle.api.authenticate()

    def search_dataset(self, keyword: str):
        dataset = kaggle.api.dataset_list(search=keyword)
        # List all dataset with keyword
        # print(dataset)
        return dataset

    def load_dataset(self, name: str, path='./data/'):
        kaggle.api.dataset_download_files(
            dataset=name, path=path, force=True, quiet=False, unzip=True)


if __name__ == '__main__':
    downloader = Kaggle()
    f = downloader.search_dataset("covid")
    # download covid19 cases report
    downloader.load_dataset("imdevskp/corona-virus-report")
