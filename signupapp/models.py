from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class SignUp(models.Model):

	firset_name = models.CharField(max_length=120,null=True,blank=True)
	last_name = models.CharField(max_length=120,null=True,blank=True)
	email = models.EmailField()
	times_temp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updatad = models.DateTimeField(auto_now_add=False, auto_now=True)
	image= models.ImageField()

	"""docstring for SignUp"""




	def __unicode__(self):
		return smart_unicode(self.email)
		
		