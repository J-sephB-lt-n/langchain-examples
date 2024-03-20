"""
Example usage:
    $ python -m llm_respond \
            --prompt_file llm_task_prompts/1.txt
"""

import argparse

from llm.llm_interface import LlmInterface
from llm.models.gpt4 import Gpt4

models: dict[str, LlmInterface] = {"gpt4": Gpt4}

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", help="The name of the LLM model to use", type=str)
# parser.add_argument(
#        "-f",
#        "--prompt_file",
#        help="Path to file containing prompt to give to the model",
#        type=str
#        )
args = parser.parse_args()

llm: LlmInterface = models[args.model]()
