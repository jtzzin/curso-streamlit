import numpy as np; # lib de dados
import pandas as pd; #lib de dados
import streamlit as st;

st.title("Lidando com dados e graficos");
st.header(" --- Gerando dados aleatorios e frames interativos --- ");

# Criando um dataframe (tabelas) de exemplo
df = pd.DataFrame (
    np.random.randn(20, 3), # gerando 20 linhas e 3 colunas
    columns=["a", "b", "c"] # nomes para as colunas

)

# mostrar a tabela
st.subheader(" DataFrame gerado: ")
st.dataframe(df); # instancia ele (se eu deixar apenas - st.table -, nao fica possivel buscar nada)

# exibindo graficos simples com os dados gerados

st.subheader("Graficos intuitivos: ");
st.line_chart(df); # aqui, o grafico vai ser em linhas
st.bar_chart(df);# grafico de barras
# fim dos dados aleatorios

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Fazendo upload do proprio pc para o site

st.subheader("Inserindo dados CSV da maquina local: ");
upload = st.file_uploader (
    label=("Envie o seu arquivo CSV: "),
    type="CSV", # retorna apenas os arquivos CSV para adiantar o processo
)

# verificando se houve o envio do arquivo csv
if upload is not None:
    try:
        # mostar um pouco do arquivo
        df_upload = pd.read_csv(upload) # variavel que armazena o dataframe e faz a leitura com o pd (pandas)
        st.success("Arquivo carregado com sucesso! "); # msg de sucesso
        st.write("Suas primeiras 5 linhas do arquivo"); # texto informativo
        st.dataframe(df_upload.head()); # ela mostra, como padrao, as 5 primeiras linhas do arquivo, podendo mudar

    # buscando duas colunas para validar o arquivo
        if df_upload.shape[1] >= 2: # verificando se a coluna é igual ou maior que 2
             st.subheader("Grafico das duas primeiras colunas"); 
             st.line_chart(df_upload.iloc [:, :2]) # retorna todas as linhas, mas da primeira até a segunda coluna apenas

    # caso nao passe de duas colunas
        else: 
            st.info("arquivo com menos de duas colunas, erro.");
    
    # mensagem de erro se nao der certo
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo, certifique-se de enviar um arquivo CSV valido")






