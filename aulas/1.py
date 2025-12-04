import streamlit as st;

# conteudo da pagina em si, nao do menu da lateral
st.title("Aula sobre botoes e side bar");

st.header("veremos como criar uma barra lateral no site");
# fim pagina

# side bar
st.sidebar.header("aqui, comecamos com a sidebar de fato");

# campo input de nome 
nome = st.sidebar.text_input(label=("Informe o teu nome:"));

st.sidebar.write(f"ola, {nome}");

#criando colunas
colunas = st.columns(3); # criando tres espacos de colunas

# inicio da coluna 1
with colunas [0]:
    st.header("Coluna 1");
    if st.button("Clique aqui!"): # botao para apertar e receber um  em verde
        st.success("voce apertou mesmo!"); # aviso

    # criando uma barra de arrastar - slider -
    valor_slider = st.slider (
        label="Arraste o campo abaixo:", # sempre que criar um widget, informar uma label de campo

        min_value=0,
        max_value=(1000),
        value=0 # valor que comeca por padrao ao entrar o site

    )

    st.write(f"o valor selecionado foi: {valor_slider}")
    # fim da coluna 1

    #coluna 2
    with colunas[1]:
        st.header("Coluna 2");
        st.info("essa é uma mensagem informativa"); # msg de info azul

        #aqui, pode inserir url de img ou direto do caminho do pc
        st.image(
            image="https://streamlit.io/images/brand/streamlit-logo-primary-lightmark-lighttext.png", # caminho da img, local ou publica
            caption="exemplo usando link", # legenda da img,
            use_container_width=True # usa todo o espaco possivel do campo
        )


    
       
    