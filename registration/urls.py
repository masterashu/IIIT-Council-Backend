from django.urls import path
from registration.views import LoginView, LogoutView, PasswordResetView as PRV, PasswordResetDoneView as PRDV
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from registration.views import PasswordChangeView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/', PRV.as_view(), name='password_reset'),
    path('password-reset/done/', PRDV.as_view(), name='password_reset_done'),
]
