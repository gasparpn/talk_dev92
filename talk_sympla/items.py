import scrapy


class EventoItem(scrapy.Item):
    local = scrapy.Field()
    data = scrapy.Field()
    pass

