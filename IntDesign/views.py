from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

from .forms import ContactForm, OrderForm
from .models import Order


# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}

    return render(request, 'index.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def service(request):
    return render(request, 'service.html')


@login_required
def order_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('IntDesign:order_list')
        else:
            return HttpResponseBadRequest('Form is not valid ')
    else:
        form = OrderForm()

    return render(request, 'order_create.html', {'form': form})


@login_required
def order_list(request: HttpRequest) -> HttpResponse:
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def order_edit(request: HttpRequest, pk=int) -> HttpResponse:
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('IntDesign:order_list')
        else:
            return HttpResponseBadRequest('Form is not valid ')
    else:
        form = OrderForm(instance=order)

    return render(request, 'order_create.html', {'form': form})


@login_required
def order_delete(request: HttpRequest, pk=int) -> HttpResponse:
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if request.method == 'POST':
        order.delete()
        return redirect('IntDesign:order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})


@login_required
def blog(request):
    return render(request, 'blog.html')

# def blog_list(request):
#
# def blog_create(request: HttpRequest) -> HttpResponse:
#
# def blog_edit(request: HttpRequest, pk=int) -> HttpResponse:
#
# def blog_delete(request: HttpRequest, pk=int) -> HttpResponse:
