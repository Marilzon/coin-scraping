import scrapy

class TopTokens(scrapy.Spider):
  name = 'TopTokens'
  start_urls = ['https://beincrypto.com.br/converter']

  def parse(self, response):
    trend_tokens = response.css('p>strong::text').getall()

    for token in trend_tokens:
      yield {
        'name': token,
      }
