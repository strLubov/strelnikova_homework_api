from voluptuous import Schema, PREVENT_EXTRA

user_schema = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_user_schema = Schema(
    {
        "data":  {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str,
    },
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)