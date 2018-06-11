#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/superset.db'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

# from flask import redirect
# from flask_appbuilder.security.views import UserDBModelView,AuthDBView
# # from flask_appbuilder.security.sqla.manager import SecurityManager
# from superset.security import SupersetSecurityManager
# from flask_appbuilder.security.views import expose
# # from flask_appbuilder.actions import action
# from flask_appbuilder.security.manager import BaseSecurityManager

# # Create a custom view to authenticate the user
# # AuthDBView=SupersetSecurityManager.authdbview

# class SattvaAuthDBView(AuthDBView):
#     login_template = 'appbuilder/general/security/login_db.html'

#     def __init__(self):
#         print(' ******* init new AuthDBView ')
#         super(SattvaAuthDBView, self)

#     @expose('/login/', methods=['GET', 'POST'])
#     def login(self):
#         print(' *** Sattva login flow ********* ')
#         if g.user is not None and g.user.is_authenticated():
#             return redirect(self.appbuilder.get_url_for_index)
        
#         #temp flow - auto login admin
#         user = self.appbuilder.sm.find_user(username='admin')
#         flash('**** Admin auto logged in ****** ', 'warning')
#         login_user(user, remember=False)
#         return redirect(self.appbuilder.get_url_for_index)

# class SattvaSecurityManager(SupersetSecurityManager):
#     authdbview = SattvaAuthDBView
#     def __init__(self, appbuilder):
#         print(' ******* inside SM ')
#         super(SattvaSecurityManager, self).__init__(appbuilder)

from security import SattvaSecurityManager
CUSTOM_SECURITY_MANAGER = SattvaSecurityManager