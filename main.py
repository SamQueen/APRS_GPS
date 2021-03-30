from urllib.request import urlopen
from html_parser import MyHTMLParser


def main():
    callsign = input("Enter callsign: ")
    url = "https://aprs.fi/info/a/" + callsign
    page = urlopen(url)
    html = page.read().decode("utf-8")
    
    parser = MyHTMLParser()
    parser.feed(html)
    
    laditude = parser.lad
    longitude = parser.long
    
    print("\nLaditude : ", laditude)
    print("Longitude : ", longitude)
    
main();