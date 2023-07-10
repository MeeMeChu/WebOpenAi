import json
import openai

# Load your API key from an environment vaหriable or secret management service
api_key = "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"
openai.api_key = api_key

file_name = "prompt.jsonl"


upload_response = openai.File.create(
    file = open(file_name, "rb"),
    purpose='fine-tune'
)

file_id = upload_response.id
print(file_id)

fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci")      
print("Response id: ", fine_tune_response.id)
fine_tune_events = openai.FineTune.list_events(id=fine_tune_response.id)
print(fine_tune_events)

#retrieve_response = openai.FineTune.retrieve(id=fine_tune_response.id)
##print(retrieve_response)
#fine_tuned_model = fine_tune_response.fine_tuned_model
#print(fine_tuned_model)