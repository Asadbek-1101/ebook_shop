from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Books, Category, Cart
from .forms import LoginForm, RegisterForm, ProfileEditForm, ClientRegistrationForm
from .permissons import AdminRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        books = Books.objects.filter(in_stock=True)
        category = Category.objects.all()
        count = Cart.objects.count()
        return render(request, 'users/home.html', {"books": books, 'count':count, "category": category})



class BooksDetailView(View):
    def get(self, request, book_id):
        cart = Cart.objects.all()
        count = Cart.objects.count()
        book = get_object_or_404(Books, id=book_id)
        return render(request, 'users/batafsil.html', {'cart':cart, 'count':count, "book": book})

    def post(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(books=book).exists():
            cart = Cart.objects.filter(books=book).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.books = book
            cart.quantity = quantity
            cart.save()
        return redirect('/')

class CartDetailView(View):
    def get(self, request):
        count = Cart.objects.count()
        cart = Cart.objects.all()
        return render(request, 'users/cart_detail.html', {'count':count, "cart": cart})


class CategoryView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        books = category.books.all()
        count = Cart.objects.count()
        return render(request, 'users/all_books.html', {'count':count, "books": books})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')
        return render(request, 'users/register.html', {'form': form})

class ProfileView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')

class EditProfileView(AdminRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})

class DashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'sellers/dashboard.html')


class ClientSignUpView(View):
    def get(self, request):
        form = ClientRegistrationForm()
        return render(request, 'users/client_signup.html', {'form': form})

    def post(self, request):
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'users/client_signup.html', {'form': form})









