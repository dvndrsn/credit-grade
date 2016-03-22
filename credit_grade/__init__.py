# this file contains your app and routes
from flask import Flask
from flask_restful import Api
from credit_grade.resources.api import CreditGradeAPI
from credit_grade.common.model import CreditGradeModel

model_data_file = 'sample_data.csv'
model_persist_file = 'model.pkl'

def init_model(filename):
    x_data, y_data = CreditGradeModel.process_data_from_file(filename)
    model = CreditGradeModel.train_model(x_data, y_data)
    CreditGradeModel.save_model(model, model_persist_file)

    return model

def init_resources(model):
    app = Flask('credit_grade')
    api = Api(app)

    api.add_resource(CreditGradeAPI, '/', '/CreditGrade',
                    resource_class_kwargs={ 'credit_grade_model': model } )

    return app, api

try:
    model = CreditGradeModel.load_model(model_persist_file)
except:
    model = init_model(model_data_file)

cg_model = CreditGradeModel(model)

app, api = init_resources(cg_model)
