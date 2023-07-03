from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from restaurant.models import Cook, Dish, DishType
from restaurant.forms import (
    DishSearchForm,
    DishForm,
    CookSearchForm,
    CookCreationForm,
    CookExperienceUpdateForm,
)


@login_required
def index(request) -> render:
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_types_list"
    template_name = "restaurant/dish_types_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = DishType.objects.all()

        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-types-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-types-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish-types-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Dish.objects.all().select_related("dish_type")

        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dishes-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CookSearchForm(initial={"username": username})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Cook.objects.all()

        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])

        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__cooks")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:cooks-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy(LoginRequiredMixin, "restaurant:cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:cooks-list")


class ToggleAssignToDishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        cook = get_object_or_404(Cook, id=request.user.id)
        dish = get_object_or_404(Dish, id=pk)

        if dish in cook.dishes.all():
            cook.dishes.remove(dish)
        else:
            cook.dishes.add(dish)

        return HttpResponseRedirect(reverse_lazy("restaurant:dish-detail", args=[pk]))
