# Acessar https://labs.play-with-docker.com/ e logar com usuário e senha do Dockerhub
# Clonar o git com o seguinte comando: git clone https://github.com/matheusmoreti/projetoDockerCompose.git
# Acessar a pasta com o seguinte comando: cd projetoDockerCompose
# Iniciar o manager swarm com o comando: docker swarm init --advertise-addr 192.168.0.23
# Criar um novo stack com o comando: docker stack deploy -c docker-compose.yml stackFiap
# Listar serviços: docker service ls
# Iniciar o serviço: docker service scale ymjs3lryimmv=3
######################################################################################
# Para subir imagem para dockerHub:
# Utilizar comando: docker login
# Utilizar o comando para ver as tags: docker images
# Para criar a tag, utilizar o comando: docker tag nome_da_tag_1 [seu_usuario]/[nome_da_imagem_1]
# Para criar a tag, utilizar o comando: docker tag nome_da_tag_2 [seu_usuario]/[nome_da_imagem_2]
# Para dar push na imagem criada, utilizar o comando: docker push [seu_usuario]/[nome_da_imagem_1]
# Para dar push na imagem criada, utilizar o comando: docker push [seu_usuario]/[nome_da_imagem_2]
