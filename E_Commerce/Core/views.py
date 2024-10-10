from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
from django.db.models import Count
from django.core.serializers import serialize
from Authentication.models import *
from django.urls import reverse


class HomeListView(ListView):
    template_name = 'index.html'
    def get_context_data(self):
        context = {}
        context['contact'] = Contact.objects.get()
        context['carousel'] = Carousel.objects.all()
        context['category'] = Category.objects.annotate(brand_count=Count('subcategory')).order_by('-brand_count', '-name')
        context['category1'] = context['category'].filter(brand_count=0)
        context['brands'] = Brands.objects.all()
        context['products'] = Product.objects.all().order_by('category')
        context['products1'] = Product.objects.all().values('category__name').annotate(Count('category__name')).order_by('-category__name__count')
        context['circle'] = Circle.objects.all()
        return context

    def get(self, request):
        context = self.get_context_data()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'productid' in request.GET:
            if request.user.is_authenticated:
                user = CustomUser.objects.get(id=request.user.id)
                print(int(request.GET.get('productid')),'-----------------')
                product = int(request.GET.get('productid'))
                try:
                    user_product = UserProduct.objects.get(user=user, product=product)
                    user_product.count += 1
                    user_product.save()
                except:
                    user.products.add(int(request.GET.get('productid')))
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'redirect', 'url': reverse('AuthenticationUrls:login')})

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'price_range_min' in request.GET:
            price_min = request.GET.get('price_range_min')
            price_max = request.GET.get('price_range_max')
            products = Product.objects.filter(price__gte=price_min, price__lte=price_max)
                # product['fields'].img_url = product.img.url
            products_json = serialize('json', products)
            return JsonResponse(products_json, safe=False)
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get('query', '')
        context = self.get_context_data()
        context['products'] = Product.objects.filter(name__icontains=query).order_by('?')
        return render(request, self.template_name, context)
    
class CartListView(ListView):
    template_name = 'cart.html'
    def get_context_data(self):
        context = {}
        context['contact'] = Contact.objects.get()
        context['circle'] = Circle.objects.all()
        return context
    def get(self, request):
        context = self.get_context_data()
        context['user'] = CustomUser.objects.get(id=request.user.id)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            user = CustomUser.objects.get(id=int(request.user.id))
            product = int(request.GET.get('prod_id'))
            user_product = UserProduct.objects.get(user=user, product=product)
            user_product.count = request.GET.get('prod_count')
            user_product.save()
            return JsonResponse({'id': user_product.product_id})
        return render(request, self.template_name, context)