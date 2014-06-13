from django.contrib import admin
from core.models import Speaker, Contact, Talk, Media



class MediaInLine(admin.TabularInline):
    model = Media
    extra = 1

class TalkAdmin(admin.ModelAdmin):
    inlines = [MediaInLine,]



class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
