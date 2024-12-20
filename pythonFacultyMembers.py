from bs4 import BeautifulSoup
import os

# Function to get information from the HTML file
def extractInfo(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract the information from the HTML file
    name = soup.find('div', class_='name').get_text(strip=True)
    titleAndDep = soup.find('div', class_='first-appointment').get_text(strip=True)
    title, department = titleAndDep.split('—')
    title = title.strip()
    department = department.strip()
    office = soup.find('div', class_='office').get_text(strip=True)
    phone = soup.find('div', class_='phone').get_text(strip=True).replace('phone: ', '')
    email = soup.find('div', class_='email').a.get_text(strip=True)
    
    return {
        'Name': name,
        'Title': title,
        'Department': department,
        'Office': office,
        'Phone': phone,
        'Email': email
    }

# Function to write faculty information to a text file
def writeFile(facultyInfo, output):
    with open(output, 'w') as file:
        for faculty in facultyInfo:
            file.write(f"Name: {faculty['Name']}\n")
            file.write(f"Title: {faculty['Title']}\n")
            file.write(f"Department: {faculty['Department']}\n")
            file.write(f"Office: {faculty['Office']}\n")
            file.write(f"Phone: {faculty['Phone']}\n")
            file.write(f"Email: {faculty['Email']}\n")
            file.write("\n")

# HTML files to get output for
htmlFiles = [
    'Faculty Profiles1.html',
    'Faculty Profiles2.html',
    'Faculty Profiles3.html',
    'Faculty Profiles4.html'
]

faculty = []

# Extract faculty information from HTML file
for html_file in htmlFiles:
    with open(html_file, 'r', encoding='utf-8') as file:
        htmlInfo = file.read()
        facultyData = extractInfo(htmlInfo)
        faculty.append(facultyData)

# Write the extracted information 
output = 'FacultyOutput.txt'
writeFile(faculty, output)

print(f"Faculty info has been written to {output}")