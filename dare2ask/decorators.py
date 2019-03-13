from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

from dare2ask.models import Lecture

def is_staff(function):
    def wrap(request, *args, **kwargs):
        lecture = Lecture.objects.get(pk=kwargs['lecture_name_slug'])
        if str(self.staff):
            return True
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
