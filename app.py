import streamlit as st 

generos = {
    'Trap' : {
        'Matuê' :'https://www.youtube.com/watch?v=zctKiN-okXI',
        'Teto' : 'https://www.youtube.com/watch?v=EjEqRyWZiT4',
        'Wiu' :'https://www.youtube.com/watch?v=wFBp_PHXrf4',
        'KayBlack' : 'https://www.youtube.com/watch?v=sQzchBJ2KvM'

    }, 
    'Funk' : {
        'Mc Tuto' : 'https://www.youtube.com/watch?v=S_O_iKYYaRs',
        'Mc Kevin' : 'https://www.youtube.com/watch?v=M8E9BZp2tKw',
        'Mc IG' : 'https://www.youtube.com/watch?v=QkIf6Y_XWpE',
        'Mc Ryan Sp' : 'https://www.youtube.com/watch?v=HAIlJRfEeBE'
    }, 
    'Rap' : {
        'Drake' : 'https://www.youtube.com/watch?v=HL1UzIK-flA',
        '50cent' : 'https://www.youtube.com/watch?v=5qm8PH4xAss',
        'Kaney West' : 'https://www.youtube.com/watch?v=Bm5iA4Zupek',
        'YNW Melli' : 'https://www.youtube.com/watch?v=sjUHRlfIlN4'
    }, 
    'Pagode' : {
     'Arlindo Cruz' : 'https://www.youtube.com/watch?v=vNK58tL6J70',
     'thiaguinho': 'https://www.youtube.com/watch?v=qUqc_cYejX0',
     'Ferrugem' : 'https://www.youtube.com/watch?v=JhXagtxvDKY',
     'pixote' : 'https://www.youtube.com/watch?v=QxamVP2dJCA'
     
      }, 

}

st.sidebar.title('Bob playlist 🎵🎶')
st.sidebar.image('bob.png')

genero = st.sidebar.selectbox('Selecione um genero músical', generos.keys())

artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)

video, sobre = st.tabs(['Video','Sobre o artista '])

with video: 
    st.video(generos[genero][artista])

    with sobre:
         if artista == 'Matuê': 
             st.markdown('''
              Matheus Brasileiro Aguiar (Fortaleza, 11 de outubro de 1993), mais conhecido como Matuê, é um rapper, cantor, compositor, guitarrista e empresário brasileiro. Ficou conhecido com o single "Anos Luz", lançado em 2017 e pelo álbum "Máquina do Tempo" lançado em 2020. É considerado um dos símbolos do trap brasileiro.[1][2]

             Foi o único artista de hip hop em 2023 a ter 10 músicas com mais de 100 milhões de streams nas plataformas digitais.
             ''')
        
         elif artista == 'Teto': 
             st.markdown('''

             Clériton Sávio Santos Silva (Jacobina, 19 de outubro de 2001), mais conhecido como Teto, é um rapper, cantor e compositor brasileiro. Ficou conhecido por meio das prévias de suas músicas que foram lançadas não oficialmente em vários canais do YouTube, alcançando milhões de visualizações e ganhando fama em redes sociais como o TikTok e Instagram.
             ''')
        
         elif artista == 'Wiu':
             st.markdown(''' Vinicius William Sales de Lima, (Fortaleza, 16 de fevereiro de 2002) mais conhecido como WIU, é um rapper, cantor, compositor e produtor musical brasileiro. Ficou conhecido com os singles "Felina", "Horas Iguais", "Coração de Gelo" e pelo álbum "Manual de Como Amar Errado", lançado em 2022.
             ''')

         elif artista == 'KayBlack':
             st.markdown(''' Kaique Menezes , conhecido pelo seu nome artístico KayBlack ( nascido em 12 de março de 2000 em São Paulo ), é um músico brasileiro que é conhecido por sua mistura de funk e rap . Em abril de 2023, ele se tornou o segundo artista mais transmitido no Spotify no Brasil. 

             Ele colaborou com artistas como Xamã , Orochi e Tropkillaz . Ele também ganhou algum renome no mundo da moda , representando marcas de luxo internacionalmente. 
             ''')

         elif artista == 'Mc Tuto' :
             st.markdown(''' Emerson Teixeira Muniz (São Paulo, 9 de julho de 2000), mais conhecido como MC Tuto, é um cantor e compositor brasileiro. Recebeu maior reconhecimento por participar do "The Box Medley Funk 2",[1][2] e pela sua música "Barbie".[3] É um dos artistas mais populares do Brasil em 2025 de acordo com a lista de Billboard Artistas 25.
             ''')

         elif artista == 'Mc Kevin':
             st.markdown(''' Kevin Nascimento Bueno (São Paulo, 29 de abril de 1998  Rio de Janeiro, 16 de maio de 2021), conhecido artisticamente como MC Kevin, foi um cantor e compositor brasileiro.
             ''')

         elif artista == 'Mc IG':
             st.markdown(''' Guilherme Sérgio Ramos de Souza (São Paulo, 10 de maio de 1997) mais conhecido como MC IG, é um cantor, compositor e empresário brasileiro. Ele ficou conhecido pelos seus singles “3 Dias Virado”, “Goodnight Menina” e pela canção “Let’s go 4” lançado em 2023.[1]
             ''')

         elif artista == 'Mc Ryan Sp':
             st.markdown(''' Ryan Santana dos Santos (São Paulo, 2 de fevereiro de 2001), mais conhecido como MC Ryan SP, é um cantor e compositor brasileiro.
             ''')

         elif artista == 'Drake': 
             st.markdown('''Aubrey Drake Graham (nascido em 24 de outubro de 1986) é um rapper, cantor e ator canadense. Ele é creditado por popularizar a sensibilidade do R&B na música hip-hop . Drake ganhou reconhecimento pela primeira vez estrelando como Jimmy Brooks na série de drama adolescente da CTV Television Network, Degrassi: The Next Generation (2001–2008) e começou sua carreira musical lançando de forma independente as mixtapes Room for Improvement (2006), Comeback Season (2007) e So Far Gone (2009) antes de assinar com a Young Money Entertainment . [ 5 ]
             ''')

         elif artista == '50cent':
             st.markdown(''' Curtis James Jackson III, mais conhecido pelo seu nome artístico 50 Cent (Nova Iorque, 6 de julho de 1975),[1] é um rapper, compositor, ator, diretor, roteirista e empresário norte-americano. Ficou conhecido com o lançamento dos álbuns Get Rich or Die Tryin' (2003) e The Massacre (2005). Get Rich or Die Tryin' obteve a certificação de platina seis vezes pela RIAA e vendeu cerca de 13 milhões de cópias em todo o mundo.[2][3] Seu disco The Massacre foi certificado cinco vezes pela RIAA[2] e vendeu 11 milhões de cópias.[4]
             ''')

         elif artista ==  'Kaney West':
             st.markdown(''' Ye[1] (em inglês: Ye; romaniz.: [je]; YAY; nascido Kanye Omari West; Atlanta, 8 de junho de 1977), mais conhecido como Kanye West (em inglês: Kanye West; romaniz.: [ˈkɑːnjeɪ]; KAHN-yay),[8] é um rapper, compositor, produtor musical, político e designer de moda americano.[9][10][11] West ficou famoso no início de sua carreira como produtor da Roc-A-Fella Records, onde ganhou reconhecimento pelo seu trabalho no álbum The Blueprint, de Jay-Z, assim como por hits para outros cantores como Alicia Keys, Ludacris, Janet Jackson e outros. Atualmente, como vocalista, West é o 4.º artista que mais vendeu músicas em formato digital.[12] Além disso, ele acumula uma impressionante coleção de prêmios, incluindo um total de 24 Grammys, tornando-se assim o maior rapper da história da premiação. Sua notável conquista de 24 Grammys também o posiciona como o 7.º artista mais laureado dentre todas as edições da premiação.[13] Para além disso, em 2024, a Billboard elegeu Kanye West como a sétima maior estrela pop do período 2000–2024.[14]
             ''')

         elif artista == 'YNW Melli':
             st.markdown(''' Jamell Maurice Demons (Gifford, 1 de maio de 1999), conhecido profissionalmente como YNW Melly, é um rapper, cantor e compositor americano. De Gifford, Flórida. Ele é mais conhecido por suas músicas "Murder on My Mind"[1] e "Mixed Personalities", com Kanye West . Seu single "Murder on My Mind" é considerado a fuga de YNW Melly, que ganhou ainda mais atenção depois que o rapper foi acusado de duplo assassinato.[2] Ele lançou seu álbum de estréia, "We All Shine", em 17 de janeiro de 2019, que recebeu uma resposta positiva da crítica. Ele também tem um irmão cantor/compositor chamado YNW Bslime, e eles têm uma música juntos chamada “Dying For You”.
             ''')

         elif artista == 'Arlindo Cruz':
             st.markdown(''' Arlindo Domingos da Cruz Filho OMC (Rio de Janeiro, 14 de setembro de 1958  Rio de Janeiro, 8 de agosto de 2025) foi um cantor, compositor e músico brasileiro. Em trinta e seis anos de carreira lançou vinte e três álbuns, sendo nove enquanto integrante do Fundo de Quintal, cinco em parceria com o sambista Sombrinha e nove em carreira solo.
             ''')

         elif artista == 'thiaguinho':
             st.markdown(''' Thiago André Barbosa (Presidente Prudente, 11 de março de 1983), mais conhecido pelo seu nome artístico Thiaguinho, é um cantor, compositor, apresentador e empresário brasileiro.
             Tornou-se conhecido após participar do talent show Fama, em 2002,[2][3] e ganhou notoriedade na música por ter sido integrante do grupo de samba e pagode Exaltasamba, no qual permaneceu de 2003 a 2012.[4] Em 2012 lançou seu primeiro álbum e DVD solo, Ousadia & Alegria, que recebeu uma indicação ao Grammy Latino na categoria Melhor Álbum de Samba/Pagode e certificado de platina pelas 80 mil cópias vendidas.[5] Em 2014 foi lançado o álbum Outro Dia, Outra História, que lhe rendeu certificado de disco de ouro pelas 40 mil cópias vendidas. Hey, Mundo!, seu terceiro álbum, foi lançado em 2015 e recebeu certificação de disco de dupla platina pelas 160 mil cópias vendidas. Seu segundo DVD #VamoQVamo foi lançado em 2016. Em janeiro de 2017 lançou o álbum Tardezinha.[6] Seu álbum Só Vem foi lançado em 2017 e recebeu certificado de ouro pelas 40 mil cópias vendidas. Em junho de 2018 lançou o álbum Tardezinha 2.[7] Em setembro de 2019 lançou Vibe, seu terceiro DVD da carreira
             ''')

         elif artista == 'Ferrugem':
             st.markdown(''' Jheison Failde de Souza (Rio de Janeiro, 20 de outubro de 1988), mais conhecido pelo nome artístico Ferrugem, é um cantor e compositor brasileiro.[1]
             Após ganhar destaque com a canção "Climatizar" nas rádios, Ferrugem assinou com a gravadora Warner Music Brasil e lançou em 2015 seu álbum de estreia Climatizar. Seu segundo álbum Seja o Que Deus Quiser foi lançado em 2017.[2] Porém Ferrugem só obteve visibilidade nacional após o lançamento do seu primeiro DVD Prazer, eu sou Ferrugem, lançado em 2018.[3] O álbum lhe rendeu uma indicação ao Grammy Latino na categoria Melhor Disco de Samba e Pagode.[4] Em 2019, lançou seu segundo DVD Chão de Estrelas
             ''')

         elif artista == 'pixote':
             st.markdown('''Pixote, a Lei do Mais Fraco é um filme brasileiro de 1980,[2] do gênero drama, dirigido por Hector Babenco. O roteiro do filme foi escrito por Babenco e Jorge Durán, sendo baseado no livro de romance-reportagem[3] Infância dos Mortos do escritor José Louzeiro.
             ''')

