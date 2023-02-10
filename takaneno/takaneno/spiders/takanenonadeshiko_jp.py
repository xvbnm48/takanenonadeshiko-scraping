import scrapy


class TakanenonadeshikoJpSpider(scrapy.Spider):
    name = "takanenospider"
    allowed_domains = ["takanenonadeshiko.jp"]
    start_urls = ["https://takanenonadeshiko.jp/members/"]

    def parse(self, response):
        members = response.css('.members__list li .members__profile')
        for member in members:
            photo = response.css('.members__list li a img').attrib['src']
            yield {
                'name': member.css('.members__profile .members__name::text').get(),
                'name EN': member.css('.members__profile .members__name--en::text').get(),
                'link-social': [member.css('.members__link li a.sns_twitter').attrib['href'], member.css('.members__link li a.sns_insta').attrib['href'], member.css('.members__link li a.sns_tiktok').attrib['href'], member.css('.members__link li a.sns_showroom').attrib['href']],
                'photo': photo,
            }
