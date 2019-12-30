

from django.contrib import admin
from functools import update_wrapper
from django.views.generic import RedirectView
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.urls import include, path, re_path
from django.contrib.contenttypes import views as contenttype_views
from django.contrib.auth.views import redirect_to_login


class BlogAdminSite(admin.AdminSite):
    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                if request.path == reverse('admin:logout', current_app=self.name):
                    index_path = reverse('admin:index', current_app=self.name)
                    return HttpResponseRedirect(index_path)
                # change relogin router path after logout
                return redirect_to_login(request.get_full_path(), '/user/login.html')
            return view(request, *args, **kwargs)
        if not cacheable:
            inner = never_cache(inner)
        if not getattr(view, 'csrf_exempt', False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)

    def get_urls(self):
        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)
        urlpatterns = [
            path('', wrap(self.index), name='index'),
            # change router path of login page
            path('login/', RedirectView.as_view(url='/user/login.html')),
            path('logout/', wrap(self.logout), name='logout'),
            path('password_change/', wrap(self.password_change, cacheable=True), name='password_change'),
            path('password_change/done/', wrap(self.password_change_done, cacheable=True), name='password_change_done'),
            path('jsi18n/', wrap(self.i18n_javascript, cacheable=True), name='jsi18n'),
            path('r/<int:content_type_id>/<path:object_id>/', wrap(contenttype_views.shortcut), name='view_on_site'),
        ]
        valid_app_labels = []
        for model, model_admin in self._registry.items():
            urlpatterns += [
                path('%s%s' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)
        if valid_app_labels:
            regex = r'^(?P<app_label>'+'|'.join(valid_app_labels)+')/$'
            urlpatterns += [
                re_path(regex, wrap(self.app_index), name='app_list'),
            ]
        return urlpatterns