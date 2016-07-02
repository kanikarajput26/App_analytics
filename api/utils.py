def Processor(collect1,cid):
    newlist =[]
    for item in collect1.find({"_id.id":cid}):
        newlist.append(item)
    return newlist

