##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## makefile
##

NAME	=	trade

SRC		=	main.py

all:
	cp $(SRC) $(NAME)
	chmod 755 $(NAME)

clean:
	echo "Nothing to clean"

fclean:	clean
	rm $(NAME)	\

re:	fclean clean all

.PHONY:	all re clean fclean