# Import the classes from the respective files
from Author import Author
from Article import Article
from magazine import Magazine

# Create instances and test methods
author1 = Author("John Owens")
author2 = Author("C.D Brooks")

magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Fashion Trends", "Fashion")

article1 = author1.add_article(magazine1, "The Future of Coding")
article2 = author1.add_article(magazine2, "Summer Fashion Essentials")
article3 = author2.add_article(magazine1, "Ethical Dilemmas in Tech")

# Test methods
print(article1.title())
print(article1.magazine().name())
print(article1.author().name())

print(author1.articles())
print(author1.magazines())
print(author1.topic_areas())

print(magazine1.contributors())
print(magazine1.article_titles())
print(magazine1.contributing_authors())
