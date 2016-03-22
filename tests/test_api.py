import unittest
from unittest.mock import Mock
from credit_grade import app, init_resources
from credit_grade.resources.api import CreditGradeAPI
from credit_grade.common.model import CreditGradeModel
import json

class TestCreditGradeAPI(unittest.TestCase):

    def setUp(self):
        mock_credit_grade_model = Mock(spec = CreditGradeModel)
        mock_credit_grade_model.predict.return_value = 'A1'

        app, api = init_resources(mock_credit_grade_model)
        app.config['TESTING'] = True

        self.app = app.test_client()

    @staticmethod
    def get_json_response(app, data):
        response = app.get('/CreditGrade', \
                            data=data)
        return json.loads(response.data.decode('utf-8'))

    def test_request_ok(self):
        data = dict(approved_amount=1,
                    term_months=1,
                    dscr=1,
                    vantage_score=1,
                    fico_score=1,
                    intelliscore=1,
                    bdfs_score=1,
                    annual_revenue=1,
                    business_founding_years=1)

        actual = TestCreditGradeAPI.get_json_response(self.app, data)
        expected = {'credit_grade': 'A1'}

        self.assertEqual(actual, expected)

    def test_missing_field(self):
        # dict missing required field approved_amount
        data = dict(#approved_amount=1,
                    term_months=1,
                    dscr=1,
                    vantage_score=1,
                    fico_score=1,
                    intelliscore=1,
                    bdfs_score=1,
                    annual_revenue=1,
                    business_founding_years=1)

        actual = TestCreditGradeAPI.get_json_response(self.app, data)
        missing = 'Missing required parameter in the JSON body or the post body or the query string'
        expected = { 'message' : { 'approved_amount' : missing } }

        self.assertEqual(actual, expected)

    def test_all_missing_field(self):
        # dict is empty
        data = dict()

        actual = TestCreditGradeAPI.get_json_response(self.app, data)

        missing = 'Missing required parameter in the JSON body or the post body or the query string'
        expected = {'message':
                    {'intelliscore': missing,
                     'approved_amount': missing,
                     'dscr': missing,
                     'term_months': missing,
                     'annual_revenue': missing,
                     'bdfs_score': missing,
                     'vantage_score': missing,
                     'fico_score': missing,
                     'business_founding_years': missing }
        }

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()