from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views
from Movies.views import MovieChangeViewSet
from rest_framework.routers import DefaultRouter

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

router = DefaultRouter()
router.register(r'movies', MovieChangeViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ShopSense.views.home', name='home'),
    # url(r'^ShopSense/', include('ShopSense.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', HomePageView.as_view(),name="about_page"),
    url(r'^api-token-auth/', views.obtain_auth_token),
#     url(r'^$', MovieListViewSet.as_view(), name="movie_lisitng"),
#     url(r'^set_lang/(?P<lang_code>\w+)/$', SetLangView.as_view(),name="set_lang"),
)

urlpatterns = urlpatterns + router.urls