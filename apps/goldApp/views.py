from django.shortcuts import render, redirect
import random
from datetime import datetime

#make dictionary  earned = true

def index(request):
	if 'gold' in request.session:
		pass
	else:
		request.session['gold'] = 0
	if 'messages' in request.session:
		pass
	request.session['messages'] = []
	return render(request, 'goldTemp/index.html')

def process_money(request):
	i = datetime.now()
	random.randrange(0,2)
	if request.POST['building'] == 'farm':
		gold = random.randrange(10,20)
		request.session['gold'] += gold
		string = "earned" + " " +  str(gold) + " " + "gold" + " "  + "from the farm!" + " " + str(i) 
		request.session['messages'].append(string)
		print gold
		print request.session['messages']

	if request.POST['building'] == 'cave':
		gold = random.randrange(5,11)
		request.session['gold'] += gold
		string = "earned" + " " +  str(gold) + " " + "gold" + " "  + "from the cave!" + " " + str(i)
		request.session['messages'].append(string)
		print gold
		print request.session['messages']

	if request.POST['building'] == 'house':
		gold = random.randrange(2,6)
		request.session['gold'] += gold
		string = "earned" + " " +  str(gold) + " " + "gold" + " "  + "from the house!" + " " + str(i)
		request.session['messages'].append(string)
		print gold

	if request.POST['building'] == 'casino':
		gold = random.randrange(-50,50)
		request.session['gold'] += gold
		if gold < 0:
			string = "lost" + " " + str(gold) + "  " +  "gold" + " "  + "from the casino!" + " " + str(i)
			request.session['messages'].append(string)
		else:
			string = "earned" + " " +  str(gold) + " " + "gold" + " "  + "from the casino!" + " " + str(i)
			request.session['messages'].append(string)
		print gold
	return render(request, 'goldTemp/index.html')



def clear(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')
