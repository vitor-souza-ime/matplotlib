# Script de Plotagem de Funções Matemáticas

Este repositório contém um script Python que gera gráficos de várias funções matemáticas utilizando as bibliotecas NumPy e Matplotlib. O script cria uma grade de subgráficos 4x2, exibindo os gráficos das funções linear, quadrática, cúbica, quártica, seno, cosseno, gaussiana e sigmoide no intervalo \([-10, 10]\).

## Visão Geral

O script define oito funções matemáticas comuns e as visualiza em subgráficos separados. Cada gráfico inclui uma grade, eixos horizontais e verticais em zero, e um título para maior clareza. As funções plotadas são:
- Linear 
- Parabólica
- Cúbica 
- Quártica
- Seno 
- Cosseno 
- Gaussiana 
- Sigmoide 

## Funcionalidades
- Gera uma grade de subgráficos 4x2 usando Matplotlib.
- Plota funções com uma resolução de 400 pontos no intervalo \([-10, 10]\).
- Inclui linhas de grade e marcadores de eixos para melhor visualização.
- Utiliza formatação no estilo LaTeX para os títulos das funções.

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Instalação
1. Clone o repositório ou baixe o script:
   ```bash
   git clone https://github.com/seuusuario/plotagem-funcoes-matematicas.git
   cd plotagem-funcoes-matematicas
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install numpy matplotlib
   ```

## Uso
1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o script:
   ```bash
   python main.py
   ```
3. O script abrirá uma janela exibindo a grade de gráficos 4x2. Feche a janela para encerrar o programa.

## Estrutura do Código
- **Importações**: Utiliza `numpy` para operações numéricas e `matplotlib.pyplot` para plotagem.
- **Geração de Dados**: Cria um array `x` usando `np.linspace(-10, 10, 400)`.
- **Funções**: Define uma lista de tuplas contendo valores `x`, valores `y` e títulos para cada função.
- **Plotagem**: Usa `plt.subplots()` para criar uma grade 4x2 e plota cada função com títulos e formatação apropriados.

## Exemplo de Saída
O script produz uma figura com 8 subgráficos, cada um mostrando uma função diferente. Os títulos são exibidos em formato matemático (e.g., \(x\), \(x^2\)), e a grade facilita a leitura.

## Contribuição
Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests para adicionar novas funções, melhorar a visualização ou aprimorar a documentação. Por favor, siga o estilo de código existente e inclua testes, se aplicável.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes (se não estiver incluído, considere adicionar um).

## Agradecimentos
- Inspirado em exemplos educacionais para visualização de funções matemáticas.
- Utiliza bibliotecas de código aberto: NumPy e Matplotlib.


