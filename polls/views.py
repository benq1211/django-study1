import csv

from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render,reverse,get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.gzip import gzip_page

from .forms import ContactForm,AuthorForm,PublisherForm
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

def send_mail(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'polls/sendmail.html', {'form':form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            return HttpResponse('subject: %s message: %s sender %s cc_myself: %s'%(subject,message,sender, cc_myself))
        else:
            #return HttpResponse("Not valid")
            return render(request, 'polls/sendmail.html', {'form',form})
def author_add(request):
	if request.method == 'GET':
		form = AuthorForm()
		return render(request,'polls/author_add.html',{'form':form})


def publisher_add(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return HttpResponse("Add ok")
    else:
        form = PublisherForm(initial={'name': "O'Reilly"})
    return render(request, 'polls/publisher_add.html', {'form': form})
