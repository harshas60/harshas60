import random
import re
import json
import os

class Quiz:
    def __init__(self):
        self.questions = []
        self.scores = []
        self.load_questions()
    
    def load_questions(self):
        # Load questions from a JSON file or define them here
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
                "answer": "A"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
                "answer": "B"
            },
            {
                "question": "Who is known as the Father of the Nation in India?",
                "options": ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) Subhas Chandra Bose", "D) Sardar Vallabhbhai Patel"],
                "answer": "A"
            },
            {
                "question": "Who is the author of the novel 'To Kill a Mockingbird'?",
                "options": ["A) Harper Lee", "B) Harriet Tubman", "C) L. S. Meyer", "D) J. D. Salinger"],
                "answer": "A"
            },
            {
                "question": "Which country is famous for the Great Wall?",
                "options": ["A) China", "B) Japan", "C) South Korea", "D) North Korea"],
                "answer": "A"
            }
            # Add more questions as needed
        ]
    
    def display_question(self, question):
        print(question["question"])
        for option in question["options"]:
            print(option)
    
    def ask_question(self, question):
        self.display_question(question)
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer == question["answer"]:
            print("Correct!")
            return 1
        else:
            print("Incorrect.")
            return 0
    
    def run_quiz(self):
        random.shuffle(self.questions)
        score = 0
        for question in self.questions:
            score += self.ask_question(question)
        print(f"Your final score is: {score}/{len(self.questions)}")
    
# Create a Quiz instance and run the quiz
quiz = Quiz()
quiz.run_quiz()
