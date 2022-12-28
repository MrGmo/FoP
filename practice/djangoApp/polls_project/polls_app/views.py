from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = latest_question_list[question_id-1]
    data = { 'question': question }
    return render(request, 'polls/detail.html', data)

def results(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = latest_question_list[question_id-1]
    selected_choice = question['choices'][int(request.POST['choice'])-1]
    selected_choice['votes'] += 1
    
    # redirect the user to a GET route, so they don't resubmit their vote if they refresh the page
    return HttpResponseRedirect(f'/polls/{question_id}/results')


latest_question_list = [
    {
        'id' : 1,
        'question_text': 'whats up',
        'pub_date':'2022-01-04',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
    {
        'id' : 2,
        'question_text': 'whats new',
        'pub_date':'2022-02-09',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
]