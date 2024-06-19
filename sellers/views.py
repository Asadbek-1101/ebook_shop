from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.permissons import SellerRequiredMixin
from .forms import CreateBookForm
from users.models import Books
from users.forms import ProfileEditForm

class SellerDashboardView(SellerRequiredMixin, View):
    def get(self, request):
        return render(request, 'sellers/dashboard.html')

class SellerProfileView(SellerRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')


class CreateBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = CreateBookForm()
        return render(request, 'sellers/create_book.html', {'form': form})

    def post(self, request):
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            book = Books(
                name=name,
                author=author,
                category=category,
                price=price,
                quantity=quantity,
                description=description,
                image=image
            )
            book.save()

            return redirect('sellers:profile')

        return render(request, 'sellers/create_book.html', {'form': form})


class EditProfileView(SellerRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'sellers/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('sellers:profile')

        form = ProfileEditForm(instance=request.user)
        return render(request, 'sellers/edit_profile.html', {'form': form})



def BookDeletedView(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return redirect('/')
