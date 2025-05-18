from flask_restx import Resource, reqparse

from src.ext import api
from src.models import Question


@api.route("/questions/<int:question_id>")
class QuestionAPI(Resource):
    def get(self, question_id):
        question = Question.query.filter_by(id=question_id).first()
        paired_question = Question.query.filter(Question.pair_number == question.pair_number, Question.id != question_id).first()

        next_question1 = Question.query.filter_by(pair_number=question.next_pair_number).first()
        next_question2 = Question.query.filter_by(pair_number=paired_question.next_pair_number).first()

        response = [
            {
                "question": question.text,
                "next_question_id": next_question1.id if next_question1 else None,
                "identified_plant_id": question.plant_id,
            },
            {
                "question": paired_question.text,
                "next_question_id": next_question2.id if next_question2 else None,
                "identified_plant_id": paired_question.plant_id,
            }
        ]
        return response, 200