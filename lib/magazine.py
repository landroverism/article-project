class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all if magazine.name() == name), None)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def add_contributor(self, author):
        if author not in self._contributors:
            self._contributors.append(author)

    def contributors(self):
        return self._contributors

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def article_titles(self):
        return [article.title() for article in self._articles]

    def contributing_authors(self):
        return [author for author in self._contributors if len(author.articles()) > 2]
