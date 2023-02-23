from django.shortcuts import redirect
from django.urls import reverse

class Routing_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        from django.urls import resolve

#     current_namespace = resolve(request.path_info).namespace
#     # do something with current_namespace

        

        if request.user.is_authenticated:
            if request.user.is_seller is False:
                if "seller" in request.path:
                    return redirect(reverse('customer:home'))
            if request.user.is_seller is True:
                if "seller" not in request.path:
                    return redirect(reverse('seller:seller_home'))
                
        response = self.get_response(request)
        return response
