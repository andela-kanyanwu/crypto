from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        data = request.POST.get('data', False)
        key = request.POST.get('key', False)
        encoded_data = request.POST.get('encoded_data', False)
        