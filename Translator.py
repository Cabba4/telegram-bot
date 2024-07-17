import translations;

def t(key, language="en"):
  if language == "en":
    dictionary = translations.en
#  else if language == "fi":
#    dictionary = translations.fi
  else:
    return key

  if key in dictionary.keys():
    return dictionary[key]
  else:
    return key