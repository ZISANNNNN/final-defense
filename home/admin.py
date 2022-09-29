from django.contrib import admin
from .models import job
from .models import all_cv
from .models import edit_profile_model
from .models import edit_profile_picture
from .models import wishlist
from .models import apply_for_job

admin.site.register(job)
admin.site.register(all_cv)
admin.site.register(edit_profile_model)
admin.site.register(edit_profile_picture)
admin.site.register(wishlist)
admin.site.register(apply_for_job)

