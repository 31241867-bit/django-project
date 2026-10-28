
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_ids):
        correct_ids = set(
            self.choice_set.filter(is_correct=True)
            .values_list('id', flat=True)
        )
        selected_ids = set(selected_ids)

        return bool(correct_ids) and correct_ids == selected_ids


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(
        'Enrollment',
        on_delete=models.CASCADE
    )
    choices = models.ManyToManyField(Choice)
