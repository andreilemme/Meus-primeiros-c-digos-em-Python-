import requests

def buscar_user_instagram(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info?username={username}"
    
    response = requests.get(
        url,
        headers={"User-Agent": "Instagram 88.0.0.17.109"},
        timeout=5
    )
    
    try:
        resultado = response.json()
        conta = {
            'exists': True,
            'user_id': resultado['logging_page_id'].replace('profilePage_', ''),
            'full_name': resultado['graphql']['user']['full_name'],
            'perfil_curtidas': resultado['graphql']['user']['edge_followed_by']['count'],
            'biografia': resultado['graphql']['user']['biography']
        }
        
        return conta
        
    except (KeyError, ValueError):
        return {'exists': False}

# Substitua "nomedousuario" pelo username do Instagram
resultado = buscar_user_instagram("cristianoronaldo")

if resultado['exists']:
    print("Projeto Encontrado:")
    print("- ID:", resultado['user_id'])
    print("- Nome Completo:", resultado['full_name']) 
    print("- Curtidas:", resultado['perfil_curtidas'])
    print("- Bio:", resultado['biografia'])
else:
    print("Nao foi possivel encontrar o projeto.")