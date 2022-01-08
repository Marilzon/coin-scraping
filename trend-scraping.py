import scrapy

class TopTokens(scrapy.Spider):
  name = 'top40tokens'
  start_urls = ['https://beincrypto.com.br/converter']

  def parse(self, response):
    trend_tokens = response.css('p>strong::text').getall()
    number = 1
    for token in trend_tokens:
      yield {
        number: token,
      }
      number = number + 1
