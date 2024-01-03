from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extentions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleListEvent(EventsResource):
    def event_get_count(self):
        return {'count': Article.query.count()}


class ArticleDetailsEvent(EventsResource):
    def event_get_count_by_author(self, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailsEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


