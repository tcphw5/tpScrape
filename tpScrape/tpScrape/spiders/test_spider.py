import scrapy


"""
some require login to see exchange price

want to find
            div class = aafes-thumbnail-item
            div class = aafes-item-name (contains a with href to item page)
            div class = item-pricing
            p class = aafes-price
            nav class = aafes-breadcrumb  (a's)

on item page:
            div class = jsPDPAccordionContent sm-hidden

            Looks like max of 20
            if out of stock option value 1 is 0
            select id = "prodQtySelection" followed by numbers
                option value = "1"
                option value = "2" ect... get last value

            in generic named javascript tag.
            maybe search for "ccs_cc_args

             // AAFES-CNET
					      ccs_cc_args.push(['cpn', '7816888']);
					      ccs_cc_args.push(['mf', 'LEGO']);

					      ccs_cc_args.push(['pn', '6136476']);
					      // ccs_cc_args.push(['upcean', 'UPC_EAN_CODE']);
					      // ccs_cc_args.push(['ccid', 'CATALOG_CODE']);
					      ccs_cc_args.push(['lang', 'en']);
					      ccs_cc_args.push(['market', 'us'])

            price: div class = aafes-price-strong

            breadcrumbs also can be easily ffound on item page
            nav class = aafes-breadcrumb omit-current-page
            or at the bottom in plaintext (can maybe search breadcrumbs)
            Checking the CLP/PLP page breadcrumbs String: ,apparel, womens apparel, tops, blouses & tunics
"""

class firstSpider(scrapy.Spider):
    name = "finderz"

    def start_requests(self):
        urls = [
            'https://www.shopmyexchange.com/browse/electronics/tvs/projectors/_/N-2096063601?N=&Ns=&Ntt=&Nrpp=30'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'finders-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
