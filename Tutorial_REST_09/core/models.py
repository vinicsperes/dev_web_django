from django.db import models

class Recipe(models.Model):
  DIFFICULTY_LEVELS = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
  )
  
  name = models.CharField(max_length=120)
  ingredients = models.CharField(max_length=400)
  picture = models.FileField()
  difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
  prep_time = models.PositiveIntegerField()
  prep_guide = models.TextField()

  def __str__(self):
    return f"Recipe for {self.name}"