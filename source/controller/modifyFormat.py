

from sqlalchemy import null

#modify filter to match the format used in Elastic search
def modifyFilter(filter):
    type = filter['type']
    language = filter['language']

    # case either type or language list has 1 member
    if (len(type) == 1):
        type = type[0]

    if (len(language) == 1):
        language = language[0]

        # case both type and language is empty list
    if (len(type) == 0 and len(language) == 0):
        return null
    else:
        # case either type and language is empty list
        if (len(type) == 0):
            filter = {
                "bool":
                {
                    "must": {"term": {"language": language}}
                }
            }
        elif (len(language) == 0):
            filter = {
                "bool": {
                    "must": {"term": {"type": type}}
                }
            }
        #default case
        else:
            filter = {
                "bool": {
                    "must": [
                        {"term": {"type": type}},
                        {"terms": {"language": language}}
                    ]
                }
            }

    return filter

