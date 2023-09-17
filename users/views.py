import os

from django.contrib.sites.shortcuts import get_current_site
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from django.core.mail import send_mail

from config import settings
from users.forms import UserForm, UserProfileForm, VerificationForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    queryset = User.objects.last()

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.set_unusable_password()

            # Send an email to the user with the token:
            # current_site = get_current_site(request)
            # print('current_site', current_site)
            new_user.save()

            verification_key = urlsafe_base64_encode(force_bytes(new_user.pk))
            # verification_key = new_user.pk
            print('RegisterView: verification_key', verification_key, 'new_user.pk', new_user.pk)
            send_mail(
                subject='Верификация почты',
                message=f'перейдите по ссылке: '
                        f'http://127.0.0.1:8000/users/verification?verification_key={verification_key}\n ',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[new_user.email]
            )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification(request):
    key_data = request.GET.get('verification_key')
    template = 'users/verification.html'
    verification_key = int(urlsafe_base64_decode(key_data).decode())
    print(key_data, '=', verification_key)

    if request.method == 'POST':
        form = VerificationForm(request.POST)  # or None)
        if form.is_valid():
            user = User.objects.get(pk=verification_key)
            user.is_verified = True
            user.is_active = True
            user.save()
            return redirect(reverse('catalog:index'))
    form = VerificationForm(request.POST or None)
    context = {'form': form}
    return render(request, template, context)


# class VerificationView(TemplateView):
#     template_name = 'users/verification.html'

#     model = User
#     template_name = 'users/verification.html'
#     success_url = reverse_lazy('catalog:index')
#     context_object_name = 'pk'
#
#     # queryset = User.objects.get(verification_key=4444)
#
#     verification_key = request.parse_header_parameters(['verification_key'])
#
#     usr = User.objects.get(verification_key=verification_key)
#     usr.is_active = True
