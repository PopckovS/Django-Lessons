from django.http import HttpResponse

# Импортируем модель Вопросов
from .models import Question, Choice


def index(request):
    """
    Главный метод, показывает все вопросы.
    URL: /
    """
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # print(latest_question_list)
    # output = ', '.join([q.question_text for q in latest_question_list])

    # Удалить все обьекты(записи) из таблицы Question
    # output = Question.objects.all().delete()

    # Получить все обьекты из таблицы Question
    questions = Question.objects.all()
    # output = ', '.join([q.question_text for q in questions])

    output = ''
    for question in questions:
        output += "Текст вопроса = {question_text} " \
                  "Дата публикации = {pub_date}" \
                  "<br>".format(
            question_text=question.question_text,
            pub_date=question.pub_date
        )

    return HttpResponse("Показывает все вопросы <hr> {output}".format(
        output=output
    ))


def detail(request, question_id: int):
    """
    Показать конкретный вопрос по его id
    URL: /<question_id>/detail
    """
    return HttpResponse(
        f"Показать конкретный вопрос по его id = {question_id}"
    )


def results(request, question_id: int):
    """
    Показать результат по конкретному вопросу по его id
    URL: /<question_id>/results
    """
    response = f"Показать результат по конкретному \n " \
               f"вопросу по его id = {question_id}"
    return HttpResponse(response)


def vote(request, question_id: int):
    """
    Голосование по вопросу по его id
    URL: /<question_id>/vote
    """
    return HttpResponse(f"Голосование по вопросу {question_id}")
