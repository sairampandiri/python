#given a number n,print it in words
import inflect
n=int(input())
p = inflect.engine()
print(p.number_to_words(n))
