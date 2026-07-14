from bson import ObjectId


def stringify_object_id(document: dict) -> dict:
    if "_id" in document and isinstance(document["_id"], ObjectId):
        document["_id"] = str(document["_id"])
    return document


def as_object_id(id_value: str) -> ObjectId:
    if not ObjectId.is_valid(id_value):
        raise ValueError("Invalid ObjectId")
    return ObjectId(id_value)


def as_document_id(id_value: str) -> ObjectId | str:
    """Support both seeded string IDs and Mongo-generated ObjectIds."""
    return ObjectId(id_value) if ObjectId.is_valid(id_value) else id_value
