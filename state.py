import json

# Check each link that gets posted
class State:
    def __init__(self):
        self.posted_links = set()
        self.filename = "state.json"
        
    # loads file and set posted links variable
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                links = json.load(f)
                self.posted_links = set(links)
        except FileNotFoundError:
            self.posted_links = set()
    
    # writes links of files after it is done running
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(list(self.posted_links), f)
    
    # return link that is already posted
    def is_posted(self, link):
        return link in self.posted_links
    
    # add link to set
    def add_link(self, link):
        self.posted_links.add(link)
            
            