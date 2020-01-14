# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime

class PricebotSpider(scrapy.Spider):
    name = 'pricebot'
    allowed_domains = ['www.amazon.ca/Bear-Paws-Birthday-Cake-168g/dp/B078QC91SV/ref=sr_1_2?keywords=bear+paws']
    start_urls = ['https://www.amazon.ca/Bear-Paws-Birthday-Cake-168g/dp/B078QC91SV/ref=sr_1_2?keywords=bear+paws/',
    'https://www.amazon.ca/Oreo-Original-Sandwich-Cookies-Grams/dp/B06W2PMJ89/ref=sr_1_4?keywords=oreo&qid=1576611333&sr=8-4'
    ]

    def parse(self, response):
        price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract() 
        title = response.xpath('//span[contains(@id,"productTitle")]/text()').extract()
        Time_Stamp = ['a', 'b']
        for item in zip(title, price, Time_Stamp):
            scraped_info = {
                'Product Title' : item[0],
                'Price' : item [1],
                'Time Stamp' : item [2]
              
                
            }
            
            scraped_info['Time Stamp'] = datetime.now().strftime("%m/%d/%Y/ %H:%M:%S")
            print (scraped_info['Time Stamp'])
        
            yield scraped_info
