from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv


# Create your views here.

def post_list(request):
	flag = 0
	input_file = csv.DictReader(open("/home/indictrans/prashant_workspace/campus_management/student_profile/login.csv"))
	if request.POST.get('username'):
		for row in input_file:
			if row == {'username':request.POST.get('username'),'password':request.POST.get('password')}:
				request.session['name'] = request.POST.get('username')
				request.session['password'] = request.POST.get('password')
				return redirect(access_session)
	
	return render(request, 'student_profile/login.html', {})

def access_session(request):
	input_file = csv.DictReader(open("/home/indictrans/prashant_workspace/campus_management/student_profile/profile.csv"))
	for row in input_file:
		if row.get('username') == request.session.get('name'):
			return render(request, 'student_profile/student_profile.html', {"firstname":row.get('firstname'),"city":row.get('city'),"taluka":row.get('taluka'),"district":row.get('district')})

def file_crud_operation(request):
	lines = list()
	input_file = csv.DictReader(open("/home/indictrans/prashant_workspace/campus_management/student_profile/mycsv.csv"))
	return render(request, 'student_profile/show_fees.html', {"input_file":input_file})
	
def record_delete(request,username):
	lines = list()
	input_file = csv.DictReader(open("/home/indictrans/prashant_workspace/campus_management/student_profile/mycsv.csv"))
	for row in input_file:
		if row.get('username') != str(username):
			lines.append(row)
	keys = lines[0].keys()
	with open('/home/indictrans/prashant_workspace/campus_management/student_profile/mycsv.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(lines)
		return redirect(file_crud_operation)

def record_add(request,username):
	lines = list()
	input_file = csv.DictReader(open("/home/indictrans/prashant_workspace/campus_management/student_profile/mycsv.csv"))
	for row in input_file:
		lines.append(row)
	
	keys = lines[0].keys()
	with open('/home/indictrans/prashant_workspace/campus_management/student_profile/mycsv.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(lines)
		return redirect(file_crud_operation)