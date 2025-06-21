import pandas as pd
from openai import AzureOpenAI
from utils import classify_attendance
import os

api_key = os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-12-01-preview",
    azure_endpoint="https://mindcraft-kapidhwaj-openai-api-key.openai.azure.com/"
)

def main():
    df = pd.read_csv("data/sample_attendance.csv")
    statuses = []

    for _, row in df.iterrows():
        name = row["Name"]
        time = str(row["EntryTime"]) if pd.notna(row["EntryTime"]) else ""
        status = classify_attendance(client, DEPLOYMENT_NAME, name, time)
        statuses.append(status)

    df["Status"] = statuses
    output_path = "output/processed_attendance.xlsx"
    os.makedirs("output", exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"Processed attendance saved to {output_path}")

if __name__ == "__main__":
    main()

