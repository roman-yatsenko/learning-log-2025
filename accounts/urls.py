from django.urls import include, path

app_name = 'accounts'
urlpatterns = [
    # Додати URL авторизації за замовчуванням
    path('', include('django.contrib.auth.urls')),
]
