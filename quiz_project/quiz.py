def run_quiz(questions):
    score  = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input('Enter your answer (A, B, C): ')
        if answer.upper() == question['answer']:
            print('Correct \n')
            score+=1
        else:
            print('Wrong!! The correct answer is', question["answer"], '\n')
            
    print(f'You got {score} out of {len(questions)} questions correct.')
            
         
        

questions = [
    {
        "prompt": "Who is credited with inventing the World Wide Web?",
        "options": ["A. Steve Jobs", "B. Bill Gates", "C. Tim Berners-Lee"],
        "answer": "C"
    },
    {
        "prompt": "What type of computer was the first laptop computer?",
        "options": ["A. Apple Macintosh", "B. IBM PC", "C. Osborne 1"],
        "answer": "C"
    },
    {
        "prompt": "What is the largest social media network in the world?",
        "options": ["A. Twitter", "B. Facebook", "C. Instagram"],
        "answer": "B"
    },
    {
        "prompt": "Who is considered the founder of modern computer science?",
        "options": ["A. Alan Turing", "B. Steve Jobs", "C. Bill Gates"],
        "answer": "A"
    },
    {
        "prompt": "The website Info.cern.ch is famous for what function?",
        "options": ["A. Being the predecessor for Wikipedia", "B. Being the world\'s very first website", "C. Being the world\'s first ever search engine"],
        "answer": "B"
    },
    {
        "prompt": "What year was the iPhone first released in?",
        "options": ["A. 2007", "B. 2009", "C. 2010"],
        "answer": "A"
    }
]   


run_quiz(questions)