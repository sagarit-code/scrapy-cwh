

This is a small Scrapy project I built to scrape all courses from CodeWithHarry.
The spider crawls the main courses page and extracts:

* Course title
* Course link
* Course description

All scraped data is saved into data.json.

Tech Stack

Python
Scrapy
Virtual Environment (venv)

How to Run

bash
scrapy crawl cwhspider -o data.json

Output Example
json
[
  {
    "link": "https://www.codewithharry.com/courses/the-ultimate-web-dev-course",
    "title": "[English] Ultimate Web Development Course 2025",
    "description": "This is the only modern, always up-to-date Web Development course..."
  }
]

Why I Built This
I wanted to learn real-world web scraping and understand how spiders, selectors, item pipelines, and Scrapy’s engine work — so I scraped CodeWithHarry’s course catalog as a practice project.


If you want a more “founder-vibes” version or more detailed docs, just say the word.
