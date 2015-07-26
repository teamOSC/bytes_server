from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'staypay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'bytes.views.mainPage'),
    url(r'^outlets/create/$', 'bytes.views.createOutlets'),
    url(r'^outlets/fetch/$', 'bytes.views.getOutlets'),
    url(r'^outlets/info/$', 'bytes.views.getOutletInfo'),
    url(r'^outlets/create_info/$', 'bytes.views.createOutletInfo'),
    url(r'^outlets/create/form/$', 'bytes.views.createForm'),
    url(r'^outlets/create_info/form/$', 'bytes.views.createInfoForm'),
    url(r'^outlets/billing/$', 'bytes.views.billing'),
    url(r'^outlets/orders/(?P<outlet_id>[0-9]+)/$', 'bytes.views.dashboardAPI'),
    url(r'^outlets/notify/$', 'bytes.views.notify'),
)
