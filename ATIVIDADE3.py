# importado o conector do banco de dados
import mysql.connector
#criado a conexão ao SGBD

con=mysql.connector.connect(host='localhost',user='root',password='rica15')

if con.is_connected():
    
    db_info=con.get_server_info()
    print("conectado ao sevidor myswl versão, ",db_info)
    cursor=con.cursor()

    # CRIANDO O BANCO DE DADOS ATIVIDADE 3

    cursor.execute("CREATE DATABASE  IF NOT EXISTS ATIVIDADE3 ;")
    cursor.execute("USE ATIVIDADE3;")

    #CRIANDO A TABELA CARROS E SEUS ATRIBUTOS

    cursor.execute("""CREATE TABLE IF NOT EXISTS CARROS(
                    ID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT  NOT NULL,
                    FABRICANTE VARCHAR(20) NOT NULL,
                    MARCA VARCHAR(20) NOT NULL,
                    MODELO VARCHAR(20) NOT NULL,
                    ANO_FABR DATE NOT NULL,
                    PLACA_VEICULO VARCHAR(7) NOT NULL,
                    NOME_PROPRIETARIO VARCHAR(50) NOT NULL,
                    CPF_PROPRIETARIO NUMERIC(11) NOT NULL,
                    TEL_PROP VARCHAR(11) NOT NULL,
                    END_PROP VARCHAR(50),
                    DEFEITO_APRESENTADO VARCHAR(200) NOT NULL,
                    DESCRICAO_ORCAMENTO VARCHAR(5000), 
                    VALOR_ORCAMENTO NUMERIC(10,2));
                    """)
        #cursor.execute("Describe CARROS")
    #cursor.execute('''INSERT INTO CARROS VALUES (6,'FIAT','JEEP','RENEGADE','2022-01-01','MEU0001','PROFESSOR LINDOLFO',12345678910,'11999999999',
     #               'RUA DESCOMPLICA','CARRO SEM COMBUSTIVEL', 'FAZER A COMPRA DE COMUBSTIVEL NO POSTO MAIS PRÓXIMO DA SUA RESIDÊNCIA',1000.00);''')   
  
   # cursor.execute("commit;")

    cursor.execute("Select * FROM CARROS")

   # cursor.execute("SELECT * FROM CARROS")
    show=cursor.fetchall()
    print("id          ","FABRICANTE        "," MARCA       ","Modelo        ","Ano de Fabricação ","Placa      ","Proprietário       ","CPF        ","   Telefone         " ,"Endereço   ","              DEFEITO       ","                Descrição do orçamento     ", "                                                                  Valor do Orçamento")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________")

    for  atividade3 in show:
        print(atividade3[0], "            ",atividade3[1],"              ",atividade3[2],"     ",atividade3[3],"     ",atividade3[4],"       ",atividade3[5],"   ",atividade3[6],"",atividade3[7],"  ",atividade3[8],"     ",atividade3[9],"         ",atividade3[10], "        ",atividade3[11],"                       ",atividade3[12])
        
        
        
        
        
        
        
       
        
       # print("Valor orçamento= ", atividade3[12])

        print("_____________________________________________________________________________________________________________________________________________________________________________________________________")
    linha=cursor.fetchone()


    
if con.is_connected():
    cursor.close()
    con.close()
    print ("conexão ao mysql foi encerrada")