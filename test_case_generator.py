import os
import json
import random
from tqdm import tqdm
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.getenv("LLM_HW_API_KEY")
if not api_key:
    raise ValueError("API Key not set")

client = genai.Client(api_key=api_key)

INPUT_CORPUS = "indexes/corpus.json" 
OUTPUT_FILE = "test_dataset.json"
TOTAL_CASES = 30 


class LLMResponse(BaseModel):
    generated_code: str = Field(description="The Python function code.")
    explanation: str = Field(description="Brief explanation of the changes or logic.")

class TestCase(BaseModel):
    id: int
    verdict: str
    label: int
    student_code: str
    original_code: str
    type: str


def generate_from_chunk(chunk: dict, is_plagiarism: bool, case_id: int) -> TestCase:
    
    reference_code = chunk["text"]

    if is_plagiarism:
        prompt_type = "POSITIVE (PLAGIARISM)"
        instruction = """
        TASK: Create a PLAGIARIZED version of the Reference Code.
        1. Keep the LOGIC and ALGORITHM exactly the same.
        2. Rename functions and variables (obfuscation).
        3. Change control flow structure if possible (e.g. for loop -> while loop) without changing logic.
        4. Remove or rewrite docstrings.
        """
    else:
        prompt_type = "NEGATIVE (ORIGINAL)"
        instruction = """
        TASK: Create a completely ORIGINAL function.
        1. The function should perform a task SIMILAR to the Reference Code (same domain).
        2. BUT it must use a fundamentally DIFFERENT algorithm or implementation.
        3. If the reference is 'Binary Search', you write 'Linear Search' or 'Interpolation Search'.
        4. If no alternative algorithm exists, write a function for a different but related task.
        """

    prompt = f"""
    {instruction}
    
    REFERENCE FUNCTION:
    {reference_code}
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=prompt, 
            config={
                "response_mime_type": "application/json",
                "response_json_schema": LLMResponse.model_json_schema(),
            },
        )
        ai_output = LLMResponse.model_validate_json(response.text) # type: ignore
        
        return TestCase(
            id=case_id,
            verdict="Plagiarism" if is_plagiarism else "Original",
            label=1 if is_plagiarism else 0,
            student_code=ai_output.generated_code,
            original_code=reference_code,
            type=prompt_type
        )
        
    except Exception as e:
        print(f"Error on case {case_id}: {e}")
        return None # type: ignore


if not os.path.exists(INPUT_CORPUS):
    raise FileNotFoundError(f"Could not find {INPUT_CORPUS}. Did you save it in 01_indexing?")

with open(INPUT_CORPUS, "r") as f:
    all_chunks = json.load(f)

print(f"Loaded {len(all_chunks)} function chunks from index.")

dataset = []

print(f"Generating {TOTAL_CASES} test cases using Gemini 2.0 Flash...")

for i in tqdm(range(TOTAL_CASES)):
    chunk = random.choice(all_chunks)
    
    is_plagiarism = (i % 2 == 0)
    
    case = generate_from_chunk(chunk, is_plagiarism, case_id=i)
    
    if case:
        dataset.append(case)

json_data = [t.model_dump() for t in dataset]
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4)

print(f"Success! {len(dataset)} cases saved to {OUTPUT_FILE}")