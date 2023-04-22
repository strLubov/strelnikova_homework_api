from voluptuous import Schema, PREVENT_EXTRA

resource_schema = Schema(
{
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str
        },
    extra=PREVENT_EXTRA,
    required=True
)

list_resources_schema = Schema(
{
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [resource_schema],
    "support": {
        "url": str,
        "text": str
    }
}
)