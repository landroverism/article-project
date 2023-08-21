class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine() for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_contributor(self)
        return article

    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines()))


class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine


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
