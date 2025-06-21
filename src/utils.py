def classify_attendance(client, deployment, name, time):
    prompt = f"""
You are an attendance analyzer.

Rules:
- If EntryTime is blank or null → Absent
- If EntryTime <= 09:05 → Present
- If EntryTime > 09:05 → Late

Input:
Name: {name}
EntryTime: {time}

Output:
Return only one word: Present, Late, or Absent
"""
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing {name}: {e}")
        return "Error"
