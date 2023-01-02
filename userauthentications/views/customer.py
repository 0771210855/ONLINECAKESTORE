from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm
from ..models import Customer,User
from ..forms import customer_registration_form


#---------------------------------------
# Customer Registration  and auto login
#---------------------------------------

class customerSignup(CreateView):
    model = User
    form_class = customer_registration_form
    template_name = "userauthentications/signup.html"
    success_url = reverse_lazy("customer:home")

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect (self.success_url)



#---------------------------------------
# Customer Login
#---------------------------------------
def customerSignin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect ('customer:home')
            else:
                messages.error(request, "Invalid username or password")
    else:
        messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'userauthentications/signin.html', context={"login_form":form})


def logout_request(request):
    logout(request)
    return redirect("seller:signin")