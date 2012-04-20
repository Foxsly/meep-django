from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import timezone
from meep.models import Topic, Message, User

def index(request):
    return HttpResponse("Hello, world. You're at the meep index.")

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    messages = Message.objects.filter(msg_topic=topic_id).order_by('created_at')
    return render_to_response('meep/topic.html', {'topic': topic, 'message_list':messages}, context_instance=RequestContext(request))

def topics(request):
    topic_list = Topic.objects.all()
    return render_to_response('meep/index.html', {'topic_list': topic_list}, context_instance=RequestContext(request))

def add_message(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    msg_post = request.POST['message']
    msg_author = User.objects.get(pk=1)
    message = Message(post=msg_post, created_at=timezone.now(), author=msg_author, msg_topic=topic)
    message.save()
    return HttpResponseRedirect(reverse('meep.views.topic', args=(topic_id,)))

def delete_message(request, topic_id):
    message = Message.objects.get(pk=request.POST['mid'])
    message.delete()
    return HttpResponseRedirect(reverse('meep.views.topic', args=(topic_id,)))

def add_topic(request):
    topic_author = User.objects.get(pk=1)
    topic = Topic(title=request.POST['title'], author = topic_author)
    topic.save()
    return HttpResponseRedirect(reverse('meep.views.topic', args=(topic.id,)))