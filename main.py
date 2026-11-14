import json

def check_document_for_typos(expected_data, received_data):
    """
    Compares expected immigration document data with received data to identify typos.
    This simulates the manual process of checking I-797A or I-94 for errors.
    """
    discrepancies = {}
    print("\n--- Document Typo Check ---")
    print(f"Expected Data: {json.dumps(expected_data, indent=2)}")
    print(f"Received Data: {json.dumps(received_data, indent=2)}")
    print("\n--- Discrepancies Found ---")

    # Iterate through expected fields to find mismatches or missing fields
    for field, expected_value in expected_data.items():
        received_value = received_data.get(field)
        if received_value is None:
            # Illustrates a missing field, which is a type of error
            discrepancies[field] = f"Field '{field}' missing in received document. Expected: '{expected_value}'"
        elif expected_value != received_value:
            # Illustrates a typo or mismatch in data
            discrepancies[field] = (
                f"Mismatch in '{field}': Expected '{expected_value}', "
                f"but received '{received_value}'."
            )
        else:
            print(f"  ✅ '{field}': Matches ('{expected_value}')")

    if not discrepancies:
        print("  No discrepancies found. Documents appear to be correct.")
    else:
        for field, message in discrepancies.items():
            print(f"  ❌ {message}")
    
    print("\n--- Suggested Correction Action ---")
    if discrepancies:
        # Suggests the need for correction, mirroring the article's main topic
        print("Based on the discrepancies, you may need to file a correction request with USCIS.")
        print("Specifically, address the following fields:")
        for field in discrepancies.keys():
            print(f"- {field}")
        print("\nEnsure you provide supporting evidence for the correct information.")
    else:
        print("No immediate correction action appears necessary based on this check.")

    return discrepancies

if __name__ == "__main__":
    # Scenario 1: No typos, all data matches
    print("\n" + "="*80 + "\n")
    print("--- Scenario 1: No typos ---")
    expected_applicant_data_1 = {
        "full_name": "John Doe",
        "date_of_birth": "1990-01-15",
        "visa_category": "H1B",
        "petition_number": "LIN2300000001"
    }
    received_document_data_1 = {
        "full_name": "John Doe",
        "date_of_birth": "1990-01-15",
        "visa_category": "H1B",
        "petition_number": "LIN2300000001"
    }
    check_document_for_typos(expected_applicant_data_1, received_document_data_1)
    print("\n" + "="*80 + "\n")

    # Scenario 2: Typo in name and a missing field
    print("--- Scenario 2: Typo in name and missing field ---")
    expected_applicant_data_2 = {
        "full_name": "Jane Smith",
        "date_of_birth": "1985-03-22",
        "visa_category": "H1B",
        "petition_number": "WAC2300000002"
    }
    received_document_data_2 = {
        "full_name": "Jnae Smith", # Typo here (Jane vs Jnae)
        "date_of_birth": "1985-03-22",
        # "visa_category" is intentionally missing here to simulate a common error
        "petition_number": "WAC2300000002"
    }
    check_document_for_typos(expected_applicant_data_2, received_document_data_2)
    print("\n" + "="*80 + "\n")

    # Scenario 3: Typo in visa category format
    print("--- Scenario 3: Typo in visa category ---")
    expected_applicant_data_3 = {
        "full_name": "Alice Wonderland",
        "date_of_birth": "1992-11-01",
        "visa_category": "H1B",
        "petition_number": "EAC2300000003"
    }
    received_document_data_3 = {
        "full_name": "Alice Wonderland",
        "date_of_birth": "1992-11-01",
        "visa_category": "H1-B", # Typo here (H1B vs H1-B)
        "petition_number": "EAC2300000003"
    }
    check_document_for_typos(expected_applicant_data_3, received_document_data_3)
    print("\n" + "="*80 + "\n")
