#given a number n,print it in words
import inflect
import inflection
n=int(input())
p = inflect.engine()
c=p.number_to_words(n)
print(inflection.camelize(c))
