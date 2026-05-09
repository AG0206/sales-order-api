allowed_transitions = {
    "Draft": ["Submitted", "Cancelled"],
    "Submitted": ["Cancelled"],
    "Cancelled": []
}


def is_valid_status_change(current_status, new_status):
    return new_status in allowed_transitions[current_status]
