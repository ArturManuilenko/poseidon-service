from typing import Tuple

from api_utils.api_resource.api_resource import ApiResource
from flask import render_template

from src.conf.poseidon__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/templates')
@web_sdk.html_view(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_list_template(api_resource: ApiResource) -> Tuple[str, int]:
    res = self_api.request_get('/templates', q={'limit': api_resource.pagination.limit, 'offset': api_resource.pagination.offset})

    return render_template(
        'list_templates.html',
        active="templates",
        title='Templates',
        data=res.payload,
        pagination=api_resource.pagination.mk_sqlalchemy_pagination(query=None, total=res.total_count, items=res.payload),
    ), 200
