# Q7. Create abstract Question with evaluate_answer().
# Derive MCQQuestion, TrueFalseQuestion, and DescriptiveQuestion.
# Implement answer evaluation for each.

from abc import ABC, abstractmethod


class Question(ABC):

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "B":
            return "Correct MCQ Answer"
        return "Wrong Answer"


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "True":
            return "Correct True/False Answer"
        return "Wrong Answer"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) > 20:
            return "Answer Accepted"
        return "Answer Too Short"


print(MCQQuestion().evaluate_answer("B"))
print(TrueFalseQuestion().evaluate_answer("True"))
print(DescriptiveQuestion().evaluate_answer(
    "Python supports object oriented programming."
))