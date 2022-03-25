

from sqlalchemy import null

#modify filters to match the format used in Elastic search
def modifyFilter(filters):

    print(filters)
    modifiedFilters = None
    Type = []
    
    Language = []
    # The dataset has inverted columns
    try:
        Type = filters['language']
    except KeyError:
        pass

    try:
        Language = filters['type']
    except KeyError:
        pass
    
        # case both type and language is empty list

    if (len(Type) == 0 and len(Language) == 0):
        return []
    else:
        # case either type and language is empty list
        if (len(Type) == 0):
            modifiedFilters = [{"terms": {"language": Language}}]
            
        elif (len(Language) == 0):
            modifiedFilters = [{"terms": {"type": Type}}]
            
        #default case
        else:
            modifiedFilters = [{"terms": {"type": Type}}, {"terms": {"language": Language}}]
            
    print(modifiedFilters)
    return modifiedFilters

