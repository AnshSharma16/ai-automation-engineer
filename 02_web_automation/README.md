# Phase 2 — Web Automation

This phase focuses on automating web interactions and extracting data from websites using Python.

The goal is to learn how automation scripts can interact with real websites, collect structured data, and build small automation bots.

---

## Skills Learned

* Web scraping using `requests` and `BeautifulSoup`
* Browser automation using `Selenium`
* Extracting structured data from web pages
* Building small automation bots
* Monitoring product prices automatically
* Data logging and visualization

---

## Modules

### 1. Requests Scraping

Scrapes static HTML pages using `requests` and `BeautifulSoup`.

Script:

```
requests_scraping/scrape_quotes.py
```

Workflow:

```
Website → HTML → BeautifulSoup → Extract data → CSV
```

---

### 2. Selenium Browser Automation

Automates browser actions such as opening websites, typing text, and interacting with page elements.

Script:

```
selenium_browser_automation/selenium_google_search.py
```

Workflow:

```
Python → Selenium → Chrome → Website interaction
```

Example actions:

* open webpage
* type search query
* press keyboard keys
* interact with elements

---

### 3. Job Scraper Bot

Collects job listings from a website and saves them as structured data.

Script:

```
job_scraper_bot/job_scraper.py
```

Data collected:

* job title
* company name
* location

Workflow:

```
Website → Selenium → Extract job data → CSV
```

---

### 4. Price Tracker Bot

A small monitoring bot that tracks product prices over time.

Scripts:

```
price_tracker_bot/price_tracker.py
price_tracker_bot/dashboard.py
```

Features:

* scrape product price
* compare with target price
* send email alerts
* store price history
* visualize price trends

Workflow:

```
Scraper → Save price history → Compare price → Send alert → Dashboard
```

Example output:

```
price_history.csv
price_chart.png
```

---

## Technologies Used

* Python
* Selenium
* BeautifulSoup
* requests
* pandas
* matplotlib
* webdriver-manager

---

## Key Takeaways

This phase introduces the core concepts of web automation:

* scraping static websites
* automating browsers
* building monitoring bots
* storing and visualizing scraped data

These skills are commonly used in:

* automation engineering
* data collection pipelines
* monitoring systems
* testing frameworks
