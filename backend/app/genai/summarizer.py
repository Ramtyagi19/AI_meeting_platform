def summarize_text(text):

    if not text:
        return "No meeting content found."

    summary = f"""
    Meeting Summary:

    {text[:300]}
    """

    return summary.strip()