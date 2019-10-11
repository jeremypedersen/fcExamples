import logging
import requests
import json
from bs4 import BeautifulSoup as bs

# A simple Function Compute example that will produce
# the page title for any webpage (URL) it is given as input
# 
# This function relies on the BeautifulSoup and requests
# libraries, and is a good way to test your understanding of
# the 'fun' command, which is needed to pull in non-standard
# dependencies like BeautifulSoup
def handler(event, context):
  # Get logging info
  logger = logging.getLogger()

  # Log entire raw event in case we need to do troubleshooting later
  logger.info(event)

  # Load URL (from event string)
  try:
    url = str(event.decode()).strip()
  except:
    pageTitle = "ERROR: Failed to decode event string passed to FC...is it a valid URL?"

  # Fetch page with requests, and convert to a BeautifulSoup object
  try:
    r = requests.get(url)
    page = bs(r.text)
  except:
    pageTitle = "ERROR: Failed to fetch page, check URL and ensure it points at a valid HTML document"

  # Extract page title
  try:
    pageTitle = page.title.text
  except:
    pageTitle = "ERROR: This page has no <title> tag"

  return pageTitle