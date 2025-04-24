from firecrawl import FirecrawlApp
from dotenv import load_dotenv
load_dotenv()
os.environ['FIRE_CRAWL_API'] = os.getenv('FIRE_CRAWL_API')

app = FirecrawlApp(api_key=FIRE_CRAWL_API)

# Scrape multiple websites:
batch_scrape_result = app.batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], formats=['markdown', 'html'])
print(batch_scrape_result)

# Or,we can use the asynchronous method:
batch_scrape_job = app.async_batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], formats=['markdown', 'html'])
print(batch_scrape_job)

# (async) we can then use the job ID to check the status of the batch scrape:
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job.id)
print(batch_scrape_status)
