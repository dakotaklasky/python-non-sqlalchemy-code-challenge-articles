class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    def get_title(self):
        return self._title

    def set_title(self,new_title):
        if isinstance(new_title,str) and 5<= len(new_title) <= 50 and not hasattr(self,'_title'):
            self._title = new_title
    
    title = property(get_title,set_title)

    def get_author(self):
        return self._author
    
    def set_author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
    
    author = property(get_author,set_author)

    def get_magazine(self):
        return self._magazine
    
    def set_magazine(self,new_magazine):
        if isinstance(new_magazine,Magazine):
            self._magazine = new_magazine
    
    magazine = property(get_magazine, set_magazine)

        
class Author:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self,new_name):
        if isinstance(new_name,str) and len(new_name) > 0 and not hasattr(self,'_name') :
            self._name = new_name
    
    name = property(get_name,set_name)

    def articles(self):
        #returns list of all the articles author has written of type Article
        my_articles = []
        for article in Article.all:
            if article.author is self:
                my_articles.append(article)
        return my_articles

    def magazines(self):
        my_articles = self.articles() #get all articles for particular author

        if len(my_articles) ==0:
            return None
        else:
            #get all magazines from articles
            my_magazines = []
            for article in my_articles:
                my_magazines.append(article.magazine)
            return list(set(my_magazines))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        my_magazines = self.magazines()

        if my_magazines is None:
            return None
        else:
            my_categories = []
            for magazine in my_magazines:
                my_categories.append(magazine.category)
            return list(set(my_categories))


class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    def get_name(self):
        return self._name
    
    def set_name(self,new_name):
        if isinstance(new_name,str) and 2<= len(new_name) <= 16:
            self._name = new_name
    
    name = property(get_name,set_name)

    def get_category(self):
        return self._category
    
    def set_category(self,new_category):
        if isinstance(new_category,str) and len(new_category)>0:
            self._category = new_category
    
    category = property(get_category,set_category)

    def articles(self):
        my_articles = []
        for article in Article.all:
            if article.magazine is self:
                my_articles.append(article)
        return my_articles

    def contributors(self):
        my_articles = self.articles() #get all articles for particular magazine
        if len(my_articles) == 0:
            return None
        else:
            #get all authors from magazine
            my_authors = []
            for article in my_articles:
                my_authors.append(article.author)
            return list(set(my_authors))

    def article_titles(self):
        my_articles = self.articles() #get all articles in magazine

        if len(my_articles) == 0:
            return None
        else:
            my_titles = []
            for article in my_articles:
                my_titles.append(article.title)
            return my_titles

    def contributing_authors(self):
        my_articles = self.articles() #all articles in magazine
        
        if len(my_articles) == 0:
            return None
        else:
            author_count = {}

            for article in my_articles:
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] = 1
            
            big_authors = []
            for author in author_count:
                if author_count[author] > 2:
                    big_authors.append(author)
            if len(big_authors) == 0:
                return None
            else:
                return big_authors
    
    @classmethod
    def top_publisher(cls):
        #returns magazine with most articles
        if len(cls.all) == 0: 
            return None
        max_articles = 0
        max_magazine = cls.all[0]

        for mag in cls.all:
            if len(mag.articles()) > max_articles:
                max_articles = len(mag.articles())
                max_magazine = mag

        if max_articles == 0:
            return None
        else:
            return max_magazine