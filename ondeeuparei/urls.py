from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ondeeuparei.core.views.login', name='login'),
    url(r'^board/create/', 'ondeeuparei.core.views.create', name='create'),
    url(r'^board/', 'ondeeuparei.core.views.board', name='board'),
    url(r'^logout', 'ondeeuparei.core.views.logout', name='logout'),
    url(r'', include('social_auth.urls')),
    # Examples:
    # url(r'^$', 'ondeeuparei.views.home', name='home'),
    # url(r'^ondeeuparei/', include('ondeeuparei.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
