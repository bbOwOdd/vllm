from vllm import LLM, SamplingParams

prompts = [
    # "Hello, my name is",
    # "The president of the United States is",
    # "The capital of France is",
    # "The future of AI is",
    "Do you know Japan?"
]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=500)
llm = LLM(model="/home/z890/model/Meta-Llama-3-8B", tensor_parallel_size=2, dtype="float16")   #meta-llama/Meta-Llama-3-8B /home/z890/model/Meta-Llama-3-8B
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")