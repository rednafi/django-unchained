from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""

    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    def __str__(self):
        """String for representing the model object."""
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = (
        models.TextField(
            max_length=1000, help_text="Enter a brief description of the book"
        ),
    )

    isbn = (
        models.CharField(
            "ISBN",
            max_length=13,
            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
        ),
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self) -> str:
        """String for representing the model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to acess a detail record for this book."""

        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be
    borrowed from the library)."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique id for this particular book across the whole library",
    )
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id}({self.book.title})"


class Author(models.Model):
    """Model representing an author."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to acess a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self) -> str:
        """String for representing the Model object."""

        return f"{self.last_name}, {self.first_name}"
