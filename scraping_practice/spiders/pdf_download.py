import scrapy
import urllib
import os


class PdfDownloadSpider(scrapy.Spider):
    name = "pdf-download"
    allowed_domains = ["www.city.niigata.lg.jp"]
    start_urls = ["https://www.city.niigata.lg.jp/chuo/kohoshi/index2011/r05/chuo_1001"]

    def parse(self, response):
        save_dir = 'pdfs'
        if save_dir not in os.listdir("./"):
            os.mkdir(save_dir)

        base_url = "https://www.city.niigata.lg.jp/chuo/kohoshi/index2011/r05/chuo_1001/"

        contents = response.xpath('//td[3]/p/a')
        for content in contents:
            # names = content.xpath('@href/text()').extract()
            names = content.xpath('@href')
            print(names) # namesには"pdf/396_1.pdf"のデータが入る
            for name in names :
                file_name_extract = name.extract()
                pdf_path = os.path.join(base_url, file_name_extract) #PDFのWeb上でのURLになるように結合する。
                #pdf_path = re.sub(r'^.', base_url, pdf_relative_path) ☜これだと、
                #https://www.city～/chuo_1001/df/396_1.pdf の「p」ように、最初の一文字がなぜか消える.
                #print(pdf_path)
                file_name = file_name_extract.split("/")[-1] #「396_1.pdf」が取得できる。これをローカルに保存するファイル名にする。
            #print(file_name)
                urllib.request.urlretrieve(pdf_path, os.path.join(save_dir, file_name))
