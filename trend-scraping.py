import scrapy

class TopTokens(scrapy.Spider):
  name = 'top40tokens'
  start_urls = ['https://beincrypto.com.br/converter']

  def parse(self, response):
    trend_tokens = response.css('p>strong::text').getall()

    for token in trend_tokens:
      name = 'id'
      yield {
        name: token,
      }

    next_page = response.xpath('//a[contains(@href, "/converter/2")]/@href').get()

    if next_page is not None:
      yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
