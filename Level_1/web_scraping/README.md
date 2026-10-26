# Web Scraping Toolkit: Books & Quotes Scraper

Automated data collection from popular scraping practice sites, exported to clean CSV and JSON datasets.

## Overview

This project helps developers collect structured book and quote data from popular practice scraping sites without manual copying or browser extensions. It turns messy web pages into clean, analysis-ready datasets that can be exported to CSV or JSON. Teams can use it to build datasets for machine learning, price monitoring, or content aggregation projects.

## System Architecture

```mermaid
flowchart LR
  User["Developer / Scheduler"]
  Scraper["Scraping Engine"]
  SiteA["Books Website"]
  SiteB["Quotes Website"]
  Storage[("CSV / JSON Files")]

  User --> Scraper
  Scraper --> SiteA
  Scraper --> SiteB
  Scraper --> Storage

  style User fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
  style Scraper fill:#2e1065,stroke:#8b5cf6,stroke-width:2px,color:#fff
  style SiteA fill:#1E1E24,stroke:#3D3B3C,stroke-width:2px,color:#fff
  style SiteB fill:#1E1E24,stroke:#3D3B3C,stroke-width:2px,color:#fff
  style Storage fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#fff
```

## Features

### Automated Book Catalog Scraping

Crawls the entire book catalog across multiple pages, extracts the title, price, star rating, availability, and full URL for each book, then exports everything to CSV and JSON.

```mermaid
sequenceDiagram
  actor User
  participant Scraper
  participant Site as "Books Website"
  participant File as "Data File"

  User->>Scraper: Start book catalog crawl
  Scraper->>Site: Request catalog pages
  Site-->>Scraper: Return page HTML
  Scraper->>Scraper: Extract and normalize data
  Scraper->>File: Save to CSV and JSON
```

### Dynamic Quote Extraction

Pulls quotes embedded in JavaScript data objects, normalizes nested author fields, converts tag lists into readable strings, and exports the results to CSV and JSON.

```mermaid
sequenceDiagram
  actor User
  participant Scraper
  participant Site as "Quotes Website"
  participant File as "Data File"

  User->>Scraper: Start quote extraction
  Scraper->>Site: Request JavaScript page
  Site-->>Scraper: Return page with embedded data
  Scraper->>Scraper: Parse script and extract JSON
  Scraper->>File: Save quotes to CSV and JSON
```

### Structured Export and Quality Checks

Every scraper saves results to both CSV and JSON, then prints the dataset shape, a preview, and a missing-value summary so you can verify completeness at a glance.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Adeyiwolasuccess/Codveda_Internship.git
```

2. Move into the project folder:

```bash
cd Codveda_Internship
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the environment:

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

5. Install the dependencies:

```bash
pip install requests beautifulsoup4 pandas urllib3
```

## Usage

Run the book scraper:

```bash
python scraper.py
```

Run the quote scraper:

```bash
python dynamic_scraper.py
```

Each script creates two output files in the project root:

- `./books.csv` and `./books.json` from [`scraper.py`](./scraper.py)
- `./quotes.csv` and `./quotes.json` from [`dynamic_scraper.py`](./dynamic_scraper.py)

Running the book scraper produces output similar to the following:

```text
page 1: 20 books so far
page 2: 40 books so far
...
(1000, 5)
                                               title  price  rating availability                                               link
0  A Light in the Attic                               51.77       3     In stock  http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
```

Running the quote scraper produces output similar to the following:

```text
page 1: 10 quotes so far
page 2: 20 quotes so far
...
(100, 5)
                                                text           author  author_slug                                       author_link                                  tags
0  “The world as we have created it is a process...  Albert Einstein  Albert-Einstein  /author/show/9810.Albert_Einstein  change, deep-thoughts, thinking, world
```

## Technologies Used

| Technology | Purpose |
|---|---|
| [Python](https://www.python.org/) | Core language for the scraping scripts |
| [requests](https://requests.readthedocs.io/) | HTTP sessions with retry logic and headers |
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) | HTML parsing and element selection |
| [pandas](https://pandas.pydata.org/) | Data normalization, cleaning, and export |
| [urllib3](https://urllib3.readthedocs.io/) | Configurable retry behavior for network calls |

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, make your changes, and open a pull request.

## Author

- LinkedIn: [Success Adeyiwola](https://linkedin.com/in/successadeyiwola)
- X: [jathom48](https://x.com/jathom48)

## Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Requests](https://img.shields.io/badge/Requests-2B2B2B?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://dokugen.samueltuoyo.com)