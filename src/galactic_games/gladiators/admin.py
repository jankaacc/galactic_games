from django.contrib import admin


from .models import Gladiator
from .models import Profession
from .models import Race
from .models import Species


admin.site.register(Gladiator)
admin.site.register(Profession)
admin.site.register(Race)
admin.site.register(Species)
