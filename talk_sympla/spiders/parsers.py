# funções de parser para o sympla
from scrapy.http import Response

def extrai_local(response: Response) -> str:
    local = response.css('div[class = "event-info-city"]::text').get()
    return local.strip()

def extrai_data(response: Response) -> str:
    data = response.xpath('//div[@class="event-info-calendar"]/text()').get()
    return data.strip()
