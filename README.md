# py-learn-japanese

**py-learn-japanese** é um programa interativo para aprender e praticar os alfabetos japoneses (Hiragana e Katakana). Ele fornece um ambiente divertido para treinar e dominar os caracteres japoneses, acompanhando o progresso do usuário e oferecendo feedback dinâmico.

## 📂 Estrutura do Projeto

```
py-learn-japanese/
├── assets/
│   ├── hiragana.json         # Arquivo com os caracteres Hiragana
│   ├── katakana.json         # Arquivo com os caracteres Katakana
├── AlphabetTrainer.py        # Lógica para treinamento dos alfabetos
├── main.py                   # Arquivo principal para execução do programa
├── runGame.py                # Lógica do fluxo do jogo
├── requirements.txt          # Dependências do projeto
```

## 🛠️ Configuração e Uso

Siga os passos abaixo para configurar e executar o programa:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o programa**:
   ```bash
   python main.py
   ```

## 📝 Pré-requisitos

- **Python 3.8 ou superior**  
  Certifique-se de que o Python esteja instalado no sistema. Você pode verificar a versão instalada com:
  ```bash
  python --version
  ```

## 🌟 Recursos

- **Treinamento com Hiragana e Katakana**: Teste seus conhecimentos com ambos os alfabetos japoneses.
- **Feedback dinâmico**: Receba mensagens baseadas no desempenho, motivando seu progresso.
- **Customização de tempos e dificuldade**: Adapte o programa ao seu nível de aprendizado.

## 📦 Dependências

As bibliotecas necessárias para o projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de executar o programa.

## 🚀 Próximos Passos

- [ ] Adicionar suporte ao alfabeto Kanji.
- [ ] Criar interface gráfica para o programa.

## 📜 Licença

Este projeto é de código aberto e está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais informações.
