from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=9d7d97725ad7b0de1b98f697a9cbf8c7&countries=in')
    res = r.json()
    data = res['data']
    title =[]
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])

    news = zip(title,description, image, url)
    return render(request,'newsapp/index.html', {'news':news})
