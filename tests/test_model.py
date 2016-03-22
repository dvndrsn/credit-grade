import unittest
from unittest.mock import Mock
import numpy as np
from sklearn import linear_model
from credit_grade.common.model import CreditGradeModel

class TestCreditGradeModel(unittest.TestCase):
    def setUp(self):
        # define mock for model to reliably test various edge cases
        mock_model = Mock(spec = linear_model.LinearRegression)
        # mock_model.predict.return_value = 19
        vals = [19, 20, 0, -1, 5, 11]
        mock_model.predict.side_effect = [np.array(v) for v in vals]

        self.cgm = CreditGradeModel(mock_model)

    def test_grade_to_num(self):
        data = np.array(['D5', 'D1', 'C5', 'C1', 'B3', 'A1'])

        expected = [0, 4, 5, 9, 12, 19]
        actual = CreditGradeModel.grade_to_num(data)

        for e, a in zip(actual, expected):
            self.assertEqual(e, a)

    def test_num_to_grade(self):
        data = np.array([-1, 0, 4, 5, 9, 12, 19, 20])

        expected = ['D5', 'D5', 'D1', 'C5', 'C1', 'B3', 'A1', 'A1']
        actual = CreditGradeModel.num_to_grade(data)

        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_predict(self):
        # only keys in dict matter as model is mocked
        data = dict(approved_amount=1,
                    term_months=1,
                    dscr=1,
                    vantage_score=1,
                    fico_score=1,
                    intelliscore=1,
                    bdfs_score=1,
                    annual_revenue=1,
                    business_founding_years=1)

        expected = 'A1'
        actual = self.cgm.predict(data)

        self.assertEqual(expected, actual)

    def test_predict_side_effect(self):
        # only keys in dict matter as model is mocked
        data = dict(approved_amount=1,
                    term_months=1,
                    dscr=1,
                    vantage_score=1,
                    fico_score=1,
                    intelliscore=1,
                    bdfs_score=1,
                    annual_revenue=1,
                    business_founding_years=1)

        expected = ['A1', 'A1', 'D5', 'D5', 'C5', 'B4']

        for e in expected:
            actual = self.cgm.predict(data)

            self.assertEqual(e, actual)

    # process_data, train_model