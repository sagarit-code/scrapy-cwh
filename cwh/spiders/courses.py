import scrapy

class CoursesSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["codewithharry.com/courses"]
    start_urls = ["https://www.codewithharry.com/courses"]

    def parse(self, response):
        all_course = response.css("div.bg-card")

        for each in all_course:
            link = each.css("a::attr(href)").get()
            title = each.css("a div.p-5 h2.text-xl::text").get()
            desc = each.css("a div.p-5 p.text-muted-foreground::text").get()

            yield {
                "link": response.urljoin(link),
                "title": title.strip() if title else None,
                "description": desc.strip() if desc else None,
            }

