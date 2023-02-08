import webbrowser #webbrowser tool

Name = input("Enter your name(first letter capital)  ") #taking name
if Name == 'Aman': #checking if name
    webbrowser.open_new_tab('https://images.freeimages.com/images/large-previews/4d0/hi-donkey-1402471.jpg')
else:
    print("Not for you")
