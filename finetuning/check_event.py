import json
import openai

# Load your API key from an environment variable or secret management service
api_key = "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"
openai.api_key = api_key


retrieve_response = openai.FineTune.retrieve(id="ft-UgoVqfXXoULEUCIx3gP62rCC")
print(retrieve_response)
