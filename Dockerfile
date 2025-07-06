FROM python:3.9.23-bookworm
WORKDIR /app
ADD scrape.py .
RUN pip install beautifulsoup4 python-dotenv
CMD ["python", "./scrape.py"]