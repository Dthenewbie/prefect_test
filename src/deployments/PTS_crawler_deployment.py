from prefect_github import GitHubRepository
from flows.PTS_crawler import PTS_news_scraper_pipeline


PTS_news_scraper_pipeline.from_source(
    source=GitHubRepository.load("antifraud"),
    entrypoint="src/flows/PTS_crawler.py:PTS_news_scraper_pipeline",
).deploy(
    name="pts_news_crawler_deployment",
    tags=["web crawler", "PTS", "case processing"],
    work_pool_name="antifraud",
    job_variables=dict(pull_policy="Never"),
    parameters=dict(pagenum = int(20)),
    cron="0 13 * * *"
)