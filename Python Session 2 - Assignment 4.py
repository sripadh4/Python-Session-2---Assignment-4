
# coding: utf-8

# In[1]:

Declaration = ("WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens")
a = Declaration.split()
for i in a:
    if i == "INDIA,":
        a.insert(5, "\n     ")
    if i == "SOVEREIGN,":
        a.insert(15, "!")
        a.insert(16, "\n\t    ")
    if i == "REPUBLIC":
        a.insert(21, "\n\t     ")
        print (' '.join(a[0:29]) + ":")

