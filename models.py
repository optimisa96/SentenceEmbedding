class ArticleData(dict):
    def __init__(self, source, heading, summary, text):
        self.source = source
        self.heading = heading
        self.summary = summary
        self.text = text
        dict.__init__(self, source = source, heading = heading, summary = summary, text = text)

    def __str__(self):
        return f"Source: {self.source}\nHeading: {self.heading}\nSummary: {self.summary}\nText: {self.text}"