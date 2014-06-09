# coding: utf-8

from django.utils.timezone import now
from django.utils.translation import ungettext, ugettext as _
from django.contrib import admin
from subscriptions.models import Subscription
from subscriptions.forms import SubscriptionForm


class SubscriptionAdmin(admin.ModelAdmin):
    form = SubscriptionForm

    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ['created_at']
    actions = ['mark_as_paid']


    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%d inscrição foi marcada como paga.',
            u'%d inscrições foram marcadas como paga.',
            count
        )
        self.message_user(request, msg % count)


    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()


    mark_as_paid.short_description = _(u'Marcar como pago')
    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True



# Register your models here.
admin.site.register(Subscription, SubscriptionAdmin)