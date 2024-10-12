from typing import Dict
from apify_client import ApifyClient
from config import ins_api_config, default_apify_token
from protocol import InsContent


class InstagramScrape:

    def __init__(self,apify_token:str|None=None,api_config:Dict|None=None):
        if not apify_token:
            apify_token =default_apify_token
        if not api_config:
            api_config = ins_api_config

        self.apify_client = ApifyClient(token=apify_token)
        self.api_config = api_config

    def _make_request(self,actor_id:str,run_input:Dict):

        try:
            run = self.apify_client.actor(actor_id=actor_id).call(
                run_input=run_input
            )
            self.dataset = self.apify_client.dataset(dataset_id=run["defaultDatasetId"])
        except :
            pass


    def call(self) -> None:
        """
        定义好actor和run_input,用于跑apify instagram爬取任务
        """


    def __str__(self) -> str:
        item_list = self.dataset.list_items().items
        item = item_list[0]
        item = InsContent(**item)
        return f"此次爬取的账号为:{item.ownerUsername},第一条帖子的具体内容为:{item.dict()}"

    def write_to_local(self):

        item_list = self.dataset.list_items().items
        item_list = [InsContent(**item).dict() for item in item_list]
        file_name = f"{}"
        pass

    def upload_to_db(self):
        pass


if __name__ == "__main__":
    ins_scraper = InstagramScrape()
    ins_scraper.call()
    print(ins_scraper)
