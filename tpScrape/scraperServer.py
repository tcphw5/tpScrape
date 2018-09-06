from flask import Flask
import scrapy

app = Flask(__name__)

class firstSpider(scrapy.Spider):
    name = "finder"

    def start_requests(self):
        urls = [
            'https://www.shopmyexchange.com/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'finders-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


"""
main page of server
"""
@app.route("/")
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4010, debug=True)
