import tkinter as tk
import random


# Opções do Computador
p_p_t = ["PEDRA", "PAPEL", "TESOURA"]

# Definindo botões
def botao1_click(): # pedra
    chose_computer = random.choice(p_p_t)
    # Torna a primeira fala invisível
    fala_pc.place_forget()
    
    # Torna a primeira imagem invisível
    face_inicial.place_forget()
    
    # Novas falas e imagens
    if chose_computer == p_p_t[2]: # Computador escolhe tesoura
        fala_pc2.place(x=152, y=310)  
        da_tesoura.place(x=65, y=70)  
    elif chose_computer == p_p_t[1]: # Computador escolhe papel
        fala_pc3.place(x=152, y=310)
        do_papel.place(x=65, y=70) 
    # Else vai ser feito ainda pro caso de empate
    else:
        da_pedra.place(x=65, y=70) 
        fala_pc4.place(x=152, y=310)
        

def botao2_click(): # papel
    chose_computer = random.choice(p_p_t)
    
    # Torna a primeira fala invisível
    fala_pc.place_forget()
    
    # Torna a primeira imagem invisível
    face_inicial.place_forget()
    
    # Novas falas e imagens
    if chose_computer == p_p_t[2]: # Computador escolhe tesoura
        fala_pc3.place(x=152, y=310)  
        da_tesoura.place(x=65, y=70)  
    elif chose_computer == p_p_t[1]: # Computador escolhe papel
        fala_pc3.place(x=152, y=310)
        do_papel.place(x=65, y=70) 
    # Else vai ser feito ainda pro caso de empate
    else:
        fala_pc2.place(x=152, y=310)
        da_pedra.place(x=65, y=70) 
        
def botao3_click(): # tesoura
    chose_computer = random.choice(p_p_t)
    # Torna a primeira fala invisível
    fala_pc.place_forget()
    
    # Torna a primeira imagem invisível
    face_inicial.place_forget()
    
    # Novas falas e imagens
    if chose_computer == p_p_t[2]: # Computador escolhe tesoura  
        da_tesoura.place(x=65, y=70)  
        fala_pc4.place(x=152, y=310)
    elif chose_computer == p_p_t[1]: # Computador escolhe papel
        fala_pc2.place(x=152, y=310)
        do_papel.place(x=65, y=70) 
    else:
        fala_pc3.place(x=152, y=310)
        da_pedra.place(x=65, y=70) 


# BOTÃO DE SAIR
def botao4_click():
    root.quit()
    
# BOTÃO DE RECOMEÇAR
def botao5_click():
    
    # devolvendo condição inicial de imagem
    da_pedra.place_forget()
    da_tesoura.place_forget()
    do_papel.place_forget()
    face_inicial.place(x=65, y=70)
    
    # devolvendo condição inicial de texto
    fala_pc2.place_forget()
    fala_pc3.place_forget()
    fala_pc4.place_forget()
    fala_pc.place(x=136, y=310)
    
    
# Configuração da interface
root = tk.Tk()
root.title("PEDRA, PAPEL OU TESOURA")
root.geometry("400x400")  # Definindo as dimensões da janela
root.minsize(400, 400)  # Definindo largura e altura mínimas da janela
root.maxsize(400, 400) 

# Adicionando imagem da FACE
imagem1 = tk.PhotoImage(file="face.png") # uma foto qualquer posta de exibição
face_inicial = tk.Label(root, image=imagem1)
face_inicial.place(x=65, y=70)  # Definindo a posição do label

# Adicionando imagem da PEDRA
imagem2 = tk.PhotoImage(file="pedra.png") # uma foto qualquer posta de exibição
da_pedra = tk.Label(root, image=imagem2)
# da_pedra.place(x=65, y=70)  # Definindo a posição do label

# Adicionando imagem da PAPEL
imagem3 = tk.PhotoImage(file="papel.png") # uma foto qualquer posta de exibição
do_papel = tk.Label(root, image=imagem3)
# do_papel.place(x=65, y=70)  # Definindo a posição do label

# Adicionando imagem da TESOURA
imagem4 = tk.PhotoImage(file="tesoura.png") # uma foto qualquer posta de exibição
da_tesoura = tk.Label(root, image=imagem4)
# da_tesoura.place(x=65, y=70)  # Definindo a posição do label





# Texto que convida ao jogo
texto_label = tk.Label(root, text="O Computador já fez a escolha dele. \nFaça a sua:")
texto_label.place(x=100, y=25)  

# Primeira fala do computador
fala_pc = tk.Label(root, text="Vamos. Estou esperando.") 
fala_pc.place(x=136, y=310)  

# Segunda fala do computador
fala_pc2 = tk.Label(root, text="Você teve sorte.") 
fala_pc3 = tk.Label(root, text="Sempre vencerei!") 

# Fala do empate
fala_pc4 = tk.Label(root, text="Empates me frustram.")




# Botões
botao1 = tk.Button(root, text="PEDRA 🪨", command=botao1_click)
botao1.place(x=60, y=67, width=85, height=25) 

botao2 = tk.Button(root, text="PAPEL 📜", command=botao2_click)
botao2.place(x=160, y=67, width=85, height=25)  

botao3 = tk.Button(root, text="TESOURA ✂️", command=botao3_click)
botao3.place(x=260, y=67, width=85, height=25)  

botao4 = tk.Button(root, text="SAIR", command=botao4_click)
botao4.place(x=215, y=350, width=85, height=25) 

botao5 = tk.Button(root, text="DE NOVO", command=botao5_click)
botao5.place(x=85, y=350, width=85, height=25)  

root.mainloop()


