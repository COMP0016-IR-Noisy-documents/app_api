

from sqlalchemy import null

#modify filters to match the format used in Elastic search
def modifyFilter(filters):

    
    Type = []
    
    Language = []

    try:
        Language = filters['language']
    except KeyError:
        pass

    try:
        Type = filters['type']
    except KeyError:
        pass
    
        # case both type and language is empty list
    if (len(Type) == 0 and len(Language) == 0):
        return []
    else:
        # case either type and language is empty list
        if (len(Type) == 0):
            filters = [{"terms": {"language": Language}}]
            
        elif (len(Language) == 0):
            filters = [{"terms": {"type": Type}}]
            
        #default case
        else:
            filters = [{"terms": {"type": Type}}, {"terms": {"language": Language}}]
            
    print(filters)
    return filters

# test code
if __name__ == "__main__":
    print(modifyFilter({"Language": [], "Type": []}))
    print(modifyFilter({"Language": ["sl"], "Type": []}))
    print(modifyFilter({"Language": ["sl", "es"], "Type": ["pdf"]}))
    print(modifyFilter({"Type":["docx","odt","rtf","txt","docx","odt","rtf","txt"],"Language":["sl","de","es"]}))
