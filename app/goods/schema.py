from app.common.models.goods import Goods, GoodsType
from patch import fields


class GoodsTypeSchema(GoodsType.schema_class):
    class Meta:
        fields = ("id", "name")


class GoodsSchema(Goods.schema_class):
    type_name = fields.String()

    class Meta:
        fields = ("id", "name", "type_id", "type_name", "cost")
