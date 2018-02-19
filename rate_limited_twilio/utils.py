from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .import defaults


def get_setting(name, use_defaults=True):
    """Retrieves the specified setting from the settings file.
    If the setting is not found and use_defaults is True, then the default
    value specified in defaults.py is used. Otherwise, we raise an
    ImproperlyConfigured exception for the setting.
    """
    if hasattr(settings, name):
        return getattr(settings, name)
    if use_defaults:
        if hasattr(defaults, name):
            return getattr(defaults, name)
    msg = "{0} must be specified in your settings".format(name)
    raise ImproperlyConfigured(msg)
