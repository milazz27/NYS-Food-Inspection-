
with open("temp.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        county = line.strip()
        print("<a href=\"#\">", county, "</a>")