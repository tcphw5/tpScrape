


Webscraper project to solve this problem :


Lowes
basically i want to be able to have a crawler traverse the entire lowes catalog and return some json to me. it will be up to the programmer to determine the best method to do that but here are the key requirements that I need on my end:

    lowes sku (found in the URL)
    item category bread crumb -- full list
    item title
    item number
    model number
    price
    buy in bulk (optional, need to look at the product image for a badge to appear -- see sample model number 10650136)
    min quantities needed for purchase
    ship to store available
    parcel shipping available
    raw contents of description
    raw contents of specification

this will get big pretty quick, so they can also submit a proposal for breaking the json up into manageable chunks

i need this written in python 3 (2.x won't be acceptable here) with as few dependencies as possible and any that are should be non-commercial. must be run on linux, but given the other requirements this shouldn't be an issue.

Shopmyexchange.com:

similar to lowes, return JSON

needs:

    category breadcrumbs
    price (ignore regular/sale price -- only want the actual price to be paid)
    quantity available even if sold out
    raw contents of product overview
    product title
    in page data  there is a javascript element with following items:
     // AAFES-CNET
    					      ccs_cc_args.push(['cpn', '7816888']);
    					      ccs_cc_args.push(['mf', 'LEGO']);

    					      ccs_cc_args.push(['pn', '6136476']);
    					      // ccs_cc_args.push(['upcean', 'UPC_EAN_CODE']);
    					      // ccs_cc_args.push(['ccid', 'CATALOG_CODE']);
    					      ccs_cc_args.push(['lang', 'en']);
    					      ccs_cc_args.push(['market', 'us'])
    Return all items as applicable above (even if in this examples don't have catalog code or UPC -- where applicable, I want it)


walmart:

Same requirements as others regarding Python3 and linux, however, must be able to pre-filter results by department e.g. "Sports, Fitness & Outdoors"

    category breadcrumb
    price
    walmart item number
    SKU (not visible on page -- look for this tag and get 'contents' <meta itemprop="sku" content=" 46271769">
    Brand <span itemprop="brand">
    GTIN13 <span itemprop="gtin13" content=" 0897454001857"></span>
    Price
    Primary Shipped & Sold By




