from rest_framework import routers

from whyitsuxapp import viewsets

router = routers.SimpleRouter()
router.register(r'categories', viewsets.Categories, base_name="category")
router.register(r'topics', viewsets.Topics)
router.register(r'comments', viewsets.Comments)
router.register(r'posts', viewsets.Posts)
router.register(r'tags', viewsets.Tags)

urlpatterns = router.urls
