curl https://api.openai.com/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer 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" -d '{
"input": "Your text string goes here",
"model": "text-embedding-ada-002"
}'