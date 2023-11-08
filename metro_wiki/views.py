from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import *
from metro_blog.models import Blog
from django.urls import reverse_lazy
from main_page.utils import DataMixin

# -- Categories --


class Cities(DataMixin, ListView):
    model = City
    template_name = 'wiki/categories/cities.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Города')
        return dict(list(context.items()) + list(c_def.items()))


class Lines(DataMixin, ListView):
    model = Line
    template_name = 'wiki/categories/lines.html'
    context_object_name = 'lines'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all
        context['lines'] = Line.objects.extra(select={'sorted_num': 'CAST(number AS INTEGER)'})\
            .order_by('sorted_num')
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Линий')
        return dict(list(context.items()) + list(c_def.items()))


class Stations(DataMixin, ListView):
    model = Station
    template_name = 'wiki/categories/stations.html'
    context_object_name = 'stations'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all
        context['stations'] = Station.objects.order_by('title', 'line')
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Станций')
        return dict(list(context.items()) + list(c_def.items()))


class Trains(DataMixin, ListView):
    model = Train
    template_name = 'wiki/categories/trains.html'
    context_object_name = 'trains'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Поезда')
        return dict(list(context.items()) + list(c_def.items()))


class Depots(DataMixin, ListView):
    model = Depot
    template_name = 'wiki/categories/depots.html'
    context_object_name = 'depots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Депо')
        return dict(list(context.items()) + list(c_def.items()))


# -- Objects --


class ShowCity(DataMixin, DetailView):
    model = City
    template_name = 'wiki/objects/city.html'
    slug_url_kwarg = 'city_slug'
    context_object_name = 'city'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lines'] = Line.objects.extra(select={'sorted_num': 'CAST(number AS INTEGER)'})\
            .order_by('sorted_num')
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['city'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowLine(DataMixin, DetailView):
    model = Line
    template_name = 'wiki/objects/line.html'
    slug_url_kwarg = 'line_slug'
    context_object_name = 'line'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depot'] = Depot.objects.all()
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['line'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowStation(DataMixin, DetailView):
    model = Station
    template_name = 'wiki/objects/station.html'
    slug_url_kwarg = 'station_slug'
    context_object_name = 'station'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['depot'] = Depot.objects.all()
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['station'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowTrain(DataMixin, DetailView):
    model = Train
    template_name = 'wiki/objects/train.html'
    slug_url_kwarg = 'train_slug'
    context_object_name = 'train'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title=context['train'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowDepot(DataMixin, DetailView):
    model = Depot
    template_name = 'wiki/objects/depot.html'
    slug_url_kwarg = 'depot_slug'
    context_object_name = 'depot'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['depot'])
        return dict(list(context.items()) + list(c_def.items()))


# -- Adding objects --


class AddCity(DataMixin, CreateView):
    form_class = AddCityForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('cities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить город')
        return dict(list(context.items()) + list(c_def.items()))


class AddLine(DataMixin, CreateView):
    form_class = AddLineForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('lines')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить линию')
        return dict(list(context.items()) + list(c_def.items()))


class AddStation(DataMixin, CreateView):
    form_class = AddStationForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('stations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить станцию')
        return dict(list(context.items()) + list(c_def.items()))


class AddTrain(DataMixin, CreateView):
    form_class = AddTrainForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('trains')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить метровагон')
        return dict(list(context.items()) + list(c_def.items()))


class AddDepot(DataMixin, CreateView):
    form_class = AddDepotForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('depots')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить депо')
        return dict(list(context.items()) + list(c_def.items()))


# -- Editing objects --


class UpdateCity(DataMixin, UpdateView):
    model = City
    form_class = AddCityForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'city_slug'

    success_url = reverse_lazy('cities')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать город')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateLine(DataMixin, UpdateView):
    model = Line
    form_class = AddLineForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'line_slug'

    success_url = reverse_lazy('lines')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать линию')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateStation(DataMixin, UpdateView):
    model = Station
    form_class = AddStationForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'station_slug'

    success_url = reverse_lazy('stations')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать станцию')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateTrain(DataMixin, UpdateView):
    model = Train
    form_class = AddTrainForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'train_slug'

    success_url = reverse_lazy('trains')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать поезд')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateDepot(DataMixin, UpdateView):
    model = Depot
    form_class = AddDepotForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'depot_slug'

    success_url = reverse_lazy('depots')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать депо')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()
