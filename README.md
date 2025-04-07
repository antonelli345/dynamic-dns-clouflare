# 🌐 Dynamic DNS Updater for Cloudflare

Atualize automaticamente seu IP público no Cloudflare, perfeito para conexões residenciais com IP dinâmico. Ideal para manter seu domínio sempre apontando pro IP correto, mesmo com mudanças!

---

## ✨ Funcionalidades

- 🔍 Descobre seu IP público
- 🔄 Atualiza automaticamente o registro DNS tipo "A" no Cloudflare
- 🖥 Ideal para rodar via `crontab` no Linux
- ⚙️ Uso simples com variáveis de ambiente

---

## ⚙️ Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/seuusuario/dynamic-dns-cloudflare.git
cd dynamic-dns-cloudflare
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure seu `.env` (baseado no `.env.example`)

```dotenv
API_TOKEN=sua_chave
ZONE_ID=sua_zone_id
DNS_RECORD_ID=seu_dns_id
DNS_RECORD_NAME=example.com
```

### 4. Execute o script manualmente

```bash
python update_dns.py
```

### 5. (Opcional) Adicione no `crontab` para execução automática

Execute:

```bash
crontab -e
```

E adicione:

```bash
*/10 * * * * cd /caminho/para/seu/script && /usr/bin/python3 update_dns.py >> cron.log 2>&1
```

#### 📌 Explicando:

- `*/10 * * * *`: a cada 10 minutos  
- `cd ... &&`: garante que o script será executado no diretório certo (pra ler o `.env` corretamente)  
- `>> cron.log 2>&1`: salva a saída (stdout + stderr) no arquivo `cron.log`

---

## 📌 Melhorias Futuras

- [ ] **Notificações via WhatsApp**  
  Enviar mensagens automáticas usando uma API como UltraMsg ou WhatsApp Cloud API:
  - ✅ Enviar a cada 12h quando tudo estiver ok
  - ❌ Enviar imediatamente caso a atualização falhe

- [ ] **Evitar requisições desnecessárias**  
  Verificar se o IP mudou antes de tentar atualizar o DNS

- [ ] **Logs rotativos**  
  Implementar rotação de logs para evitar arquivos gigantes

- [ ] **Interface Web leve**  
  Para exibir status atual, logs e hora da última atualização

- [ ] **Versão em Docker**  
  Facilitar o deploy com Docker e Docker Compose

---

## 🧪 Testado em

- ✅ Python 3.10+
- ✅ Linux (Debian/Ubuntu)

---

## 📝 Licença

MIT. Sinta-se à vontade para usar, modificar e compartilhar.  
Pull Requests são bem-vindos! 😄

> Projeto pessoal criado com 💡 para resolver uma dor real.  
> Ideal pra quem hospeda sites ou serviços em casa com IP dinâmico.
