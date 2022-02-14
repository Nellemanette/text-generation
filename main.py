# This is a sample Python script.
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def extract_lyrics():
    url = "https://www.azlyrics.com/lyrics/her/slide.html"

    html = urlopen(url.strip()).read()
    print(html)
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    with open('text_generator_dataset.txt', 'a') as f:
        f.write(text)

    print(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    extract_lyrics()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
