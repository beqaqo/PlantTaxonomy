from flask_restx import Resource, reqparse
from sqlalchemy import or_

from src.ext import api
from src.models import Plant

parser = reqparse.RequestParser()
parser.add_argument("page", type=int, default=1, required=True)
parser.add_argument("search", type=str, required=False)
parser.add_argument("sort", type=str, required=False)

limit = 20


@api.route("/plant")
class PlantAPI(Resource):
    @api.expect(parser)
    def get(self, ):
        args = parser.parse_args()
        page = args['page']
        search = args['search']
        sort = args['sort']

        plants = Plant.query

        if search:
            plants = plants.filter(
                or_(
                    Plant.name.ilike(f"%{search}%"),
                    Plant.eng_name.ilike(f"%{search}%"),
                    Plant.family_name.ilike(f"%{search}%"),
                    Plant.family_name_geo.ilike(f"%{search}%")
                )
            )

        if sort == "asc":
            plants = plants.order_by(Plant.family_name.asc())
        elif sort == "desc":
            plants = plants.order_by(Plant.family_name.desc())

        total_items = plants.count()

        plants = plants.limit(limit).offset((page - 1) * limit)

        plants_json = [{"id": plant.id,
                        "name": plant.name,
                        "eng_name": plant.eng_name,
                        "family_name": plant.family_name,
                        "family_name_geo": plant.family_name_geo,
                        "description": plant.description,
                        "image": plant.image} for plant in plants]

        response = {
            "plants": plants_json,
            "pagination": {
                "currentPage": page,
                "totalPages": (total_items // limit) + (1 if total_items % limit > 0 else 0),
                "pageSize": limit,
                "totalItems": total_items,
            }
        }

        return response, 200


@api.route("/plant/<int:id>")  # Route for a specific plant
class PlantAPI(Resource):
    def get(self, id):
        plant = Plant.query.get_or_404(id)
        plants_json = [{"id": plant.id,
                        "name": plant.name,
                        "eng_name": plant.eng_name,
                        "family_name": plant.family_name,
                        "family_name_geo": plant.family_name_geo,
                        "description": plant.description,
                        "image": plant.image}]
        return plants_json, 200