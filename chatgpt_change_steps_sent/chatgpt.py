from config import get_api_key, MODEL
from openai import OpenAI

def return_chatgpt_response(formatted_steps=[]):
    if not formatted_steps:
        return "No steps provided"
    client = OpenAI(api_key=get_api_key())
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": prompt_for_call(formatted_steps)
        }])

    output = response.choices[0].message.content
    return output.split("\n")


def prompt_for_call(formatted_steps):
    return f"""
I have a list of steps that need to be refined to sound more professional and natural while maintaining clarity.

Input:
{formatted_steps}(This will be a list of multiple steps.)

Requirements:
Rewrite each step to enhance professionalism and readability.
Maintain the meaning and sequence of the original steps.
Provide the output as a list without numbering or bullet points.
Ensure each refined step corresponds to an input step.
Output Format:
Each step should be rewritten and presented in the same order as provided, formatted as a clean list without any numbering or bullets."""
