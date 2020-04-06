def sentence_maker(phrase):
    interrogative = ("how", "what", "why")
    
    if phrase.startswith(interrogative):
        return "{}?".format(phrase.capitalize())
        #return text
    else:
        return "{}".format(phrase.capitalize())

results = []
while True:
    user_input = input("Say Something : ")
    if(user_input == "bye"):
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))

