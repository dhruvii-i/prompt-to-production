"""
UC-0A — Complaint Classifier
Starter file. Build this using the RICE → agents.md → skills.md → CRAFT workflow.
"""
import argparse
import csv

def classify_complaint(row: dict) -> dict:
    """
    Classify a single complaint row.
    Returns: dict with keys: complaint_id, category, priority, reason, flag
    """
    description = row.get("description", "").lower()
    
    # Severity keywords for Urgent priority
    severity_keywords = ["injury", "child", "school", "hospital", "ambulance", "fire", "hazard", "fell", "collapse"]
    priority = "Standard"
    if any(word in description for word in severity_keywords):
        priority = "Urgent"
    
    # Category mapping keywords
    category_map = {
        "Pothole": ["pothole"],
        "Flooding": ["flood", "water", "rain"],
        "Streetlight": ["streetlight", "lights out", "flickering"],
        "Waste": ["garbage", "bins", "waste", "smell", "dead animal"],
        "Noise": ["music", "noise", "sound", "loud"],
        "Road Damage": ["road surface", "cracked", "sinking", "manhole"],
        "Heritage Damage": ["heritage"],
        "Heat Hazard": ["heat", "sun"],
        "Drain Blockage": ["drain", "drainage", "blocked"],
    }
    
    category = "Other"
    reason = "No specific category keywords found."
    flag = ""
    
    for cat, keywords in category_map.items():
        for kw in keywords:
            if kw in description:
                category = cat
                reason = f"Classified as {cat} because the description mentions '{kw}'."
                break
        if category != "Other":
            break
            
    if category == "Other":
        flag = "NEEDS_REVIEW"
        reason = "Genuinely ambiguous description; no keywords matched."

    return {
        "complaint_id": row.get("complaint_id"),
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }


def batch_classify(input_path: str, output_path: str):
    """
    Read input CSV, classify each row, write results CSV.
    """
    results = []
    try:
        with open(input_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                results.append(classify_complaint(row))
        
        if results:
            keys = results[0].keys()
            with open(output_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(results)
    except FileNotFoundError:
        print(f"Error: Input file {input_path} not found.")
    except Exception as e:
        print(f"Error during batch classification: {e}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input",  required=True, help="Path to test_[city].csv")
    parser.add_argument("--output", required=True, help="Path to write results CSV")
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")
