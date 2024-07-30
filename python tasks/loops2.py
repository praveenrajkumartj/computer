class edex():
    name="praveen"
    loc="erode"
print(getattr(edex,'name'))
print(getattr(edex,'loc'))
setattr(edex,'course','python')#create
print(getattr(edex,'course'))
setattr(edex,'loc','salem')#update
print(getattr(edex,'loc'))
#delattr(edex,'loc')#delete
print(getattr(edex,'loc'))

print(edex.name)
edex.id=2
print(edex.id)



class edex():
    name="praveen"
    loc="erode"
print(edex.name)#acess
edex.course='python'
edex.loc='salem'
del edex.name
print(edex.loc)
print(edex.course)
print(edex.name)



class edex():
    name="praveen"
    loc="erode"
tech=edex()    



