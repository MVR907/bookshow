from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.models import Book
from book.form import BookForm
import os


# Create your views here.
def index(request):
	shelf=Book.objects.all()   #only dmin can add any feature 


	return render(request,'index.html',{'book_shelf':shelf})

def upload(request):
	obj=BookForm()

	if request.method=='POST':
		obj=BookForm(request.POST,request.FILES)

		if obj.is_valid():
			obj.save()

			return redirect('index')
		else:
			return HttpResponse("something went wrong,reload <a href='{{url:'index'}}'>reload</a>")
	else:
		return render(request,'upload.html',{'upload_form':obj})

def update(request,book_id):
	book_id=int(book_id)

	try:
		book_select=Book.objects.get(id=book_id)
	except Book.DoesnotExist:
		return redirect('index')
	else:
		book_form=BookForm(request.POST or None,instance=book_select)

		if book_form.is_valid():
			old_image=""
			if book_select.picture:
				old_image=book_select.picture.path
				form=BookForm(request.POST,request.FILES,instance=book_select)
				if form.is_valid():
					if os.path.exists(old_image):
						os.remove(old_image)
						form.save()
			

			
			return redirect('index')
		return render(request,'upload.html',{'upload_form':book_form})



def delete(request,book_id):
	book_id=int(book_id)

	try:
		book_select=Book.objects.get(id=book_id)
	except book.DoesnotExist:
		return redirect('index')
	book_select.delete()
	return redirect('index')



