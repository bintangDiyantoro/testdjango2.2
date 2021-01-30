from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Artikel
from .forms import ArtikelForm


class Index(ListView):
    model = Artikel
    extra_context = {
        'title': 'Selamat datang di blog saya',
        'message': 'Selamat menikmati data yang kami sajikan'
    }
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('keyword'):
            self.queryset = self.model.objects.filter(
                judul__contains=self.request.GET['keyword'])
            print(self.request.GET['keyword'])
            for i in self.queryset:
                print(i)
        return super().get_queryset()


class Detail(DetailView):
    model = Artikel

    def get_object(self, *args, **kwargs):
        self.extra_context = {
            'title': self.model.objects.get(slug=self.kwargs['slug']), 'message': 'Selamat menikmati data secara detail', }
        return super().get_object()


class Create(CreateView):
    form_class = ArtikelForm
    extra_context = {
        'title': 'Tambah artikel baru',
        'message': 'Selamat menginput'
    }
    template_name = 'blog/artikel_form.html'
    # fields = [
    #     'judul', 'isi', 'penulis',
    # ]


class Update(UpdateView):
    model = Artikel
    fields = ('judul', 'isi', 'penulis', 'photo')

    def get_context_data(self):
        self.extra_context = {
            'title': 'Update {}'.format(self.model.objects.get(slug=self.kwargs['slug']).judul),
            'message': 'Selamat menginput'
        }
        return super().get_context_data()


class Delete(DeleteView):
    model = Artikel

    def get_success_url(self):
        return reverse('blog:index')
