from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class CaseStatus(models.Model):
	casenumber = models.CharField(max_length=10,primary_key=True)
	description=models.TextField()
	courtname= models.CharField(max_length=200)
	verdict=models.TextField()
	caseflag=models.BooleanField()
	dateofregister=models.DateTimeField()

	def __unicode__(self):
		return self.casenumber
	def __str__(self):
		return self.casenumber


class Complaint(models.Model):
	complaintid= models.AutoField(primary_key=True)
	dateofcomplaint=models.DateTimeField(auto_now=False, auto_now_add=True)
	content = models.TextField()
	policestation= models.CharField(max_length=120)
	location=models.TextField()


	def __unicode__(self):
		return self.complaintid
	def __str__(self):
		return self.complaintid
	def get_absolute_url(self):
		return reverse("crimefiles:detail", kwargs={"id":self.complaintid})	

class Fir(models.Model):
	firid=models.CharField(max_length=10,primary_key=True)
	signedby= models.CharField(max_length=20)
	content=models.TextField(default="First Information Report")

	def  __unicode__(self):
		return self.firid

	def __str__(self):
		return self.firid

class CopStatus(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	dateofregister=models.DateTimeField()

	def  __unicode__(self):
		return self.firid

	def __str__(self):
		return self.firid

