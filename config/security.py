from flask import redirect, g, flash, request
from flask_appbuilder.security.views import UserDBModelView,AuthDBView
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import expose
from flask_appbuilder.security.manager import BaseSecurityManager
from flask_login import login_user, logout_user


class CustomAuthDBView(AuthDBView):
    login_template = 'appbuilder/general/security/login_db.html'

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        if request.args.get('username') is not None:
            user = self.appbuilder.sm.find_user(username=request.args.get('username'))
            flash('Admin auto logged in', 'success')
            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)
        elif g.user is not None and g.user.is_authenticated():
            return redirect(self.appbuilder.get_url_for_index)
        else:
            flash('Unable to auto login', 'warning')
            return super(CustomAuthDBView,self).login()

class CustomSecurityManager(SupersetSecurityManager):
    authdbview = CustomAuthDBView
    def __init__(self, appbuilder):
        super(CustomSecurityManager, self).__init__(appbuilder)

