from Nao import Nao

def get_user_input(text):
	input = raw_input(text)

	if "(" not in input:
		input += "(None)"

	if "nao." not in input:
		input = "nao." + input

	return input

def main():
    nao = Nao("192.168.0.2", None)
    nao.init()

    do_loop = True

    while do_loop:
    	entree_utilisateur = get_user_input("Nao: ")

    	if entree_utilisateur == "nao.quit(None)":
    		do_loop = False
    	elif entree_utilisateur == "nao.help(None)":
    		print nao.actions.keys()
    	else:
	    	try:
	    		eval(entree_utilisateur)
	    	except Exception, e:
	    		print e



if __name__ == '__main__':
    main()