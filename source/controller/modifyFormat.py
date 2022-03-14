

from sqlalchemy import null

#modify filter to match the format used in Elastic search
def modifyFilter(filter):
    Type = filter['Type']
    Language = filter['Language']

    # case either type or language list has 1 member
    if (len(Type) == 1):
        Type = Type[0]

    if (len(Language) == 1):
        Language = Language[0]

        # case both type and language is empty list
    if (len(Type) == 0 and len(Language) == 0):
        return null
    else:
        # case either type and language is empty list
        if (len(Type) == 0):
            filter = {
                "bool":
                {
                    "must": {"term": {"Language": Language}}
                }
            }
        elif (len(Language) == 0):
            filter = {
                "bool": {
                    "must": {"term": {"Type": Type}}
                }
            }
        #default case
        else:
            filter = {
                "bool": {
                    "must": [
                        {"term": {"Type": Type}},
                        {"terms": {"Language": Language}}
                    ]
                }
            }

    return filter

# test code
if __name__ == "__main__":
    print(modifyFilter({"Language": [], "Type": []}))
    print(modifyFilter({"Language": ["sl"], "Type": []}))
    print(modifyFilter({"Language": ["sl", "es"], "Type": ["pdf"]}))
    print(modifyFilter({"Type":["docx","odt","rtf","txt","docx","odt","rtf","txt"],"Language":["sl","de","es"]}))
