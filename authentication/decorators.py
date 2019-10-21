from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def student_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    """
    decorator for views that check that the logged in user in a student ,
    redirect to the log-in page if neccessary
    :param function:
    :param redirect_field_name:
    :param login_url:
    :return:
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student or u.is_superuser,
        login_url = login_url,
        redirect_field_name= redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def lecturer_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    """
        decorator for views that check that the logged in user in a student ,
        redirect to the log-in page if neccessary
        :param function:
        :param redirect_field_name:
        :param login_url:
        :return:
        """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_lecturer or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator