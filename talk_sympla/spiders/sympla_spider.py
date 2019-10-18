import json

import scrapy

from talk_sympla.spiders import parsers
from talk_sympla.items import EventoItem


class SymplaSpyder(scrapy.Spider):
    name = 'sympla'

    def start_requests(self):
        urls = ['https://www.sympla.com.br/dev92__621492',]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        local = parsers.extrai_local(response)
        data = parsers.extrai_data(response)
        evento_item = EventoItem(local=local, data=data)
        evento_json = json.dumps(dict(evento_item))
        with open('evento.json', 'w') as f:
            f.write(evento_json)
