"""
Vision-based auto-categorization, for step 6 of the intake plan:
suggest category/part name from a photo so staff just confirms instead of typing.

Wire this into routers/photos.py after a photo upload, e.g.:
    suggestion = classify_part_photo(contents)
    return {"item_id": item_id, "saved": True, "suggestion": suggestion}
"""
import base64
import os
import httpx

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

def classify_part_photo(image_bytes: bytes) -> dict:
    if not ANTHROPIC_API_KEY:
        return {"category": None, "part_name": None, "note": "ANTHROPIC_API_KEY not set"}

    b64 = base64.b64encode(image_bytes).decode("utf-8")
    response = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 200,
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}},
                    {"type": "text", "text": (
                        "This is a photo of a used motor spare part. Reply ONLY as JSON: "
                        '{"category": "...", "likely_part_name": "...", "condition_notes": "..."}'
                    )},
                ],
            }],
        },
        timeout=30,
    )
    response.raise_for_status()
    text = response.json()["content"][0]["text"]
    return {"raw_model_response": text}
