from flask_restful import Resource, reqparse, fields, marshal_with

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('approved_amount', required=True)
parser.add_argument('term_months', required=True)
parser.add_argument('dscr', required=True)
parser.add_argument('vantage_score', required=True)
parser.add_argument('fico_score', required=True)
parser.add_argument('intelliscore', required=True)
parser.add_argument('bdfs_score', required=True)
parser.add_argument('annual_revenue', required=True)
parser.add_argument('business_founding_years', required=True)

response = {
    'credit_grade': fields.String
}

class CreditGradeAPI(Resource):
    ''' REST API for getting a prediction for credit grade from provided data.
    All parameters are mandatory.
    Example usage:
        curl 'http://localhost:5000/CreditGrade?approved_amount=1&term_months=1&dscr=1&vantage_score=1&fico_score=1&intelliscore=1&bdfs_score=1&annual_revenue=1&business_founding_years=1&vantage_score'
    '''

    def __init__(self, **kwargs):
        self.credit_grade_model = kwargs['credit_grade_model']

    @marshal_with(response)
    def get(self):
        args = parser.parse_args()
        print(args)

        credit_grade = self.credit_grade_model.predict(args)
        print(credit_grade)

        return { 'credit_grade' : credit_grade }