import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     author_1.name = "ActuallyTopher"
        # assert author_1.name == "Carry Bradshaw"

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     author_2.name = 2
        # assert author_2.name == "Nathaniel Hawthorne"

    def test_name_len(self):
        """author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert hasattr(author_1, "name")
        assert len(author_1.name) > 0
        assert hasattr(author_2, "name")
        assert len(author_2.name) > 0

        # Uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Author(2)

    def test_add_article(self):
        """creates and returns a new article given a magazine and title"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
        article_2 = author_1.add_article(magazine_2, "2023 Eccentric Design Trends")
        article_3 = author_1.add_article(magazine_2, "Carra Marble is so 2020")

        assert isinstance(article_1, Article)
        assert len(author_1.articles()) == 3
        assert len(magazine_1.articles()) == 1
        assert len(magazine_2.articles()) == 2
        assert article_1 in magazine_1.articles()
        assert article_2 in magazine_2.articles()
        assert article_3 in magazine_2.articles()

    def test_topic_areas(self):
        """returns a list of topic areas for all articles by author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_2, "Carrara Marble is so 2020")
        author_2.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(author_1.topic_areas()) == 2
        assert set(author_1.topic_areas()) == {"Fashion", "Architecture"}
        assert author_2.topic_areas() == ["Architecture"]

    def test_topic_areas_are_unique(self):
        """topic areas are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Giorgio Faletti")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "Dating life in NYC")
        author_1.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(set(author_1.topic_areas())) == len(author_1.topic_areas())
        assert len(author_1.topic_areas()) == 2
        assert "Fashion" in author_1.topic_areas()
        assert "Architecture" in author_1.topic_areas()
        assert author_2.topic_areas() is None