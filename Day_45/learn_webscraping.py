from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup) # Prints the whole soup 
print(soup.prettify()) # First formats and then prints the soup

# Print the first anchor tag found in the soup (this method you can use to get first tag matching)
print(soup.a)

# Getting all the anchor tags or any tag (this method you can use to get all tag matching)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText(), "--->", tag.get('href'))

# Getting a particular element by using id 
heading = soup.find(name="h1", id="name")
print(heading)

my_list = soup.find(name="li", class_="my_list")
print(my_list)
print(my_list.text)

# Selecting a single element based on selector 
# Selecting based on the hireracy (first matching)
company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)