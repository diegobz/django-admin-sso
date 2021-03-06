from django.conf import settings
from django.utils.translation import ugettext_lazy as _


ASSIGNMENT_ANY = 0
ASSIGNMENT_MATCH = 1
ASSIGNMENT_EXCEPT = 2
ASSIGNMENT_CHOICES = (
    (ASSIGNMENT_ANY, _('Any account from the domain')),
    (ASSIGNMENT_MATCH, _("Only an account that matches a specific username")),
    (ASSIGNMENT_EXCEPT, _("All accounts that don't match a specific username")),
)

DJANGO_ADMIN_SSO_ADD_LOGIN_BUTTON = getattr(
    settings,
    'DJANGO_ADMIN_SSO_ADD_LOGIN_BUTTON',
    True)

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = getattr(
    settings,
    'DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID',
    None)
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = getattr(
    settings,
    'DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET',
    None)

DJANGO_ADMIN_SSO_AUTH_URI = getattr(
    settings,
    'DJANGO_ADMIN_SSO_AUTH_URI',
    'https://accounts.google.com/o/oauth2/auth')
DJANGO_ADMIN_SSO_TOKEN_URI = getattr(
    settings,
    'DJANGO_ADMIN_SSO_TOKEN_URI',
    'https://accounts.google.com/o/oauth2/token')
DJANGO_ADMIN_SSO_REVOKE_URI = getattr(
    settings,
    'DJANGO_ADMIN_SSO_REVOKE_URI',
    'https://accounts.google.com/o/oauth2/revoke')
