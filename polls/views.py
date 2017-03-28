import csv
from django.shortcuts import render,reverse,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.views.decorators.http import require_http_methods,require_safe
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import never_cache

from .models import Choice,Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # output = ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #return render(request, 'index.html', context)

#@gzip_page
@never_cache
def detail(request,question_id):
    #return HttpResponse('Your are looking at question {}'.format(question_id))
    question = get_object_or_404(Question,id=question_id)
    return render(request, 'polls/detail.html',{'question': question})
def results(request,question_id):
    return HttpResponse('You are looking at results of question {}'.format(question_id))
#@require_http_methods(["POST"])
#@require_safe
@gzip_page
def vote(request, question_id):
    #return HttpResponse('Your are voting on question {}'.format(question_id))   
    p = get_object_or_404(Question,pk=question_id)
    print(request.method)
    if request.method == 'POST':
        choice_id = request.POST.get('choice',0)
        try:
            selected_choice = p.choices.get(pk=choice_id)
        except Choice.DoseNotExist:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice",
           })
        else:
           selected_choice.votes += 1
           selected_choice.save()
           return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
    else:
       return HttpResponse('Your post question id: %s' %question.id)        
def polls_404_handler(request):
    return HttpResponseNotFound("Not found")
 
def export(request):
  # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file', None)
        if upload_file is None:
            return HttpResponse('No file get')
        else:
            with open('/tmp/%s' % upload_file.name, 'wb') as f:
                f.write(upload_file.read())
            return HttpResponse('Ok')
    else:
        return render(request, 'polls/upload.html')

