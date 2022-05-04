class News:
    def __init__(self,author,title,description,urlToImage,date,content,url):
        self.author=author
        self.title=title
        self.description=description
        self.urlToImage=urlToImage
        self.date=date
        self.content=content
        self.url=url

class Sources:
    def __init__(self,id, name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url