import scrapy

class FashionSpider(scrapy.Spider):
    name = "fashion"
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static"]

    def parse(self, response):
        for product in response.css(".thumbnail"):
            yield {
                "name": product.css(".title::text").get(default="N/A"),
                "price": product.css(".price::text").get(default="N/A"),
                "description": product.css(".description::text").get(default="No description"),
                "image_url": product.css("img::attr(src)").get(default="No image"),
            }

