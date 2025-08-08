from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
soup = BeautifulSoup(response.content, 'html.parser')
content_div = soup.find('div', class_='article--viewer_content')
content = content_div.find_all('p')

@app.route("/")
def hello():
    if content_div:
        return render_template("index.html", paras = content)
    else:
        return "no article found"

if __name__ == "__main__":
    app.run(debug=True)