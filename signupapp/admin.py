from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	form = SignUpForm #  laow 3ayz adyf form 3la admin.py
	#class Meta:
#		model = SignUp




admin.site.register(SignUp,SignUpAdmin)

		