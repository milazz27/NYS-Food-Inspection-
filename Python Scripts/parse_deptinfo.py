from bs4 import BeautifulSoup
import csv

# Load HTML file
with open("../Data/relevant_content.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = []

# Loop through all directory entries
for div in soup.find_all("div", class_="member-directory"):
    # Extract county and main URL
    county_tag = div.find("h2")
    county_link = county_tag.find("a") if county_tag else None
    county_name = county_link.get_text(strip=True) if county_link else ""
    county_url = county_link["href"] if county_link and county_link.has_attr("href") else ""

    # Extract department
    dept_tag = div.find("h2", class_="subtitle")
    department = dept_tag.get_text(strip=True) if dept_tag else ""

    # Extract phone (first 'a' tag with class='phone')
    phone_tag = div.find("a", class_="phone")
    phone = phone_tag.get_text(strip=True) if phone_tag else ""

    # Extract fax (first 'a' tag with class='fax')
    fax_tag = div.find("a", class_="fax")
    fax = fax_tag.get_text(strip=True) if fax_tag else ""

    rows.append([county_name, department, phone, fax, county_url])

# Write results to CSV
with open("county_health_departments.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["County", "Department", "Phone", "Fax", "Website"])
    writer.writerows(rows)

print(f"✅ Extracted {len(rows)} entries with phone/fax numbers → county_health_departments.csv")
