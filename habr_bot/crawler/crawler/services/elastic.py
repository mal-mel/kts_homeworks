from datetime import datetime

import elasticsearch

from crawler.types import Article


class _ES:
    def __init__(self, host: str, port: int):
        self._es_connection = elasticsearch.AsyncElasticsearch([{
            "host": host,
            "port": port
        }])

    async def insert_record(self, index_name: str, data: dict) -> dict:
        return await self._es_connection.index(index_name, body=data)

    async def delete_record(self, index_name: str, record_id: str) -> dict:
        return await self._es_connection.delete(index=index_name, id=record_id)

    async def _create_index(self, index_name: str, index_settings: dict) -> dict or None:
        if not await self._es_connection.indices.exists(index_name):
            return await self._es_connection.indices.create(index_name, body=index_settings)

    async def _delete_index(self, index_name: str) -> dict:
        return await self._es_connection.indices.delete(index_name)

    async def _update_record(self, index_name: str, record_id: str, data: dict) -> dict:
        return await self._es_connection.update(index=index_name, id=record_id, body={"doc": data})

    async def _delete_by_query(self, index_name: str, delete_query: dict) -> dict:
        return await self._es_connection.delete_by_query(index=index_name, body=delete_query)

    async def _search(self, index_name: str, search_query: dict) -> dict:
        return await self._es_connection.search(index=index_name, body=search_query)


class ElasticInterface(_ES):
    def __init__(self, host: str, port: int, index: str):
        super().__init__(host, port)
        self.index = index

    async def insert_article(self, article: Article) -> dict:
        return await self.insert_record(self.index, {
            "add_date": datetime.now(),
            "content": article.content,
            "url": article.url
        })

    async def get_article(self, url: str) -> dict or None:
        response = (await self._search(self.index, {
            "query": {
                "term": {
                    "url": url
                }
            }
        }))["hits"]["hits"]
        if response:
            return response[0]

    async def is_article_exists(self, article: Article) -> bool:
        return bool(await self.get_article(article.url))
