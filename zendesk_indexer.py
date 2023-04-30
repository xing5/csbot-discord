from zenpy import Zenpy
import re
import logging
# import trafilatura
# from trafilatura.settings import use_config
from content_indexer import index

logging.basicConfig(level=logging.INFO, force=True)

# tftConfig = use_config()
# tftConfig.set("DEFAULT", "EXTRACTION_TIMEOUT", "0")

creds = {
    'email' : '',
    'token' : '',
    'subdomain': ''
}

zenpy_client = Zenpy(**creds)

articles = zenpy_client.help_center.articles()
logging.info(f"number of articles: {len(articles)}")
for article in articles:
    logging.info(article.title)
    extracted_data = '\n'.join([ s for s in re.findall(r'>([^<]+)<', article.body) if s.strip() ])
    # extracted_data = trafilatura.bare_extraction(article.body, output_format='json', config=tftConfig)
    index('bigtimestudios', article.title, extracted_data)
    