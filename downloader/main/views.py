from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<img src="https://i.playground.ru/p/1Fcw47v1SBe3zmpSd1ovvg.jpeg">')


def about(request):
    return HttpResponse('https://i.mycdn.me/getVideoPreview?id=1472155421333&idx=5&type=39&tkn=PX300WXAQP4LLMykZzAoe7_yN_U&fn=vid_l')
