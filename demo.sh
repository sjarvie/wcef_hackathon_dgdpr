#!/usr/bin/env bash -e

echo "Upload file"
curl \
  -X POST \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "ciphertext": "otLmP9mrqIvjT1b1OH7Y6eYVqloe9GDSGw==", 
    "edek": "k9oAIgECyhFc6GRLBo95/1+a/UgubjPUAHnC97HhzK0y1QEQxrPaACIBA1GB2xea/mYkiQUSaq2Cv9D9YrZQ5M4Es+SYyl9xgdZn2gAiAQNKUddXs/WkaewE4dUjksF6awGlUz1QAPeN8lkE28LQDg==", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ=="
  }' \
  "localhost:8888/upload"

echo -e "\n\nList files"
curl \
  -sS \
  -X GET \
  "localhost:8888/files?sender=AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==" | jq

echo -e "\n\nGrant access"
curl \
  -X POST \
  -Ss \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==", 
    "receiver": "AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA==", 
    "name": "Bob", 
    "rekey": "AEJsNi3kOpBwbKnjpGvVzeWh+dn3m9vmjHc65HzajMtt", 
    "encryptedEphemeralKey": "k9oAIgECyhFc6GRLBo95/1+a/UgubjPUAHnC97HhzK0y1QEQxrPaACIBA1GB2xea/mYkiQUSaq2Cv9D9YrZQ5M4Es+SYyl9xgdZn2gAiAQNKUddXs/WkaewE4dUjksF6awGlUz1QAPeN8lkE28LQDg=="
  }' \
  "localhost:8888/shares"

echo -e "\n\nDownload"
curl \
  -X POST \
  -Ss \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==",
    "receiver": "AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=="
  }' \
  "localhost:8888/download" | jq

echo -e "\n\nList shares"
curl \
  -X GET \
  -Ss \
  "localhost:8888/shares?filename=DonaldTrumpMentalExamination.txt&sender=AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==" | jq

echo -e "\n\nDownload"
curl \
  -X POST \
  -Ss \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==",
    "receiver": "AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=="
  }' \
  "localhost:8888/download" | jq

echo -e "\n\nRevoke access"
curl \
  -X DELETE \
  -sS \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==", 
    "receiver": "AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=="
  }' \
  "localhost:8888/shares"

echo -e "\n\nDownload"
curl \
  -X POST \
  -Ss \
  -d '{
    "filename": "DonaldTrumpMentalExamination.txt", 
    "sender": "AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ==",
    "receiver": "AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=="
  }' \
  "localhost:8888/download" | jq

