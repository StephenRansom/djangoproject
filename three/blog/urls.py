from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.posts_by_category, name='posts_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.posts_by_tag, name='posts_by_tag'),
    url(r'^author/(?P<author_slug>[\w-]+)/$', views.posts_by_author, name='posts_by_author'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/$', views.test_redirect, name='test_redirect'),
    url(r'^cookie/$', views.test_cookie, name='cookie'),
    url(r'^track_user/$', views.track_user, name='track_user'),
    url(r'^stop-tracking/$', views.stop_tracking, name='stop_tracking'),
    url(r'^test-delete/$', views.test_delete, name='test_delete'),
    url(r'^test-session/$', views.test_session, name='test_session'),
    url(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    url(r'^access-session-data/$', views.access_session_data, name='access_session_data'),
    url(r'^delete-session-data/$', views.delete_session_data, name='delete_session_data'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    ]

