NAME	=	{{name_project}}

INCLUDES = 	-I./includes
SRC		=	main.c

OBJ_DIR	=	{{inputs.obj_dir}}
OBJS	=	$(patsubst %.c, $(OBJ_DIR)/%.o, $(SRC))

CC		=	{{inputs.cc}}
CFLAGS	=	{{inputs.cflags}}

VPATH	=	./src			#caso crie novos diretorios, adicione aqui

$(OBJ_DIR)/%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@  $(INCLUDES)

all: $(NAME)

$(NAME): $(OBJ_DIR) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)
clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONE: all clean fclean re
