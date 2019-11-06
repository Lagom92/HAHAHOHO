from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg import openapi

schema_url_patterns = [
    path('boards/', include('boards.urls')),
    path('accounts/', include('accounts.urls')),
]
 
schema_view = get_schema_view(
    openapi.Info(
        title="하하호호 Open API",
        default_version='v1',
        description = 
        '''
        하하호호 Open API 문서 페이지 입니다.

        하하호호는 취미 모임을 만들어주는 웹입니다.

        해보고 싶은 취미가 있는데 기회가 없었지 않나요?...

        하고 싶은 취미가 있는데 같이 할 사람 찾기가 어렵나요??...

        저희 하하호호 로 오세요!

        URL: http://54.180.148.99
        
        팀원: 문동식, 이지선, 김훈, 조호근, 양시영, 안현상
        
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ehdtlr9376@gmail.com"),
        license=openapi.License(name="Team 하하호호"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)