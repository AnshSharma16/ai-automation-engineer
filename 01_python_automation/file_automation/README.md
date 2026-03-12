# Phase 1 — Python Automation Foundations

This phase focuses on learning how to automate real tasks using Python.
The goal is to understand how scripts can interact with files, APIs, and scheduled jobs.

These automation patterns are widely used in **data engineering, backend automation, and AI automation workflows**.

---

## Skills Learned

* Python scripting for automation
* File system automation
* API data extraction
* Data processing using pandas
* Scheduling automated jobs

---

## Modules

### 1. File Automation

Automates file management tasks such as renaming files in bulk.

Script:

```
file_automation/auto_rename_files.py
```

Workflow:

```
Folder → Read files → Rename automatically
```

Example use cases:

* Renaming thousands of images
* Organizing downloaded files
* Cleaning dataset file names

---

### 2. API Automation

Fetches data from an API and stores it in CSV format.

Script:

```
api_automation/api_to_csv.py
```

Workflow:

```
API → JSON → Pandas → CSV
```

Example use cases:

* Collecting data for analytics
* Building ETL pipelines
* Monitoring external APIs

---

### 3. Scheduling Automation

Runs automation scripts automatically at scheduled intervals.

Script:

```
scheduling/scheduled_api_collector.py
```

Workflow:

```
Scheduler → Run script → Save output
```

Example use cases:

* Hourly data collection
* Automated monitoring systems
* Data pipeline jobs

---

## Technologies Used

* Python
* requests
* pandas
* schedule
* os

---

## Project Structure

```
01_python_automation
│
├── file_automation
│   ├── auto_rename_files.py
│   └── sample_files
│
├── api_automation
│   └── api_to_csv.py
│
└── scheduling
    └── scheduled_api_collector.py
```

---

## Example Outputs

Generated files are stored in the root `outputs/` directory.

Examples:

```
outputs/posts_data.csv
outputs/scheduled_posts.csv
```

---

## Key Takeaways

This phase introduces the fundamental automation patterns used in real-world systems:

* File automation
* Data extraction
* Scheduled workflows

These concepts are the foundation for more advanced automation such as:

* Web scraping bots
* Data pipeline automation
* AI-powered automation agents
