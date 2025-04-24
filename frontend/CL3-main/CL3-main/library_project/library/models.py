from django.db import models

class Book(models.Model):
    FICTION = 'Fiction'
    NON_FICTION = 'Non-fiction'
    SCIENCE = 'Science'
    HISTORY = 'History'
    BIOGRAPHY = 'Biography'

    CLASSIFICATION_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-fiction'),
        (SCIENCE, 'Science'),
        (HISTORY, 'History'),
        (BIOGRAPHY, 'Biography'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    classification = models.CharField(max_length=50, choices=CLASSIFICATION_CHOICES)

    def __str__(self):
        return f"{self.title} by {self.author}"
