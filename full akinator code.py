import akinator
aki = akinator.Akinator()
q = aki.start_game()
while aki.progression <= 80:
    a = input(q +"\n\t")
    if a == 'b':
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurhter:
            pass
    else:
        q = aki.answer(a)
aki.win()
correct = input(f"Its {aki.first_guess['name']} ({aki.first_guess['description']})! Was i correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
if correct.lower() == 'yes' or correct.lower() == 'y':
    print("yes i got it\n")
else:
    print("ohh just missed\n")
            
