from django.shortcuts import render
from .models import TableData
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    template_name = 'table/table.html'
    table_data_all = TableData.objects.all().order_by('user_id')

    query=request.GET.get("q")

    if query:
        table_data_all = table_data_all.filter(
            Q(username__icontains=query) |
            Q(user_id__icontains=query) |
            Q(contact__icontains=query) |
            Q(primary_role__icontains=query) |
            Q(additional_role__icontains=query) |
            Q(school_id__icontains=query) |
            Q(school_name__icontains=query) |
            Q(block_name__icontains=query) |
            Q(district_name__icontains=query) |
            Q(dise_code__icontains=query)
            ).distinct()

    paginator = Paginator(table_data_all, 20)

    page_number = request.GET.get('page')
    table_data_all = paginator.get_page(page_number)

    context = {'table_data':table_data_all}

    return render(request,template_name,context)