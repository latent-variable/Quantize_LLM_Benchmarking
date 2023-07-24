
# from human_eval.data import read_problems
from hella_swag.evaluation import evaluate_hella_swag_dataset



if __name__ == '__main__':
    
    score = evaluate_hella_swag_dataset(limit = None)

    # Basic example
    # history = {'internal': [], 'visible': []}

    # "Continue" example. Make sure to set '_continue' to True above
    # arr = [user_input, 'Surely, here is']
    # history = {'internal': [arr], 'visible': [arr]}

    # run(user_input, history)
