__author__ = 'Mago Castozzo'

import argparse
import os
import hashlib

class Questioner:
    def __init__(self):
        self.message = 'Ma lo sai chi?'

class Respondent:
    def __init__(self, answer):
        self.answer = answer
    
    def isAnswerCorrect(self):
        hashed_string = hashlib.sha256(self.answer.encode('utf-8')).hexdigest()
        if hashed_string == "57063d5457bdab24e7df8f75e9d11951f5bcdb90d1f181d9a2605eced52b54b3":
            return True
        
        return False




parser = argparse.ArgumentParser()
parser.add_argument('answer', type=str,
                    help='Put this only if you know the real answer')

def main(args):
    """Running this just because"""
    questioner = Questioner()
    respondent = Respondent(args.answer)

    print("Question is: %s"%questioner.message)
    if respondent.isAnswerCorrect():
        print("Well done. Your answer is correct. Thanks to %s"%args.answer)
    else:
        print("Sorry, you really need to think a bit harder on this important question")

if __name__ == "__main__":
    main(parser.parse_args())