from flask import redirect, g, flash
from flask_appbuilder.security.views import UserDBModelView,AuthDBView
# from flask_appbuilder.security.sqla.manager import SecurityManager
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import expose
# from flask_appbuilder.actions import action
from flask_appbuilder.security.manager import BaseSecurityManager
from flask_login import login_user, logout_user

# Create a custom view to authenticate the user
# AuthDBView=SupersetSecurityManager.authdbview
print('****** inside security.....')

class SattvaAuthDBView(AuthDBView):
    login_template = 'appbuilder/general/security/login_db.html'

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        print(' *** Sattva login flow ********* ')
        if g.user is not None and g.user.is_authenticated():
            return redirect(self.appbuilder.get_url_for_index)
        
        #temp flow - auto login admin
        user = self.appbuilder.sm.find_user(username='admin')
        flash('**** Admin auto logged in ****** ', 'warning')
        login_user(user, remember=False)
        return redirect(self.appbuilder.get_url_for_index)

class SattvaSecurityManager(SupersetSecurityManager):
    authdbview = SattvaAuthDBView
    def __init__(self, appbuilder):
        print(' ******* inside SM ')
        super(SattvaSecurityManager, self).__init__(appbuilder)

