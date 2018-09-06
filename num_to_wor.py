#given a number n,print it in words
'''import inflect
import inflection
n=int(input())
p = inflect.engine()
c=p.number_to_words(n)
print(inflection.camelize(c))'''
a=int(input())
lst=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
if(1<=a<=10):
  print(lst[a-1])
