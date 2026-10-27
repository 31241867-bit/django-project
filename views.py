
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, Submission


def submit(request):
    if request.method == "POST":
        question_id = request.POST.get("question")
        choice_id = request.POST.get("choice")

        question = get_object_or_404(Question, id=question_id)
        choice = get_object_or_404(
            Choice, id=choice_id, question=question
        )

        Submission.objects.create(
            question=question,
            choice=choice
        )

        return redirect("show_exam_result")

    questions = Question.objects.all()
    return render(request, "exam.html", {"questions": questions})


def show_exam_result(request):
    submissions = Submission.objects.all()
    return render(
        request,
        "exam_result.html",
        {"submissions": submissions}
    )
