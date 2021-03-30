from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        data = data.split(" ")
        
        if(len(data) > 3): 
            if(data[3] == "locator"):
                
                self.lad = data[0] 
                self.long = data[1] 