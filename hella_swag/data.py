from typing import Iterable, Dict
import gzip
import json
import os


ROOT = os.path.dirname(os.path.abspath(__file__))
HELLASWAG_VAL = os.path.join(ROOT, "..", "Data", "HellaSwag", "hellaswag_val.jsonl")
HELLASWAG_TRAIN = os.path.join(ROOT, "..", "Data", "HellaSwag", "hellaswag_train.jsonl")


def read_hella_swag_problems(limit = None, evalset_file: str = HELLASWAG_VAL) -> Dict[str, Dict]:
    problem_set = {}
    for ind, task in enumerate(stream_jsonl(evalset_file)):
        if limit != None and limit == ind:
            break
        problem_set[ind] = task 
    return problem_set


def read_multishot_examples(k, trainset_file: str = HELLASWAG_TRAIN):
    multi_shot_examples = []
    for ind, example in enumerate(stream_jsonl(trainset_file)):
        if ind == k:
            break
        else:
            multi_shot_examples.append(format_example(example, ind))

    return "\n\n".join(multi_shot_examples)
       
def format_example(example, ind):
    ctx = example['ctx']
    label = example['label']
    endings = example['endings']
    correct_ending = endings[label]
    expected_model_reponse = f'Based on the provided information, \"{ctx} {correct_ending}\" is the most logical response, thus the correct answer is *{label}*'
    options = "\n".join([f'{ind}. {ending}' for ind, ending in enumerate(endings)])
    prompt = f'Example: {ind} \nScenerio: {ctx} \n{options}\n{expected_model_reponse}'
    return prompt

def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, 'rt') as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    yield json.loads(line)