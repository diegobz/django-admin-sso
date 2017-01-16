from django.conf import settings
from django.utils.translation import ugettext_lazy as _


ASSIGNMENT_ANY = 0
ASSIGNMENT_MATCH = 1
ASSIGNMENT_EXCEPT = 2
ASSIGNMENT_CHOICES = (
    (ASSIGNMENT_ANY, _('any')),
    (ASSIGNMENT_MATCH, _("matches")),
    (ASSIGNMENT_EXCEPT, _("don't match")),
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

# Automatically create user object on first login
DJANGO_ADMIN_SSO_AUTO_CREATE_USER = getattr(
    settings,
    'DJANGO_ADMIN_SSO_AUTO_CREATE_USER',
    False)

# Whether users created on first login should be set as superuser
DJANGO_ADMIN_SSO_AUTO_SUPERUSER = getattr(
    settings,
    'DJANGO_ADMIN_SSO_AUTO_SUPERUSER',
    False)

# Add automatically created user to specific Groups. Groups are created if they
# do not exist yet.
DJANGO_ADMIN_SSO_AUTO_USER_GROUPS = getattr(
    settings,
    'DJANGO_ADMIN_SSO_AUTO_USER_GROUPS',
    [])
