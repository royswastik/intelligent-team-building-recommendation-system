__author__ = 'Swastik'
class Publication:
    abstract = ""
    citations = ""
    keywords = []
    sections = []
    title = ""
    def __init__(self, title):
      self.title = title

    def get_abstract(self):
        pass

    def get_title(self):
        pass
