from django.conf.urls import url

from dojo.finding import views

urlpatterns = [
    #  findings
    url(r'^finding$', views.open_findings, {'view': 'All'},
        name='all_findings'),
    url(r'^finding$', views.open_findings,
        name='findings'),
    url(r'^finding/bulk$', views.finding_bulk_update_all,
        name='findings_bulk_all'),
    url(r'^product/(?P<pid>\d+)/finding/bulk_product$', views.finding_bulk_update_all,
        name='findings_bulk_all_product'),
    url(r'^finding/open$', views.open_findings,
        name='open_findings'),
    url(r'^product/(?P<pid>\d+)/finding/open$', views.open_findings,
        name='product_open_findings'),
    url(r'^product/(?P<pid>\d+)/finding/all$', views.open_findings, {'view': 'All'},
        name='product_all_findings'),
    url(r'^product/(?P<pid>\d+)/finding/closed$', views.closed_findings,
        name='product_closed_findings'),
    url(r'^product/(?P<pid>\d+)/finding/accepted$', views.accepted_findings,
        name='product_accepted_findings'),
    url(r'^finding/closed$', views.closed_findings,
        name='closed_findings'),
    url(r'^finding/accepted', views.accepted_findings,
        name='accepted_findings'),
    url(r'^finding/(?P<fid>\d+)$', views.view_finding,
        name='view_finding'),
    url(r'^finding/(?P<fid>\d+)/edit$',
        views.edit_finding, name='edit_finding'),
    url(r'^finding/(?P<fid>\d+)/touch',
        views.touch_finding, name='touch_finding'),
    url(r'^finding/(?P<fid>\d+)/request_review',
        views.request_finding_review, name='request_finding_review'),
    url(r'^finding/(?P<fid>\d+)/review',
        views.clear_finding_review, name='clear_finding_review'),
    url(r'^finding/(?P<fid>\d+)/delete$',
        views.delete_finding, name='delete_finding'),
    url(r'^finding/(?P<fid>\d+)/apply_cwe$',
        views.apply_template_cwe, name='apply_template_cwe'),
    url(r'^finding/(?P<fid>\d+)/mktemplate$', views.mktemplate,
        name='mktemplate'),
    url(r'^finding/(?P<fid>\d+)/find_template_to_apply', views.find_template_to_apply,
        name='find_template_to_apply'),
    url(r'^finding/(?P<tid>\d+)/(?P<fid>\d+)/choose_finding_template_options', views.choose_finding_template_options,
        name='choose_finding_template_options'),
    url(r'^finding/(?P<fid>\d+)/(?P<tid>\d+)/apply_template_to_finding',
        views.apply_template_to_finding, name='apply_template_to_finding'),
    url(r'^finding/(?P<fid>\d+)/close$', views.close_finding,
        name='close_finding'),
    url(r'^finding/(?P<fid>\d+)/defect_review',
        views.defect_finding_review, name='defect_finding_review'),
    url(r'^finding/(?P<fid>\d+)/open', views.reopen_finding,
        name='reopen_finding'),
    url(r'^finding/(?P<fid>\d+)/manage_images', views.manage_images,
        name='manage_images'),
    url(r'^finding/image/(?P<token>[^/]+)$', views.download_finding_pic,
        name='download_finding_pic'),
    url(r'^finding/(?P<fid>\d+)/merge$',
        views.merge_finding_product, name='merge_finding'),
    url(r'^product/(?P<pid>\d+)/merge$', views.merge_finding_product,
        name='merge_finding_product'),

    # stub findings
    url(r'^stub_finding/(?P<tid>\d+)/add$',
        views.add_stub_finding, name='add_stub_finding'),
    url(r'^stub_finding/(?P<fid>\d+)/promote',
        views.promote_to_finding, name='promote_to_finding'),
    url(r'^stub_finding/(?P<fid>\d+)/delete$',
        views.delete_stub_finding, name='delete_stub_finding'),

    # template findings

    url(r'^template$', views.templates,
        name='templates'),
    url(r'^template/add$', views.add_template,
        name='add_template'),
    url(r'^template/(?P<tid>\d+)/edit$',
        views.edit_template, name='edit_template'),
    url(r'^template/(?P<tid>\d+)/delete',
        views.delete_template, name='delete_template'),
]
