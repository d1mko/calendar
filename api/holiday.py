from flask_restful import Resource


class Holiday(Resource):

    def get(self, year, month, day):
        return {'test': 'test'}
