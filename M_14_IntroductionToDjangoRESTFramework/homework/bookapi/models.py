from django.db import models
from django.utils.translation import gettext_lazy as _



class Author(models.Model):
    """Book authors model."""
    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))
    year_birth = models.IntegerField(verbose_name=_("Year of birth"))

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
        ordering = ('last_name',)


class Book(models.Model):
    """Books model."""
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    isbn = models.CharField(
        max_length=20,
        verbose_name=_("ISBN number of the book.")
    )
    publication_date = models.IntegerField(
        verbose_name=_("Year the book was published.")
    )
    pages = models.IntegerField(verbose_name=_("Number of pages"))
    authors = models.ManyToManyField(Author, related_name="books", verbose_name=_("Author"))

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ('title',)

    def __str__(self):
        return "{title}".format(title=self.title)

    def authors_names(self) -> list:
        return ["{a} {b}".format(a=a.first_name, b=a.last_name) for a in self.authors.all()]