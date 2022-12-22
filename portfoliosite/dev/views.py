from django.shortcuts import render
from .models import about, work, skill, contact
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your views here.

def main(request):
    #yosh
    men = about.objects.first()
    y, m, d = str(men.year_of_birth).split('-')
    tugilgan_kun = date(int(y), int(m), int(d))
    yosh = relativedelta(date.today(), tugilgan_kun)

    #malaka
    y, m, d = str(men.year_of_programming).split('-')
    staj = date(int(y), int(m), int(d))
    staj = relativedelta(date.today(), staj)

    #mahorat
    skills = skill.objects.all()

    #ishlar
    works = work.objects.all()
    # @dp.message_handler()
    # async def yest(msg: types.message):
    #     await bot.send_message(1361526026, "salom")

    #contact
    if request.method == 'POST':
        klient = contact()
        klient.name = request.POST.get('name')
        klient.email = request.POST.get('email')
        klient.message = request.POST.get('message')
        klient.save()


    #resume
    return render(request, 'index.html',{'men' : men, 'yosh' : yosh, 'staj' : staj, 'skill' : skills, 'works' : works})

