from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Band, Member
from .forms import BandContactForm, BandForm, MemberForm


def home(request):
    return render(request, 'home.html')


def band_list(request):
    """ A view of all bands. """
    bands = Band.objects.all()
    search = request.GET.get('search_box')
    if search:
        bands = bands.filter(name__icontains=search)
    return render(request, 'bands/band_list.html', {'bands': bands})


def my_send_email(request):
    email = request.POST
    # import ipdb; ipdb.set_trace()
    pass


def band_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Implementar o send_email
            return redirect('home')
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})


def band_contact_as_p(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact_as_p.html', {'form': form})


def band_contact_as_table(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact_as_table.html', {'form': form})


def band_contact_bootstrap(request):
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact_bootstrap.html', {'form': form})


def band_contact_crispy(request):
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact_crispy.html', {'form': form})


def band_detail(request, pk):
    """ A view of all members by bands. """
    band = Band.objects.get(pk=pk)
    members = Member.objects.all().filter(band=band)
    context = {'members': members, 'band': band}
    return render(request, 'bands/band_detail.html', context)


def band_create(request):
    ''' https://coderwall.com/p/o8tida/better-way-to-initialize-django-forms '''
    form = BandForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Process the data in form.cleaned_data
        form.save()
        return HttpResponseRedirect(resolve_url('bands'))
    return render(request, 'bands/band_create.html', {'form': form})


class BandCreate(CreateView):
    model = Band
    form_class = BandForm
    template_name = 'bands/band_form.html'
    success_url = reverse_lazy('bands')


# def members(request):
#     return render(request, 'bands/member_list.html')


class MemberList(ListView):
    model = Member
    # template_name =
    # context_object_name =
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MemberList, self).get_context_data(**kwargs)
        context['form'] = MemberForm()
        return context


def members_vue(request):
    form = MemberForm()
    context = {'form': form}
    return render(request, 'bands/members_vue.html', context)


def members_add_ajax(request):
    data = request.POST
    import ipdb
    ipdb.set_trace()


def members_json(request):
    pass


class MemberCreate(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'bands/member_form.html'
    success_url = reverse_lazy('bands')


@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bands/protected.html', {'current_user': request.user})


def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
