#-*-coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import Personal

def person(request):
	return render(request,'person.html')


def personal_list(request):
	username = request.GET.get('user')
	sex = request.GET.get('sex')
	birth_date = request.GET.get('birth_date')
	work_date = request.GET.get('work_date')
	address = request.GET.get('address')
	city = request.GET.get('city')
	tell = request.GET.get('tell')
	mail = request.GET.get('mail')
	wendy = request.GET.get('wendy')
	paper = request.GET.get('paper')
	card_id = request.GET.get('card_id')
	Personal.objects.create(
		name = username,
		sex = sex,
		birth_date = birth_date,
		work_date = work_date,
		address = address,
		city = city,
		tell = tell,
		mail = mail,
		wendy = wendy,
		paper =paper,
		card_id = card_id
	)
	personals = Personal.objects.all()
	return render(request,'personal_list.html',context={'personals':personals})


def personal_delete(request):

	Personal.objects.filter(id = request.GET.get('id')).delete()

	personals = Personal.objects.all()

	return render(request,'personal_list.html',context={'personals':personals})

def personal_update_html(request):

    personal = Personal.objects.get(id=request.GET.get('id'))
    return render(request,'personal_update.html',context={'personal':personal})

def personal_update(request):
	username = request.GET.get('user')
	sex = request.GET.get('sex')
	birth_date = request.GET.get('birth_date')
	work_date = request.GET.get('work_date')
	address = request.GET.get('address')
	city = request.GET.get('city')
	tell = request.GET.get('tell')
	mail = request.GET.get('mail')
	wendy = request.GET.get('wendy')
	paper = request.GET.get('paper')
	card_id = request.GET.get('card_id')
	Personal.objects.filter(id=request.GET.get('id')).update(
		name = username,
		sex = sex,
		birth_date = birth_date,
		work_date = work_date,
		address = address,
		city = city,
		tell = tell,
		mail = mail,
		wendy = wendy,
		paper =paper,
		card_id = card_id
	)
	personals = Personal.objects.all()

	return render(request,'personal_list.html',context={'personals':personals})


