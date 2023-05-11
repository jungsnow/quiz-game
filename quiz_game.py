import pandas as pd

def load_questions():
    df = pd.read_csv('quiz_questions.csv')
    questions = df.to_dict('records')
    return questions
    #print(questions)
def run(quest):
    score = 0
    for q in quest:
        print(q['Question']) 
        print("Options: ")
        opts = [q['Option 1'], q['Option 2'], q['Option 3'], q['Option 4']]
        for i, option in enumerate(opts):
            print(f"{i + 1}, {option}")
        
        ans = input('Enter your number:')
        ans = int(ans) - 1
        if opts[ans] == q['Answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(score)
            

if __name__ == "__main__":
    run(load_questions())