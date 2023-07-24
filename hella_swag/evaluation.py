import re
import concurrent.futures

from hella_swag.data import read_hella_swag_problems, read_multishot_examples
from model import run


def format_problem(problem, ind):
    set_up = ('Only respond with the most likely reponse. '
              'If the correct answer is 2, respond with your answer ending with *2*')
    ctx = problem['ctx']
    endings = problem['endings']
    label = problem['label']
    options = "\n".join([f'{ind}. {ending}' for ind, ending in enumerate(endings)])
    prompt = f'{set_up} \n\nScenerio {ind} :{ctx} \n{options}'

    return prompt, label

def extract_label_from_response(respose):
    match = re.search(r'\*([0-3])\*', respose)
    if match:
        return match.group(1)
    else:
        match = re.search(r'option\s*([0-3])', respose, re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            match = re.search(r'([0-3])', respose)
            if match:
                return match.group(1)
    return -1


def evaluate_problem(problem, ind, multishot):
    history = {'internal': [], 'visible': []}
    prompt, real_label = format_problem(problem, ind)
    multishot_prompt = f'{multishot} \n\n{prompt}'
    response = run(multishot_prompt, history)

    model_label = extract_label_from_response(response)
    
    if int(model_label) == int(real_label):
        print(f'{prompt}\nModel:{response}\n✅\n')
        return 1
    else:
        print(f'{prompt}\nModel:{response}\n❌ the correct answer is {real_label} vs. {model_label}\n')
        return 0

def evaluate_hella_swag_dataset(limit = 10, k=10):
    problems = read_hella_swag_problems(limit)
    multishot = read_multishot_examples(k)

    total_problems = max(list(problems.keys()))+1
    print('Problem set size', total_problems)
    
    with concurrent.futures.ThreadPoolExecutor( max_workers=16 ) as executor:
        scores = executor.map(evaluate_problem, problems.values(), problems.keys(), [multishot]*len(problems))
    
    score = sum(scores)
    print(f'Total score: {score}/{total_problems}')
    return score / total_problems