class Pages():

    def __init__(self, title=None, url=None):
        if url is not None:
            self.title = title
            self.url = url
        else:
            raise ValueError
