import json
import openai

# Load your API key from an environment variable or secret management service
api_key = "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"
openai.api_key = api_key

file_name = "prompt.jsonl"

prompt = [{
    "prompt": "Tin Ritto ->",
    "completion": "A man in Hat Yai that lives in Sadao village"
},{
    "prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{
    "prompt": "Ritto Hat Yai 18 ->",
    "completion": "A Sadao Boy who lives in Hat Yai",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU Hat Yai",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU of Song Kla",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},{"prompt": "Tin Ritto ->",
    "completion": "A computer science student of PSU",
},]

with open(file_name, "w") as output_file:
    for entry in prompt:
        json.dump(entry, output_file)
        output_file.write("\n")


print("Done generating prompt.jsonl")

"""
upload_response = openai.File.create(
    file = open(file_name, "rb"),
    purpose='fine-tune'
)
file_id = upload_response.id
print(file_id)

fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci")     
#print(fine_tune_response)

fine_tune_events = openai.FineTune.list_events(id=fine_tune_response.id)
print(fine_tune_events)


retrieve_response = openai.FineTune.retrieve(id=fine_tune_response.id)
#print(retrieve_response)

#response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
#print(response)

# Option 1 | if response.fine_tuned_model != null
fine_tuned_model = fine_tune_response.fine_tuned_model
print(fine_tuned_model)

# Option 2 | if response.fine_tuned_model == null
retrieve_response = openai.FineTune.retrieve(fine_tune_response.id)
fine_tuned_model = retrieve_response.fine_tuned_model
print(fine_tuned_model)
"""