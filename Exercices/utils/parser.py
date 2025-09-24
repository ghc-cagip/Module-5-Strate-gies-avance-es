def parse_response(data: dict) -> str:
    # TODO: retourner une chaîne lisible à partir du dict
    return f"Status: {data.get('status', 'unknown')}"
