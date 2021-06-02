from django.db import models


class Objective(models.Model):
    POSIBLE_OBJECTIVE = [
        ('S', 'Salut'),
        ('Fr', 'Força'),
        ('P', 'Perdua'),
        ('Fl', 'Flexibilitat'),
        ('Rs', 'Resistencia'),
        ('Rc', 'Recuperacio'),
        ('A', 'Agilitat')
    ]
    objective = models.CharField(max_length=100, choices=POSIBLE_OBJECTIVE, primary_key=True)

    def __str__(self):
        return self.objective
