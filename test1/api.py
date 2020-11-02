from rest_framework import routers
from users import views as myapp_views

router = routers.DefaultRouter()
router.register(r'user', myapp_views.UserViewset)
