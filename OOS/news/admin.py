from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Articles
from .models import Contact

admin.site.register(Articles)

def export_to_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active

    headers = ['last_name', 'first_name', 'middle_name', 'email', 'organization', 'phone', 'text']
    ws.append(headers)

    for obj in queryset:
        row = [obj.last_name, obj.first_name, obj.middle_name, obj.email, obj.organization, obj.phone, obj.text]
        ws.append(row)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=contacts.xlsx'

    wb.save(response)
    return response

class ContactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'email', 'organization', 'phone', 'text']
    actions = [export_to_excel]

admin.site.register(Contact, ContactAdmin)


