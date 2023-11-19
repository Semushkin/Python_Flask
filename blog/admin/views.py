# from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from flask_admin import AdminIndexView, expose


# admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')


class CustomAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class CustomAdminIndexView(AdminIndexView):

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth.login'))
        return super().index()


class TagAdminView(CustomAdminView):
    column_searchable_list = ('name', )
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomAdminView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author_id', )


class UserAdminView(CustomAdminView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    can_delete = False
    can_edit = True
    can_view_details = False
    can_create = False
    column_editable_list = ('email',)
