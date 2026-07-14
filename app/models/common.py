from bson import ObjectId


def stringify_object_id(document: dict) -> dict:
    if "_id" in document and isinstance(document["_id"], ObjectId):
        document["_id"] = str(document["_id"])
    return document


def as_object_id(id_value: str) -> ObjectId:
    if not ObjectId.is_valid(id_value):
        raise ValueError("Invalid ObjectId")
    return ObjectId(id_value)
