from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura o Microsoft Edge WebDriver
service = Service('C:/WebDrivers/msedgedriver.exe')  # Ajuste o caminho
try:
    driver = webdriver.Edge(service=service)
except Exception as e:
    print(f"Erro ao inicializar o WebDriver: {e}")
    print("Verifique se o msedgedriver.exe está no caminho correto e compatível com o Edge.")
    exit(1)

# Acessa o WhatsApp Web
try:
    driver.get("https://web.whatsapp.com/")
except Exception as e:
    print(f"Erro ao acessar o WhatsApp Web: {e}")
    print("Verifique sua conexão ou se a VPN está interferindo.")
    exit(1)

# Aguarda o usuário escanear o QR code
print("Escaneie o QR code na tela com o WhatsApp no seu celular (você tem 60 segundos)...")
try:
    # Aguarda a caixa de pesquisa aparecer, indicando login bem-sucedido
    search_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title="Caixa de texto de pesquisa"]'))
    )
except Exception as e:
    print(f"Erro: Não foi possível fazer login. QR code escaneado? Erro: {e}")
    driver.quit()
    exit(1)

# Encontra o chat do usuário
try:
    search_box.send_keys("+5519991217481")
    time.sleep(3)
    search_box.send_keys("\n")
    time.sleep(7)  # Aguarda o chat carregar

    # Captura mensagens
    messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]')
    if messages:
        for msg in messages:
            try:
                print(msg.text)
            except:
                continue
    else:
        print("Nenhuma mensagem encontrada.")
except Exception as e:
    print(f"Erro ao processar o chat: {e}")
    print("Verifique se o número está correto ou se o chat carregou.")

# Mantém o navegador aberto até você fechar
input("Pressione Enter para encerrar...")
driver.quit()