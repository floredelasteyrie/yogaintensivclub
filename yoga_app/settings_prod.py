from settings import *


DEBUG = TEMPLATE_DEBUG = False
#DATABASE_NAME = ''
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''


#To handle email sending by the server
#EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER
#EMAIL_HOST_PASSWORD
#EMAIL_PORT
#EMAIL_USE_TLS

#persons to be notified if production site raises an exception
ADMINS = (
          ('Stéphanie', 'sdelasteyrie@gmail.com'),
          )

#persons to be notified for broken links
MANAGERS = (
          ('Stéphanie', 'sdelasteyrie@gmail.com'),
          )
SEND_BROKEN_LINK_EMAILS = True
