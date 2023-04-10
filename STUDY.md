# 🚨🚨 ESSE DOCUMENTO IRA ARMAZENAR LEVANTAMENTOS INICIAIS. CABE RESSALTAR QUE QUALQUER DIFICULDADE/LIMITAÇÃO DESCRITA ABAIXO NÃO IMPEDE O PROJETO DE CONTINUAR, SERVE APENAS PARA NORTEAR A ESCOLHA DAS TECNOLOGIAS E MÉTODOS.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1200px-ChatGPT_logo.svg.png" alt="ChatGPT" width="5%"/> 

# Informações obtidas em pesquisas na ferramenta [ChatGPT](https://chat.openai.com/chat)

#### Dicas para começar um projeto de visão computacional

1. Começar um projeto de visão computacional pode ser bastante desafiador, mas também pode ser muito empolgante! Aqui estão algumas sugestões para ajudá-lo a começar:

2. Aprenda as bases da visão computacional: antes de começar a construir seu sistema, é importante ter uma compreensão sólida dos conceitos básicos da visão computacional, como processamento de imagem, detecção de bordas, segmentação de imagem e classificação. Existem muitos recursos on-line disponíveis para ajudá-lo a aprender esses conceitos, como cursos gratuitos, tutoriais e livros.

3. Escolha uma plataforma de desenvolvimento: existem várias plataformas de desenvolvimento de visão computacional disponíveis que podem ajudá-lo a acelerar o desenvolvimento do seu sistema. Alguns exemplos incluem OpenCV, TensorFlow, PyTorch, Caffe e Keras.

4. Colete dados: um passo crucial na construção de um sistema de visão computacional é coletar dados de treinamento. Você pode usar um conjunto de dados público existente ou criar seu próprio conjunto de dados.

5. Treine um modelo de aprendizado de máquina: após coletar seus dados, você precisará treinar um modelo de aprendizado de máquina para reconhecer objetos em imagens. Existem vários tipos de modelos de aprendizado de máquina que você pode usar, como redes neurais convolucionais (CNNs), redes de detecção de objetos (ODs) e redes de segmentação de imagem.

6. Teste e ajuste seu modelo: uma vez que você tenha treinado seu modelo, você precisará testá-lo em um conjunto de dados de teste para avaliar sua precisão. Você pode precisar ajustar seu modelo várias vezes para obter os resultados desejados.

7. Integre seu modelo em um sistema de vigilância: finalmente, você pode integrar seu modelo em um sistema de vigilância que irá analisar as imagens da câmera em tempo real e alertar quando detectar uma invasão ou outra atividade suspeita.

#### Lembre-se de que a construção de um sistema de visão computacional pode ser um processo complexo e demorado, mas com persistência e dedicação, você pode criar um sistema eficaz que possa ajudar a manter sua propriedade segura.

# Continuação das informações.
Criar um programa de visão computacional para identificar invasão de perímetro em escolas usando CFTV pode ser um projeto interessante. No entanto, é importante notar que isso é um projeto complexo que exigirá habilidades avançadas em programação, visão computacional, inteligência artificial e aprendizado de máquina. Além disso, você precisará de um conjunto de dados grande e rotulado para treinar seu modelo de visão computacional.

Para começar, você precisará de uma câmera de segurança CFTV que cubra o perímetro da escola e capture imagens em tempo real. Em seguida, você pode usar uma biblioteca de processamento de imagens como OpenCV para processar as imagens capturadas. Com o OpenCV, você pode aplicar técnicas de detecção de bordas, segmentação de objetos e rastreamento de objetos para identificar objetos em movimento na imagem.

Em seguida, você pode treinar seu modelo de aprendizado de máquina para identificar se um objeto em movimento é uma pessoa ou outra coisa, como um animal ou um objeto inanimado. Você pode fazer isso criando um conjunto de dados rotulado que inclua exemplos de pessoas invadindo o perímetro da escola e exemplos de outras coisas em movimento, como animais ou carros.

Depois de treinar seu modelo de visão computacional, você pode usá-lo para detectar pessoas invadindo o perímetro da escola em tempo real. Quando o modelo detectar uma invasão, você pode configurá-lo para alertar as autoridades ou para tomar outras medidas de segurança apropriadas.

É importante lembrar que a criação de um programa de visão computacional para fins de segurança deve ser feita com cuidado e com a devida autorização e consentimento das autoridades responsáveis

# Possíveis dificuldades legais:

A utilização de câmeras de vigilância em escolas pode estar sujeita a leis e regulamentações locais, estaduais e nacionais. É importante considerar as leis e regulamentações aplicáveis antes de implementar um sistema de segurança baseado em visão computacional.

A seguir estão algumas leis e regulamentações que podem afetar a utilização de câmeras de vigilância em escolas:

1. Lei Geral de Proteção de Dados (LGPD) - Lei nº 13.709/2018: A utilização de câmeras de vigilância pode envolver a coleta, armazenamento e processamento de imagens de pessoas, o que pode ser considerado dados pessoais. A LGPD estabelece regras para o tratamento de dados pessoais, incluindo a coleta, uso, armazenamento e compartilhamento de dados pessoais.

2. Lei de Acesso à Informação - Lei nº 12.527/2011: A LAI pode ser aplicável à utilização de câmeras de vigilância em escolas. A LAI estabelece regras para o acesso à informação pública, incluindo informações coletadas por órgãos públicos, como escolas.

3. Legislação de Proteção à Privacidade: Dependendo da jurisdição, pode haver leis e regulamentações específicas de proteção à privacidade que regem a utilização de câmeras de vigilância em espaços públicos, como escolas. No Brasil, por exemplo, o Marco Civil da Internet (Lei nº 12.965/2014) e o Código de Defesa do Consumidor (Lei nº 8.078/1990) também podem ser aplicáveis.

4. Direitos Humanos: A utilização de câmeras de vigilância em escolas pode afetar os direitos humanos, como o direito à privacidade, à liberdade de expressão e à liberdade de movimento. É importante considerar os direitos humanos ao implementar um sistema de segurança baseado em visão computacional. Os direitos humanos estão previstos na Constituição Federal (CF) e em tratados internacionais de direitos humanos ratificados pelo Brasil, como a Convenção Americana de Direitos Humanos e o Pacto Internacional de Direitos Civis e Políticos.

Em resumo, a utilização de câmeras de vigilância em escolas pode estar sujeita a leis e regulamentações locais, estaduais e nacionais. É importante considerar as leis e regulamentações aplicáveis antes de implementar um sistema de segurança baseado em visão computacional e garantir que o sistema esteja em conformidade com as leis e regulamentações aplicáveis.

# Possíveis ferramentas Open Source para serem utilizadas:

#### Existem vários sistemas de código aberto disponíveis na internet que podem ser úteis para implementar uma solução de detecção de invasões em escolas e creches. Aqui estão alguns exemplos:

1. **OpenALPR**: é um software de reconhecimento automático de placas de veículos de código aberto que pode ser usado para identificar veículos suspeitos nas imediações da escola ou creche. Ele usa técnicas de visão computacional para detectar e reconhecer placas de veículos em imagens capturadas pelas câmeras de vigilância.

2. **MotionEye**: é um software de vigilância de código aberto que pode ser usado para configurar câmeras de vigilância em uma rede local. Ele suporta a integração de câmeras IP, webcams e outros dispositivos de captura de imagens e pode ser usado para monitorar e gravar imagens em tempo real.

3. **OpenCV**: é uma biblioteca de visão computacional de código aberto que pode ser usada para processar imagens capturadas pelas câmeras de vigilância. Ele fornece uma ampla variedade de funções de processamento de imagens, como detecção de objetos, rastreamento de movimento e reconhecimento de padrões.

4. **Darknet**: é uma biblioteca de aprendizado de máquina de código aberto que pode ser usada para treinar e implementar modelos YOLO para detecção de objetos em imagens de vigilância. Ele inclui várias implementações de modelos YOLO pré-treinados e pode ser usado para treinar modelos personalizados com conjuntos de dados próprios.

#### É importante lembrar que, ao usar sistemas de código aberto, é necessário avaliar cuidadosamente a segurança e a confiabilidade do software antes de integrá-lo em seu projeto. Além disso, é importante seguir as leis e regulamentações locais relacionadas à privacidade e segurança de dados.

# <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" alt="YouTube" width="5%"/> Vídeos no youtube

**[Playlist Visão Computacional - Canal Programação Dinâmica]** (https://www.youtube.com/playlist?list=PL5TJqBvpXQv729nb3vdeP4E87hLark5q9)

