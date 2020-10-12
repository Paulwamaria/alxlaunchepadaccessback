from django.shortcuts import render

# Create your views here.
def index(request):
   """This view will expose the homepage endpoint."""
    title = "Alpdaccessor"
    greet = "Welcome to Alxlpdaccessor API home page."
    context = {
        "title":title,
        "greet":greet,
    }
    return render(request,'accounts/index.html',context)
