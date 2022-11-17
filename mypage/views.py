from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'vinay', 'place': 'dehradun'}
    return render(request, 'index.html', params)


def analyse(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')

    if removepunc == 'on':
        analysed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analysed += char
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}

    elif fullcaps == 'on':
        analysed = djtext.upper()
        params = {'purpose': 'Capitalize the text', 'analysed_text': analysed}
    return render(request, 'analyse.html', params)
