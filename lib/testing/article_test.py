import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        # comment out the next two lines if using Exceptions
        article_1.title = 500  # This line should be indented correctly
        # assert article_1.title == "How to wear a tutu with style"
        
        assert isinstance(article_1.title, str)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Article(author, magazine, 500)

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= len(article_1.title) <= 50

        # uncomment the next two lines if using Exceptions
    with pytest.raises(Exception):
            Article(author, magazine, "Test")

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")

    #... rest of the code...