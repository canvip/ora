from django.shortcuts import render  #,HttpResponse
#from django.http import 
from .forms import SignUpForm
import datetime

# Create your views here.
def home(request):
	title = 'welcom ArE You nEd sign up'#1#
#	if request.user.is_authenticated():#2#
#		title = 'welcom %s' %(request.user)#3#law 3ayz tshof uesr signup

	if request.method == "POST":
		print request.POST
	form = SignUpForm()

	today = datetime.datetime.now().date()
	
	#form = SignUpForm(request.POST)
	context = {
	"title":title,
	"form":form,
	"today" : today,
	}

	return render(request,"signup.html",context)
	






