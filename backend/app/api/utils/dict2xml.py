import xmltodict


def dict_to_xml(data: dict) -> str:
    return xmltodict.unparse(data, pretty=True)
