import csv
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://raw.githubusercontent.com/Technical-Debt-Large-Scale/qualification/main/html/modified_my_atd_extracted.html"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the paper elements on the webpage
papers = soup.find_all("div", class_="paper-info")

# Open a CSV file to write the data
with open("papers.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Title", "Authors", "Year", "Summary", "Link"])

    # Loop through each paper element and extract the data
    for paper in papers:
        if paper.find("h2") is not None:
          title = paper.find("h2").text.strip()
        else:
          title = ''
        if paper.find("h3") is not None:
          authors = paper.find("h3").text.strip()
        else:
          authors = ''
        if paper.find("h4") is not None:
          year = paper.find("h4").text.strip()
        else:
          year = 0
        if paper.find("p") is not None: 
          summary = paper.find("p").text.strip()
        else:
          summary = ''
        if paper.find("a") is not None:
          link = paper.find("a")["href"]
        else: 
          link = ''
        
        # Write the data to the CSV file
        writer.writerow([title, authors, year, summary, link])