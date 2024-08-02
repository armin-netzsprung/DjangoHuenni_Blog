"""
WSGI config for DjangoHuenni_Blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os, sys

# ### AH
# exec(open("./.env/bin/activate").read(), {'__file__': "./env/bin/activate"})
# sys.path.append('./env/core/core')
# sys.path.append('./.env/lib64/python3.12/site-packages')

# ###

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoHuenni_Blog.settings')

application = get_wsgi_application()
