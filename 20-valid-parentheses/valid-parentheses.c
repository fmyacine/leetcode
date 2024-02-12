typedef struct Pile {
    char val;
    struct Pile* next;
} Pile;

void afficherPile(Pile* pile) {
    Pile* current = pile;
    printf("Pile: ");
    while (current != NULL) {
        printf("%c ", current->val);
        current = current->next;
    }
    printf("\n");
}

void initPile(Pile** pile) {
    *pile = NULL;
}

int isEmpty(Pile* pile) {
    if(pile == NULL) return true;
    else return false;
}

void empiler(Pile** pile, char value) {
    Pile* newPile = (Pile*)malloc(sizeof(Pile));
    if (newPile == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newPile->val = value;
    newPile->next = *pile;
    *pile = newPile;
}

void depiler(Pile** pile, char *value) {
    if (*pile != NULL) {
        Pile* top = *pile;
        *value = top->val;
        *pile = top->next;
        free(top);}
}

char sommet(Pile* pile) {
    if (isEmpty(pile)) {
        fprintf(stderr, "Error: Stack is empty\n");
        exit(EXIT_FAILURE);
    }
    return pile->val;
}
void viderPile(Pile** pile) {
    while (*pile != NULL) {
        Pile* temp = *pile;
        *pile = (*pile)->next;
        free(temp);
    }
}


bool isValid(char* s) {
    Pile* P;
    Pile* PF;
    initPile(&P);
    char y,x;
    for(int i = 0 ; i < strlen(s) ; i++){
        
        if(s[i] == '(' || s[i] == '{' || s[i] == '['){
            empiler(&P , s[i]);
        }

        
        if(s[i] == ')' )
        {
            if(isEmpty(P)) return false; 
            depiler(&P,&x);

            if(x != '(') return false;
        }

        if(s[i] == '}' )
        {
            if(isEmpty(P)) return false; 
            depiler(&P,&x);

            if(x != '{') return false;
        }
        if(s[i] == ']' )
        {
            if(isEmpty(P)) return false; 
            depiler(&P,&x);

            if(x != '[') return false;
        }
    }

    return isEmpty(P);
}